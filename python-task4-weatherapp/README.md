# Task 4 - Basic Weather App

## Project Description

This project is a basic Python Weather App that fetches real-time weather information using the OpenWeatherMap API.

The user enters a city name, and the application displays the current weather details.

## Features

- Takes city name as input
- Fetches real-time weather data
- Displays temperature in Celsius
- Displays temperature in Fahrenheit
- Displays humidity percentage
- Displays weather condition
- Displays wind speed
- Handles empty city input
- Handles city not found errors
- Handles invalid API key errors
- Handles network errors
- Handles request timeout errors
- Allows the user to check another city

## Technologies Used

- Python
- Requests
- JSON
- OpenWeatherMap API

## Installation

Install the Requests library using:

pip install requests

## API Setup

This project uses the OpenWeatherMap API.

To use the application:

1. Create an account on OpenWeatherMap.
2. Generate an API key.
3. Add the API key to the Python program.
4. Run the application.

Example:

API_KEY = "YOUR_API_KEY"

Do not upload your real API key to GitHub.

## How to Run

1. Open the project in PyCharm.
2. Install the Requests library.
3. Add your OpenWeatherMap API key.
4. Open the Python file.
5. Run the program.
6. Enter a city name.
7. The current weather information will be displayed.

## Example

===== BASIC WEATHER APP =====

Enter city name: Karachi

----- WEATHER INFORMATION -----

City: Karachi

Temperature: 31.5 °C

Temperature: 88.7 °F

Humidity: 70%

Weather Condition: Partly Cloudy

Wind Speed: 4.2 m/s

Check another city? (y/n): n

## Error Handling

The application handles:

- Empty city input
- City not found
- Invalid API key
- Network connection errors
- Request timeout
- Other API request errors

