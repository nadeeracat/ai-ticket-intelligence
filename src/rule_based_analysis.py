from data_processing import load_and_process_tickets


def analyze_ticket_risks(df):
    """Identify delivery risks based on business rules."""

    risks = {}

    # High-priority overdue tickets
    risks["high_priority_overdue"] = df[
        (df["is_overdue"])
        & (df["priority"].isin(["High", "Critical"]))
    ]

    # Blocked tickets
    risks["blocked_tickets"] = df[
        (df["blocked"] == True)
    ]

    # Unassigned tickets
    risks["unassigned_tickets"] = df[
        (~df["has_assignee"])
        & (~df["status"].isin(["Done"]))
    ]

    # Missing acceptance criteria
    risks["missing_acceptance_criteria"] = df[
        (~df["has_acceptance_criteria"])
        & (~df["status"].isin(["Done"]))
    ]

    return risks


def print_risk_summary(risks):
    """Print a readable summary of identified risks."""

    print("\n" + "=" * 50)
    print("DELIVERY RISK SUMMARY")
    print("=" * 50)

    for risk_type, tickets in risks.items():
        print(f"\n{risk_type.replace('_', ' ').title()}")
        print(f"Count: {len(tickets)}")

        if not tickets.empty:
            print(
                tickets[
                    ["ticket_id", "title", "status", "priority"]
                ].to_string(index=False)
            )


if __name__ == "__main__":
    tickets = load_and_process_tickets()

    risks = analyze_ticket_risks(tickets)

    print_risk_summary(risks)
