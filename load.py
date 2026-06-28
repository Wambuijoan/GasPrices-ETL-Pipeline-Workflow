import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()

def get_engine():
    DATABASE_NAME = os.getenv('DATABASE_NAME')
    DATABASE_USER = os.getenv('DATABASE_USER')
    DATABASE_PORT = os.getenv('DATABASE_PORT')
    DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
    DATABASE_HOST = os.getenv('DATABASE_HOST')

    return create_engine(
        f'postgresql+psycopg2://{DATABASE_USER}:{DATABASE_PASSWORD}'
        f'@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}'
    )

def test_connection(engine):
    with engine.connect() as conn:
        result = conn.execute(text('select 1;'))
        for row in result:
            print(row)

def load_cities(cities_df, engine):
    cities_df.to_sql('cities', engine, if_exists='replace', index=False)