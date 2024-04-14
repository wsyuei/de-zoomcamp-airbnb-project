from mage_ai.io.file import FileIO
import pandas as pd

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_file(*args, **kwargs):

    airbnb_dtypes = {
        'id': 'Int64',
        'name': 'str',
        'host_id': 'Int64',
        'host_name': 'str',
        'neighbourhood_group': 'str',
        'neighbourhood': 'str',
        'latitude': 'float64',
        'longitude': 'float64',
        'room_type': 'str',
        'price': 'float64',
        'minimum_nights': 'Int64',
        'number_of_reviews': 'Int64',
        'reviews_per_month': 'float64',
        'calculated_host_listings_count': 'Int64',
        'availability_365': 'Int64',
        'number_of_reviews_ltm': 'Int64',
        'license': 'str'
    }

    parse_dates = ['last_review']

    filepath = './Dataset/listings.csv'
    
    data = pd.read_csv(filepath, sep=",", dtype = airbnb_dtypes, parse_dates = parse_dates)

    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
