import pandas as pd
import json

def convert_json_to_dictionary(filename):
    with open(filename, 'r') as json_file:
        json_dict = json.load(json_file)

    return json_dict

def convert_to_df(filename):
    df = pd.json_normalize(convert_json_to_dictionary(filename))
    return df

if __name__ == "__main__":
    import doctest
    doctest.testmod()