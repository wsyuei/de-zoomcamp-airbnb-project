if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):

    #    price is not null and greater than 0 
    data = data[data['price'] > 0]

    #   convert datetime to date
    data['last_review_date'] = data['last_review'].dt.date

    #   convert datetime to date
    data['last_review'] = data['last_review'].dt.date

    #   remove duplicated rows
    data = data.drop_duplicates()

    #   remove blank column
    data = data.drop('neighbourhood_group', axis=1) 

    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
