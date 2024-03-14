import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()
DEBUG = False

class DefiProtocol:


    def __init__(self, url, method='rest', **params):
        self.is_enable = True
        self.url = url
        self.method = method
        self.params = params

    def fetch_data(self):
        if self.method == 'rest':
            return self.fetch_data_rest()
        elif self.method == 'webscrape':
            return self.fetch_data_webscrape()
        else:
            print("Error: Unsupported method specified.")
            return None

    def fetch_data_rest(self):
        response = requests.get(self.url, params=self.params)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None

    def fetch_data_webscrape(self):
        response = requests.get(self.url, params=self.params)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            data = {}
            data['title'] = soup.title.text
            return data
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None

    def send_message(self, message, platforms):
        for platform in platforms:
            if platform == 'line':
                self.send_message_to_line(message)
            elif platform == 'telegram':
                self.send_message_to_telegram(message)
            elif platform == 'discord':
                self.send_message_to_discord(message)
            else:
                print(f"Error: Unsupported platform '{platform}' specified.")

    def send_message_to_line(self, message):
        url = os.getenv("LINE_NOTIFY_URL")
        token = os.getenv("LINE_NOTIFY_TOKEN")
        headers = {
            'content-type':'application/x-www-form-urlencoded',
            'Authorization':'Bearer '+ token
        }

        response = requests.post(url, headers=headers, data = {
            'message':message,
        })

        if DEBUG:
            print (response.text)
            print("Sending message to Line:", message)

    def send_message_to_telegram(self, message):
        token = os.getenv("TELEGRAM_BOT_TOKEN")
        chat_id = os.getenv("TELEGRAM_CHAT_ID")
        if token is None or chat_id is None:
            print("Error: Telegram bot token or chat ID not found in environment variables.")
            return

        url = f"https://api.telegram.org/bot{token}/sendMessage"
        payload = {
            "chat_id": chat_id,
            "text": message
        }

        try:
            response = requests.post(url, json=payload)
            if DEBUG:
                if response.status_code == 200:
                    print("Message sent to Telegram successfully.")
                else:
                    print(f"Failed to send message to Telegram. Status code: {response.status_code}")
        except Exception as e:
            print("An error occurred while sending message to Telegram:", str(e))

    def send_message_to_discord(self, message):
        url = os.getenv("DISCORD_WEBHOOK_URL")
        if url is None:
            print("Error: Discord webhook URL not found in environment variables.")
            return

        payload = {'content': message}
        headers = {'Content-Type': 'application/json'}

        try:
            response = requests.post(url, json=payload, headers=headers)
            if DEBUG:
                if response.status_code == 204:
                    print("Message sent to Discord successfully.")
                else:
                    print(f"Failed to send message to Discord. Status code: {response.status_code}")
        except Exception as e:
            print("An error occurred while sending message to Discord:", str(e))
