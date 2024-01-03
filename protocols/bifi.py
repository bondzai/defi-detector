import os
from dotenv import load_dotenv
import requests
import pandas as pd
from pprint import pprint

load_dotenv()

url = os.getenv("BEEFY_API_URL")
address = os.getenv("BEEFY_ADDRESS")

params = {
    "address": address
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()

    df = pd.DataFrame(data)

    # Filter out End of life vaults
    df_filtered = df[df['is_eol'] == False] 

    pprint(df_filtered.to_dict(orient="records"))
else:
    print(f"Error: {response.status_code} - {response.text}")
