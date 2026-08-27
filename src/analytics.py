import pandas as pd


def calculate_metrics(df):
    """Calculate key delivery metrics."""

    metrics = {
        "total_tickets": len(df),

        "completed_tickets": len(
            df[df["status"] == "Done"]
        ),

        "blocked_tickets": len(
            df[df["blocked"] == True]
        ),

        "overdue_tickets": len(
            df[df["is_overdue"] == True]
        ),

        "unassigned_tickets": len(
            df[
                (~df["has_assignee"])
                & (~df["status"].isin(["Done"]))
            ]
        ),

        "tickets_without_acceptance_criteria": len(
            df[
                (~df["has_acceptance_criteria"])
                & (~df["status"].isin(["Done"]))
            ]
        ),
    }

    metrics["completion_rate"] = round(
        metrics["completed_tickets"]
        / metrics["total_tickets"]
        * 100,
        1,
    )

    return metrics


def calculate_priority_distribution(df):
    """Calculate ticket distribution by priority."""

    return (
        df["priority"]
        .value_counts()
        .reset_index()
        .rename(
            columns={
                "priority": "priority",
                "count": "ticket_count",
            }
        )
    )


def calculate_status_distribution(df):
    """Calculate ticket distribution by status."""

    return (
        df["status"]
        .value_counts()
        .reset_index()
        .rename(
            columns={
                "status": "status",
                "count": "ticket_count",
            }
        )
    )


if __name__ == "__main__":
    from data_processing import load_and_process_tickets

    tickets = load_and_process_tickets()

    metrics = calculate_metrics(tickets)

    print("\n" + "=" * 40)
    print("DELIVERY METRICS")
    print("=" * 40)

    for metric, value in metrics.items():
        print(
            f"{metric.replace('_', ' ').title()}: {value}"
        )

    print("\nPRIORITY DISTRIBUTION")
    print(calculate_priority_distribution(tickets))

    print("\nSTATUS DISTRIBUTION")
    print(calculate_status_distribution(tickets))
