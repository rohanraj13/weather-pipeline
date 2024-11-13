from dotenv import load_dotenv
import os, requests, json

def get_current_weather(id):
    load_dotenv()
    lat = 41.825272
    long = -72.560059
    json_data = requests.get(
        f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={long}&appid="+os.environ.get("api-token")).json()
    
    print(f"Current weather data for {lat}, {long}")
    return json_data

def write_data(json_data):
    title = 'data' + str(json_data['dt'])
    filename = f"data_cache/{title}.json"
    with open(filename, 'w') as file:
        json.dump(json_data, file)

    return filename