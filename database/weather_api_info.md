# UVibe Project – Weather API Data Source

## API Provider
Open-Meteo Weather API

## API Endpoint
https://api.open-meteo.com/v1/forecast?latitude=-37.814&longitude=144.9633&daily=uv_index_max,uv_index_clear_sky_max&hourly=temperature_2m,relative_humidity_2m&current=temperature_2m,relative_humidity_2m&timezone=Australia%2FSydney

## Description
This API provides real-time and forecast weather data including UV Index, temperature, and humidity. The backend server will call this API to retrieve live environmental data for the UV safety application.

## Required Fields
The backend should extract the following fields from the API response:

- current.temperature_2m
- current.relative_humidity_2m
- daily.uv_index_max
- daily.time

## Example Output
Example values returned from the API:

Temperature: 16.8 °C  
Humidity: 55 %  
UV Index (daily max): 4.25

## Usage in the System
The backend service will call this API using the user's location (latitude and longitude). The retrieved UV index will be used to determine the UV risk level and generate sun protection recommendations for the user.

## Related Dataset
The location coordinates used for the API requests are provided in:

- melbourne_postcodes.csv