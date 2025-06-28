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

## Requirements

- Python 3.8 or newer is reommended
- Gmail API credentials
- The following Python packages:
  - google-api-python-client
  - google-auth-httplib2
  - google-auth-oauthlib
  - pandas

## Setup Instructions

1. Clone the repo  
   git clone https://github.com/dami-nation/job-app-tracker.git
   cd job-app-tracker

2. Create and activate a virtual environment


On Mac/Linux:
   python3 -m venv venv
   source venv/bin/activate


On Windows:
   python -m venv venv
   venv\Scripts\activate

3. Install the required packages
   pip install -r requirements.txt

4. Set up Gmail API

- Go to the Google Cloud Console
- Create a new project (or use an existing one)
- Enable the Gmail API for the project
- Under “APIs & Services > Credentials”, create OAuth credentials
  - Application type: Desktop App
- Download the `credentials.json` file
- Place the file in the root of the project directory

5. Authenticate access

Run the script below. It will prompt you to log in and authorize access to your Gmail.
python gmail_auth.py

6. Run the main script
   python parse_and_log.py

The script will search your inbox and save matched results into `job_applications.csv`.

## Output

The CSV file will contain the following columns:

- Date
- Sender
- Subject
- Snippet (short preview of the email body)
- Message ID

## Files Ignored from Git

The following files are listed in `.gitignore` for privacy and security:

- credentials.json
- token.pickle
- job_applications.csv

## Future Plans

- EXpand the search to go beyond just "applications"
- Push results to Google Sheets
- Automate execution using cron or GitHub Actions
- Build a lightweight dashboard

## Purpose

This tool was built to help me automatically track job applications as part of a broader personal automation pipeline.
