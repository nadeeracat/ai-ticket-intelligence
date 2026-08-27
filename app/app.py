import sys
from pathlib import Path

import plotly.express as px
import streamlit as st

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT / "src"))

from analytics import (
    calculate_metrics,
    calculate_priority_distribution,
    calculate_status_distribution,
)
from data_processing import load_and_process_tickets
from rule_based_analysis import analyze_ticket_risks


st.set_page_config(
    page_title="AI Ticket Intelligence",
    page_icon="📊",
    layout="wide",
)

st.title("AI Ticket Intelligence")
st.subheader("Delivery risk detection and analytics dashboard")

tickets = load_and_process_tickets()
metrics = calculate_metrics(tickets)
risks = analyze_ticket_risks(tickets)


# KPI metrics
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Tickets", metrics["total_tickets"])
col2.metric("Overdue", metrics["overdue_tickets"])
col3.metric("Blocked", metrics["blocked_tickets"])
col4.metric(
    "Completion Rate",
    f"{metrics['completion_rate']}%",
)


# Charts
st.divider()

left, right = st.columns(2)

with left:
    priority_data = calculate_priority_distribution(tickets)

    fig = px.bar(
        priority_data,
        x="priority",
        y="ticket_count",
        title="Tickets by Priority",
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

with right:
    status_data = calculate_status_distribution(tickets)

    fig = px.pie(
        status_data,
        names="status",
        values="ticket_count",
        title="Tickets by Status",
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )


# Risk analysis
st.divider()
st.header("Delivery Risks")

for risk_type, risk_tickets in risks.items():
    risk_name = risk_type.replace("_", " ").title()

    with st.expander(
        f"{risk_name} ({len(risk_tickets)})"
    ):
        if risk_tickets.empty:
            st.success("No risks detected")
        else:
            st.dataframe(
                risk_tickets[
                    [
                        "ticket_id",
                        "title",
                        "status",
                        "priority",
                        "assignee",
                        "due_date",
                    ]
                ],
                use_container_width=True,
            )


# Full dataset
st.divider()
st.header("All Tickets")

st.dataframe(
    tickets,
    use_container_width=True,
)
