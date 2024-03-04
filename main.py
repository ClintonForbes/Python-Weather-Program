from WeatherData import WeatherData

from sqlalchemy import create_engine, Column, Integer, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# This is the instance of the class from step 1
weather_instance = WeatherData()

# These are the instances calling the methods
# print(weather_instance.get_mean_temperature())
# print(weather_instance.max_wind_speed())
# print(weather_instance.precipitation_sum())

# Setting up base class
Base = declarative_base()


# Creating my class here where my data will be stored into the table
class WeatherTable(Base):
    __tablename__ = 'weather_data_table'

    id = Column("id", Integer, primary_key=True)
    location_latitude = Column("latitude", Float)
    location_longitude = Column("longitude", Float)
    month = Column("month", Integer)
    day_of_month = Column("day", Integer)
    year = Column("year", Integer)
    five_year_mean_temperature = Column("mean_temperature", Float)
    five_year_min_temperature = Column("min_temperature", Float)
    five_year_max_temperature = Column("max_temperature", Float)
    five_year_avg_wind_speed = Column("avg_wind_speed", Float)
    five_year_min_wind_speed = Column("min_wind_speed", Float)
    five_year_max_wind_speed = Column("max_wind_speed", Float)
    five_year_sum_precipitation = Column("sum_precipitation", Float)
    five_year_min_precipitation = Column("min_precipitation", Float)
    five_year_max_precipitation = Column("max_precipitation", Float)


# Created an engine that actually makes the table when ran.
engine = create_engine('sqlite:///weather_data.db')
Base.metadata.create_all(engine)

# Created an instance for my table.
# Combined my table instance with my WeatherData instance to populate the data into the table.
weather_table_instance = WeatherTable(
    location_latitude=weather_instance.location_latitude,
    location_longitude=weather_instance.location_longitude,
    month=weather_instance.month,
    day_of_month=weather_instance.day_of_month,
    year=weather_instance.year,
    five_year_mean_temperature=weather_instance.five_year_mean_temperature,
    five_year_min_temperature=weather_instance.five_year_min_temperature,
    five_year_max_temperature=weather_instance.five_year_max_temperature,
    five_year_avg_wind_speed=weather_instance.five_year_avg_wind_speed,
    five_year_min_wind_speed=weather_instance.five_year_min_wind_speed,
    five_year_max_wind_speed=weather_instance.five_year_max_wind_speed,
    five_year_sum_precipitation=weather_instance.five_year_sum_precipitation,
    five_year_min_precipitation=weather_instance.five_year_min_precipitation,
    five_year_max_precipitation=weather_instance.five_year_max_precipitation)


Session = sessionmaker(bind=engine)
session = Session()
# Started a session, this command calls the instance to populate the data into the table
# session.add(weather_table_instance)
# session.commit()


# This method queries the WeatherTable and prints out the stored data
def print_all_weather_data(session):
    weather_data = session.query(WeatherTable).all()

    for data in weather_data:
        print(f"id: {data.id}")
        print(f"latitude: {data.location_latitude}")
        print(f"longitude: {data.location_longitude}")
        print(f"month: {data.month}")
        print(f"day: {data.day_of_month}")
        print(f"year: {data.year}")
        print(f"mean_temperature: {data.five_year_mean_temperature}")
        print(f"min_temperature: {data.five_year_min_temperature}")
        print(f"max_temperature: {data.five_year_max_temperature}")
        print(f"avg_wind Speed: {data.five_year_avg_wind_speed}")
        print(f"min_wind Speed: {data.five_year_min_wind_speed}")
        print(f"max_wind Speed: {data.five_year_max_wind_speed}")
        print(f"sum_precipitation: {data.five_year_sum_precipitation}")
        print(f"min_precipitation: {data.five_year_min_precipitation}")
        print(f"max_precipitation: {data.five_year_max_precipitation}")
        print("\n")


print_all_weather_data(session)
