# Atlas Bot

#### Overview

This is a Telegram bot that provides information about current weather (temperature, feels like and condition) and astronomical information about the moon phase, moon rise and moonset, as well as sunrise and sunset.
The bot is currently in development and additional features related to forecast and astronomy are planned.

#### Dependencies

    Python 3.7 or higher
    python-telegram-bot library
    requests library

#### Installation

    Clone or download the repository to your local machine.
    Install the required libraries by running the command pip install -r requirements.txt in the root directory of the project.
    Create a new bot on Telegram and obtain the API token.
    Create an account on WeatherAPI.com and obtain the API token.
    Add your Telegram API token and weatherAPI token into the main.py file.
    Run the bot (I suggest usign PyCharm to run the code).

#### Usage

To use the bot, start a chat with the bot on Telegram and type the command /start. The bot will respond with the possible commands you can use. 
The current sintax for weather and astronomy are: 

	/weather #country,region,city
	
#### Implementation Details

The bot uses the python-telegram-bot library to interact with the Telegram API and receive commands from users. When a user sends the /weather or /astronomy command followed by location, the bot uses the requests library to query the OpenWeather API for the exact location and requested information.

#### Future Plans

The bot is currently in development and additional features related to weather and astronomy are planned. The following features are currently being considered:

    Improvements related to using commands.
    Providing astronomical information such as planet positions and meteor shower predictions.
    Providing forecast and weather alerts.
