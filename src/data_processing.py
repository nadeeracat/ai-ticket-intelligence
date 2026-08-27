import pandas as pd
from pathlib import Path


def load_and_process_tickets():
    """Load and prepare ticket data for analysis."""

    project_root = Path(__file__).resolve().parent.parent
    data_path = project_root / "data" / "sample_tickets.csv"

    # Load data
    df = pd.read_csv(data_path)

    # Convert date columns
    df["created_date"] = pd.to_datetime(df["created_date"])
    df["due_date"] = pd.to_datetime(df["due_date"])

    # Clean text columns
    df["assignee"] = df["assignee"].fillna("")
    df["acceptance_criteria"] = df["acceptance_criteria"].fillna("")

    # Create analytical features
    today = pd.Timestamp.today().normalize()

    df["is_overdue"] = (
        (df["due_date"] < today)
        & (~df["status"].isin(["Done"]))
    )

    df["has_assignee"] = df["assignee"].str.strip() != ""
    df["has_acceptance_criteria"] = (
        df["acceptance_criteria"].str.strip() != ""
    )

    return df


if __name__ == "__main__":
    tickets = load_and_process_tickets()

    print("Tickets loaded successfully!")
    print(f"Total tickets: {len(tickets)}")
    print("\nProcessed data:")
    print(
        tickets[
            [
                "ticket_id",
                "status",
                "priority",
                "is_overdue",
                "has_assignee",
                "has_acceptance_criteria",
            ]
        ].to_string(index=False)
    )
