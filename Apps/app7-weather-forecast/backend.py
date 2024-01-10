import requests

API_KEY = '85d4473c86d7a3f25058ce9afe0cf0a3'
# city_ID = "London"
# url = f"http://api.openweathermap.org/data/2.5/forecast?id={city_ID}&appid={api_key}"
# response = requests.get(url)
# print(response.json())

def get_data(place, forecast_days = 2, kind = "Sky"):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    if kind == "Temperature":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]
    if kind == "Sky":
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
    return filtered_data

if __name__ == "__main__":
    print(get_data(place = "Tokyo"))
