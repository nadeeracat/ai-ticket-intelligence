import os
from openai import OpenAI


def generate_ai_analysis(metrics, risks):
    """Generate AI-powered delivery insights."""

    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY")
    )

    risk_summary = {}

    for risk_type, tickets in risks.items():
        risk_summary[risk_type] = {
            "count": len(tickets),
            "tickets": tickets[
                ["ticket_id", "title", "priority", "status"]
            ].to_dict(orient="records"),
        }

    prompt = f"""
You are an AI delivery intelligence assistant.

Analyze the following project metrics and risks.

Metrics:
{metrics}

Risks:
{risk_summary}

Provide:

1. Sprint Health Summary
2. Top 3 Delivery Risks
3. Business Impact
4. Recommended Actions

Be concise, specific and actionable.
Do not invent information that is not present in the data.
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        temperature=0.3,
    )

    return response.choices[0].message.content
