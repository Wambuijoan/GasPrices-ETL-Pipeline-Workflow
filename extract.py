import os
import json
import http.client
from dotenv import load_dotenv

load_dotenv()

def extract_gas_prices():
    conn = http.client.HTTPSConnection("api.collectapi.com")
    api_token = os.getenv("API_TOKEN")

    headers = {
        'content-type': "application/json",
        'authorization': f"apikey {api_token}"
    }

    conn.request("GET", "/gasPrice/stateUsaPrice?state=WA", headers=headers)
    res = conn.getresponse()
    raw_data = res.read()

    data = json.loads(raw_data.decode("utf-8"))
    return data