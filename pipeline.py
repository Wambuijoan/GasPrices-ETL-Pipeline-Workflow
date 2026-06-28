import os
import json
import http.client
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine , text

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
    data = res.read()

    data = json.loads(data.decode("utf-8"))
    return data


def transform_cities(data):
    cities = data['result']['cities']
    cities = pd.DataFrame(cities)
    cities = cities.rename(columns = {'lowername':'cities'})
    return cities


def load_cities(cities):
    DATABASE_NAME = os.getenv('DATABASE_NAME')
    DATABASE_USER = os.getenv('DATABASE_USER')
    DATABASE_PORT = os.getenv('DATABASE_PORT')
    DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
    DATABASE_HOST = os.getenv('DATABASE_HOST')

    engine = create_engine(f'postgresql+psycopg2://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}')

    with engine.connect() as conn:
        resort = conn.execute(text('select 1;'))
        for i in resort:
            print(i)

    cities.to_sql('cities',engine , if_exists='replace',index=False )


def main():
    data = extract_gas_prices()
    cities = transform_cities(data)
    load_cities(cities)

    print('ETL process completed successfully.')

if __name__ == "__main__":
    main()
