# Job Application Tracker (AutoTrack)

This is a Python-based automation tool that connects to your Gmail inbox, searches for job application confirmation emails, and logs the job details into a structured CSV file.

## Features

- Gmail API integration
- Extracts job title, company, platform, and date applied
- Logs results into a local CSV (Google Sheets version coming soon)
- Designed to scale into a full DevOps pipeline later

## Technologies Used

- Python
- Gmail API
- Pandas
- Google Auth Libraries

## How to Run

1. Clone this repo
2. Install dependencies: `pip install -r requirements.txt`
3. Set up Gmail API and get your `credentials.json`
4. Run the script to authenticate and start logging applications

## Coming Soon

- Google Sheets integration
- Web dashboard using Streamlit
- CI/CD with GitHub Actions
- Docker container support

## Purpose

I built this as part of my DevOps learning journey. It's a practical automation tool that also serves as a hands-on portfolio project.

An automated script that logs job application confirmation emails to CSV or Google Sheets
