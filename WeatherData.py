import requests


# This class represents weather data for a specific location and date.
# It includes attributes of latitude, longitude, data, and several weather metrics.
# The attributes contain the calculations required to meet the needs of mean, max, min, & sum.
class WeatherData:
    def __init__(self):
        self.location_latitude = 39.1142
        self.location_longitude = -94.6275
        self.month = 7
        self.day_of_month = 13
        self.year = 2023
        self.five_year_mean_temperature = round(sum(self.get_mean_temperature()) / len(self.get_mean_temperature()), 1)
        self.five_year_min_temperature = min(self.get_mean_temperature())
        self.five_year_max_temperature = max(self.get_mean_temperature())
        self.five_year_avg_wind_speed = round(sum(self.max_wind_speed()) / len(self.max_wind_speed()), 1)
        self.five_year_min_wind_speed = min(self.max_wind_speed())
        self.five_year_max_wind_speed = max(self.max_wind_speed())
        self.five_year_sum_precipitation = sum(self.precipitation_sum())
        self.five_year_min_precipitation = min(self.precipitation_sum())
        self.five_year_max_precipitation = max(self.precipitation_sum())

# Method that retrieves the mean temp at specific location and dates.
    def get_mean_temperature(self):
        url = ("https://archive-api.open-meteo.com/v1/archive?latitude=39.1142&longitude=-94.6275&"
               "start_date=2019-07-13,2020-07-13,2021-07-13,2022-07-13,2023-07-13&"
               "end_date=2019-07-13,2020-07-13,2021-07-13,2022-07-13,2023-07-13&"
               "daily=temperature_2m_mean&temperature_unit=fahrenheit&wind_speed_unit=mph&"
               "precipitation_unit=inch&timezone=America%2FChicago")

        response = requests.get(url).json()

        mean_temp = [item['daily']['temperature_2m_mean'][0] for item in response]
        return mean_temp

# Method that retrieves the max wind speed at specific location and dates.
    def max_wind_speed(self):
        url = ("https://archive-api.open-meteo.com/v1/archive?latitude=39.1142&longitude=-94.6275&"
               "start_date=2019-07-13,2020-07-13,2021-07-13,2022-07-13,2023-07-13&"
               "end_date=2019-07-13,2020-07-13,2021-07-13,2022-07-13,2023-07-13&"
               "daily=wind_speed_10m_max&temperature_unit=fahrenheit&wind_speed_unit=mph&"
               "precipitation_unit=inch&timezone=America%2FChicago")

        response = requests.get(url).json()

        max_wind = [item['daily']['wind_speed_10m_max'][0] for item in response]
        return max_wind

# Method that retrieves the precipitation sum at specific location and dates.
    def precipitation_sum(self):
        url = ("https://archive-api.open-meteo.com/v1/archive?latitude=39.1142&longitude=-94.6275&"
               "start_date=2019-07-13,2020-07-13,2021-07-13,2022-07-13,2023-07-13&"
               "end_date=2019-07-13,2020-07-13,2021-07-13,2022-07-13,2023-07-13&"
               "daily=precipitation_sum&temperature_unit=fahrenheit&wind_speed_unit=mph&"
               "precipitation_unit=inch&timezone=America%2FChicago")

        response = requests.get(url).json()

        pre_sum = [item['daily']['precipitation_sum'][0] for item in response]
        return pre_sum
