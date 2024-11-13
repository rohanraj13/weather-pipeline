from dbHandler import create_connection, close_connection
from createDataFrame import convert_to_df
from updateDatabase import update_database
from dataTransform import keep_columns, change_col_name, convert_kelvin_to_celsius, set_datetime_col_as_row_index
from getWeather import get_current_weather, write_data
import argparse
import time

parser = argparse.ArgumentParser()
parser.add_argument("--city_id", default="4843353", help="Fetch weather data for a specified city. Find the id of the city on OpenWeatherMap.org")
parser.add_argument("--frequency", default=900, type=int, help="How often does the program run in seconds")
args = parser.parse_args()
if args.city_id:
    print("city id inserted")
if args.city_id:
    print("program frequency inserted")


def start():
    returned_connection = create_connection()
    filename = write_data(
        get_current_weather(args.city_id))
    new_df_to_sql = set_datetime_col_as_row_index(convert_kelvin_to_celsius(
        change_col_name(keep_columns(convert_to_df(filename)))))

    update_database(new_df_to_sql, returned_connection)

    close_connection(returned_connection)


while True:
    start()
    time.sleep(args.frequency)
