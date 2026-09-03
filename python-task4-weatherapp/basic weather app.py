#Iman Mirza
#Python Programming
#Task 3 - weather app

import requests
import json

# Your OpenWeatherMap API key
API_KEY = "3f8b008cf28c352fb371b4bc6766ac35"

while True:
    print("\n===== BASIC WEATHER APP =====")

    # Ask user for city
    city = input("Enter city name: ").strip()

    # Validate empty input
    if city == "":
        print("City name cannot be empty!")
        continue

    # OpenWeatherMap API URL
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        # API request
        response = requests.get(url, params=params, timeout=10)

        # Check errors
        if response.status_code == 404:
            print("City not found. Please enter a valid city.")
            continue

        elif response.status_code == 401:
            print("Invalid API key. Please check your API key.")
            break

        response.raise_for_status()

        # Convert response to JSON
        data = response.json()

        # Get weather information
        temperature_c = data["main"]["temp"]
        temperature_f = (temperature_c * 9/5) + 32
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]

        # Display weather
        print("\n----- WEATHER INFORMATION -----")
        print("City:", data["name"])
        print(f"Temperature: {temperature_c:.1f} °C")
        print(f"Temperature: {temperature_f:.1f} °F")
        print(f"Humidity: {humidity}%")
        print("Weather Condition:", condition.title())
        print(f"Wind Speed: {wind_speed} m/s")

    except requests.exceptions.Timeout:
        print("Request timed out. Please try again.")

    except requests.exceptions.ConnectionError:
        print("Network error. Please check your internet connection.")

    except requests.exceptions.RequestException:
        print("Something went wrong while getting weather data.")

    # Ask whether user wants another search
    again = input("\nCheck another city? (y/n): ").lower()

    if again != "y":
        print("Thank you for using the Weather App!")
        break