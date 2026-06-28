import pandas as pd

def transform_cities(data):
    cities = data['result']['cities']
    cities_df = pd.DataFrame(cities)
    cities_df = cities_df.rename(columns={'lowername': 'cities'})
    return cities_df