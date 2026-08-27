# AI Ticket Intelligence

An AI-powered analytics application that analyzes project ticket data to identify delivery risks, generate insights, and support data-driven decision-making.

## Business Problem

Project teams often work with large volumes of ticket data. Identifying overdue work, blockers, unclear requirements, and delivery risks manually can be time-consuming.

This project demonstrates how data analytics and Large Language Models can be combined to transform raw project data into actionable business insights.

## Solution

AI Ticket Intelligence processes ticket data and provides:

- Delivery risk detection
- Overdue ticket analysis
- Blocked work identification
- Unassigned ticket detection
- Acceptance criteria validation
- Delivery metrics and analytics
- Interactive dashboard
- AI-generated delivery insights and recommendations

## Architecture

```text
CSV Ticket Data
       ↓
Data Processing
       ↓
Feature Engineering
       ↓
Rule-Based Risk Detection
       ↓
Analytics & Metrics
       ↓
OpenAI LLM Analysis
       ↓
Business Recommendations
       ↓
Streamlit Dashboard

Key Features
Data Processing

The application cleans and processes ticket data, including:

Date conversion
Missing value handling
Overdue ticket detection
Assignment validation
Acceptance criteria validation
Delivery Risk Detection

The system identifies:

High-priority overdue tickets
Critical overdue tickets
Blocked tickets
Unassigned tickets
Tickets without acceptance criteria
Analytics

The dashboard provides:

Total ticket count
Completion rate
Overdue ticket count
Blocked ticket count
Priority distribution
Status distribution
AI-Powered Analysis

The application uses OpenAI to generate:

Sprint health summaries
Key delivery risks
Business impact analysis
Recommended actions
Technology Stack
Python
Pandas
OpenAI API
Streamlit
Plotly
Project Structure

ai-ticket-intelligence/
│
├── app/
│   └── app.py
│
├── data/
│   └── sample_tickets.csv
│
├── notebooks/
│   └── exploratory_analysis.ipynb
│
├── screenshots/
│
├── src/
│   ├── analytics.py
│   ├── data_processing.py
│   ├── llm_analysis.py
│   └── rule_based_analysis.py
│
├── tests/
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md

Installation

Clone the repository:
git clone https://github.com/nadeeracat/ai-ticket-intelligence.git
cd ai-ticket-intelligence

Install dependencies:
python3 -m pip install -r requirements.txt

Create an environment file:
cp .env.example .env

Add your OpenAI API key:
OPENAI_API_KEY=your_api_key_here

Run the Application
python3 -m streamlit run app/app.py

Open the application:
http://localhost:8501

Future Improvements
Azure DevOps API integration
Real-time ticket data ingestion
Advanced ML-based risk prediction
Historical trend analysis
Multi-team analytics
Deployment to the cloud
Disclaimer

This project uses synthetic ticket data and does not contain confidential business information.



