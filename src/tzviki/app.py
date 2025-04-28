import requests
from twilio.rest import Client
import random
BACKGROUNDS_URL="https://raw.githubusercontent.com/dconnolly/chromecast-backgrounds/refs/heads/master/backgrounds.json"


class Tzviki:
    def __init__(self, account_sid, auth_token, from_number, to_number):
        self.client = Client(account_sid, auth_token)
        self.backgrounds = requests.get(BACKGROUNDS_URL).json()
        self.from_number = from_number
        self.to_number = to_number

    def send_background(self):
        background = random.choice(self.backgrounds)
        message = self.client.messages.create(
            from_=self.from_number,
            to=self.to_number,
            body=f"*התמונה היומית:*\nיוצר: {background.get('author')}",
            media_url=background["url"],
        )
        return message.sid
