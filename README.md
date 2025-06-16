# Job Application Tracker

This is a Python automation tool that connects to your Gmail inbox, searches for job application confirmation emails, and logs the job details into a structured CSV file.

## What It Does

- Authenticates with Gmail securely using OAuth2
- Searches for emails with "application" in the subject after June 1, 2025
- Extracts:
  - Subject line
  - Sender email
  - Email date
- Logs each result into `job_applications.csv` locally

## Tech Stack

- Python
- Gmail API (via Google Cloud Console)
- Google OAuth2
- `google-api-python-client`, `pandas`, `csv`

## How to Run

1. Clone the repo  
   `git clone https://github.com/your-username/job-app-tracker.git`

2. Set up environment
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
Configure Gmail API

Set up a Google Cloud project

Enable Gmail API

Create OAuth credentials for Desktop

Download credentials.json into the project folder

Authenticate once

bash
Copy
Edit
python gmail_auth.py
Run the parser

bash
Copy
Edit
python parse_and_log.py
Ignored Files
credentials.json

token.pickle

job_applications.csv

These are added to .gitignore for security and privacy.

Next Steps
Filter by platform (LinkedIn, Indeed, etc.)

Push output to Google Sheets

Run automatically (cron or GitHub Actions)

Build a web dashboard

## Purpose

Built to track job applications and serve as the foundation for a full DevOps automation pipeline in my personal lab environment.
