# importing 'unittest' allows me to test my code.
import unittest
from WeatherData import WeatherData


# This class is testing three different calculations in my code. Mean Temp, Max Wind Speed, & Precipitation Sum


class TestWeatherData(unittest.TestCase):
    def setUp(self):
        # Creating an instance so I can use for testing.
        self.test_weather = WeatherData()

    def test_mean_temperature_calculation(self):
        # Testing the mean temperature calculation
        mean_temperature = self.test_weather.five_year_mean_temperature

        expected_mean_temperature = 79.2

        self.assertEqual(mean_temperature, expected_mean_temperature,
                         "Mean temperature calculation is incorrect.")

    def test_max_wind_speed_calculation(self):
        # Testing the max wind speed calculation
        max_wind_speed = self.test_weather.five_year_max_wind_speed

        expected_max_wind_speed = 9.8

        self.assertEqual(max_wind_speed, expected_max_wind_speed,
                         "Max wind speed calculation is incorrect.")

    def test_precipitation_sum_calculation(self):
        # Testing the precipitation sum calculation
        precipitation_sum = self.test_weather.five_year_sum_precipitation

        expected_precipitation_sum = 0.059

        self.assertEqual(precipitation_sum, expected_precipitation_sum,
                         "Precipitation sum calculation is incorrect.")


if __name__ == '__main__':
    unittest.main()
