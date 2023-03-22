**Atlas Bot**

Overview

This is a Telegram bot that provides information about the moon phase, moon rise and set times, as well as sunrise and sunset times for a given city. The bot responds to the command /moon followed by the name of a city.

The bot is currently in development and additional features related to weather and astronomy are planned.

Dependencies

    Python 3.7 or higher
    python-telegram-bot library
    requests library

Installation

    Clone or download the repository to your local machine.
    Install the required libraries by running the command pip install -r requirements.txt in the root directory of the project.
    Create a new bot on Telegram and obtain the API token.
    Add your Telegram API token into the main.py file.
    Run the bot (I suggest usign PyCharm to run the code).

Usage

To use the bot, start a chat with the bot on Telegram and type the command /moon followed by the name of a city. The bot will respond with the current moon phase, moon rise and set times, as well as sunrise and sunset times for the given city.
Implementation Details

The bot uses the python-telegram-bot library to interact with the Telegram API and receive commands from users. When a user sends the /moon command followed by a city name, the bot uses the requests library to query the OpenWeather API for the city and astronomical information. 

Future Plans

The bot is currently in development and additional features related to weather and astronomy are planned. The following features are currently being considered:

    Displaying current weather conditions for a given city.
    Providing astronomical information such as planet positions and meteor shower predictions.
    Providing personalized weather and astronomical alerts.
