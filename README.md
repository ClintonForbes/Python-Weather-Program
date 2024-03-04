# Python-Weather-Program

Weather Data Program

This Python Program analyzes weather data for a specific location and date
range using the Open-Meteo API. The program runs with both 'WeatherData.py'
and 'main.py'. The WeatherData.py file holds the main class as well as three
methods that retrieve the data. The main.py file calls the methods from the instance.
It also has the class that makes up the SQLite database. Since this is on Pycharm Community
Edition, no installing is required, but you will need to import sqlalchemy and requests.

The program takes predefined inputs for the location and date:

Location:
    Latitude: 39.1142
    Longitude: -94.6275
Date:
    Month: 7
    Day of Month: 13
    Year: 2023

These three commands will fetch the corresponding data
    Get Mean Temperature
    Max Wind Speed
    Precipitation Sum

These are retrieved from the weather data site. Once gathered the following
weather metrics are calculated.
    Five-Year Mean Temperature
    Five-Year Minimum Temperature
    Five-Year Maximum Temperature
    Five-Year Average Wind Speed
    Five-Year Minimum Wind Speed
    Five-Year Maximum Wind Speed
    Five-Year Total Precipitation
    Five-Year Minimum Precipitation
    Five-Year Maximum Precipitation


A second class and a database is created that will be used to store the data.
The database will be created with this command:

    "engine = create_engine('sqlite:///weather_data.db')"
    "Base.metadata.create_all(engine)"

These metrics are then stored in the SQLite table by the instance of the table combined with
the instance of the first class. The session maker command is used to populate the table:

    "Session = sessionmaker(bind=engine)"
    "session = Session()"
    "session.add(weather_table_instance)"
    "session.commit()"

The program will also print and display the data outputs to the console.

Sources that were used:

  Zippenfenig, P. (2023). Open-Meteo.com Weather API [Computer software].
  Zenodo. https://doi.org/10.5281/ZENODO.7970649



