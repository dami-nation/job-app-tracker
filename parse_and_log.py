import base64
import csv
import os
from googleapiclient.discovery import build
from gmail_auth import authenticate_gmail
from datetime import datetime

def get_job_emails(service):
    query = 'subject:application after:2025/06/01'
    results = service.users().messages().list(userId='me', q=query, maxResults=10).execute()
    messages = results.get('messages', [])
    return messages

def get_email_details(service, msg_id):
    msg = service.users().messages().get(userId='me', id=msg_id, format='metadata', metadataHeaders=['Subject', 'From', 'Date']).execute()
    headers = msg['payload']['headers']
    subject = next((h['value'] for h in headers if h['name'] == 'Subject'), 'N/A')
    sender = next((h['value'] for h in headers if h['name'] == 'From'), 'N/A')
    date = next((h['value'] for h in headers if h['name'] == 'Date'), 'N/A')
    return subject, sender, date

def log_to_csv(data, filename='job_applications.csv'):
    file_exists = os.path.isfile(filename)
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['Date Retrieved', 'Subject', 'From', 'Email Date'])
        for row in data:
            writer.writerow([datetime.now().isoformat()] + list(row))

def main():
    creds = authenticate_gmail()
    service = build('gmail', 'v1', credentials=creds)

    messages = get_job_emails(service)
    if not messages:
        print("No job application emails found.")
        return

    all_data = []
    for msg in messages:
        subject, sender, date = get_email_details(service, msg['id'])
        all_data.append((subject, sender, date))

    log_to_csv(all_data)
    print(f"{len(all_data)} entries added to job_applications.csv")

if __name__ == '__main__':
    main()

