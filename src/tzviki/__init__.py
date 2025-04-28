from .app import Tzviki
import os
from dotenv import load_dotenv

load_dotenv()
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
from_number = os.getenv("FROM_NUMBER")
to_number = os.getenv("TO_NUMBER")

def main() -> None:
    tzviki = Tzviki(account_sid, auth_token, from_number, to_number)
    tzviki.send_background()
