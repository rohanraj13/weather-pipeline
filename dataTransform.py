def keep_columns(df):
    return df[[
        'main.temp','main.temp_min','main.temp_max','main.pressure','main.humidity','wind.speed','wind.deg','dt','name'
        ]]

def change_col_name(pandas_df_kept_columns):
    return pandas_df_kept_columns.rename(columns={
        'main.temp': 'temp', 'main.temp_min': 'temp_min', 'main.temp_max': 'temp_max', 'main.pressure': 'pressure', 
        'main.humidity': 'humidity', 'wind.speed': 'wind_speed', 'wind.deg': 'wind_deg'
        })


def convert_kelvin_to_celsius(pandas_df_kept_renamed_columns):
    columns = ["temp", "temp_min", "temp_max"]
    for column in columns:
        pandas_df_kept_renamed_columns[column] = pandas_df_kept_renamed_columns[column] - 273.15
    return pandas_df_kept_renamed_columns


def set_datetime_col_as_row_index(pandas_df_kept_renamed_columns_in_celsius):
    return pandas_df_kept_renamed_columns_in_celsius.set_index('dt')


if __name__ == "__main__":
    import doctest
    doctest.testmod()