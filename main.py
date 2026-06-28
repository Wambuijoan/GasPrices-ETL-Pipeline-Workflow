from extract import extract_gas_prices
from transform import transform_cities
from load import get_engine, test_connection, load_cities

def main():
    data = extract_gas_prices()
    cities = transform_cities(data)
    load_cities(cities)

    print('ETL process completed successfully.')

if __name__ == "__main__":
    main()