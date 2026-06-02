import requests

API_KEY = "cc9685fed045ee02cf1f64cbbc0d027e"  # Replace with your OpenWeatherMap API key


def get_weather(city):
    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200:
            print("\nCity not found!")
            return

        city_name = data["name"]
        country = data["sys"]["country"]
        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        weather = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]

        print("\n===== WEATHER REPORT =====")
        print(f"City       : {city_name}, {country}")
        print(f"Temperature: {temperature}°C")
        print(f"Feels Like : {feels_like}°C")
        print(f"Humidity   : {humidity}%")
        print(f"Weather    : {weather.title()}")
        print(f"Wind Speed : {wind_speed} m/s")
        print("==========================")

    except Exception as e:
        print("Error:", e)


def main():
    print("===== Weather App =====")

    while True:
        city = input("\nEnter city name: ")

        if city.lower() == "exit":
            print("Goodbye!")
            break

        get_weather(city)


if __name__ == "__main__":
    main()
