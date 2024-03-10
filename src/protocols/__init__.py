import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()


class DefiProtocol:
    def __init__(self, url, method='rest', **params):
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
            else:
                print(f"Error: Unsupported platform '{platform}' specified.")

    def send_message_to_line(self, message):
        url = 'https://notify-api.line.me/api/notify'
        token = os.getenv("LINE_TOKEN")
        headers = {
            'content-type':'application/x-www-form-urlencoded',
            'Authorization':'Bearer '+ token
        }

        r = requests.post(url, headers=headers, data = {
            'message':message,
        })

        print (r.text)
        print("Sending message to Line:", message)

    def send_message_to_telegram(self, message):
        print("Sending message to Telegram:", message)
