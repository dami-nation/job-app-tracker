import os.path
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def authenticate_gmail():
    print("Starting Gmail authentication...")

    creds = None

    if os.path.exists('token.pickle'):
        print("Found existing token. Loading...")
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    else:
        print("No existing token found.")

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            print("Refreshing expired token...")
            creds.refresh(Request())
        else:
            print("Starting OAuth flow...")
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
            print("OAuth flow complete.")

        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
            print("Saved new token to token.pickle")

    print("Authentication complete.")
    return creds
if __name__ == '__main__':
    authenticate_gmail()

