import requests
import telebot

api_key = 'WEATHER-API-KEY'

# Initialize the Telebot library
bot = telebot.TeleBot('YOUR-TELEGRAM-API-KEY')

@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.reply_to(message, "Hello, i'm Atlas! I'm a developing bot, the available commands in the moment are /weather and /astronomy \n"
                          "To use then just type the command + your #Country, Region, City")

@bot.message_handler(commands=['astronomy'])
def handle_moon_command(message):
    location = message.text.split('#')
    city = message.text.split(',')[2].title().strip()
    data = 'today'  # You can also use "tomorrow" or a specific date in "YYYY-MM-DD" format

    url = f'http://api.weatherapi.com/v1/astronomy.json?key={api_key}&q={location}&dt={data}'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()['astronomy']
        moon_phase = data['astro']['moon_phase']
        moonrise = data['astro']['moonrise']
        moonset = data['astro']['moonset']
        sunrise = data['astro']['sunrise']
        sunset = data['astro']['sunset']
        bot.reply_to(message, f'City:{city}\nThe current moon phase is {moon_phase}, moon rises at {moonrise} and sets at {moonset}.\n'
                              f'The sun rises at {sunrise} and sets at {sunset}.')
    else:
        bot.reply_to(message, 'Error getting moon information.')

# Define a new handler for the "/weather" command
@bot.message_handler(commands=['weather'])
def handle_weather_command(message):
    location = message.text.split('#')
    city = message.text.split(',')[2].title()
    data = 'today'  # You can also use "tomorrow" or a specific date in "YYYY-MM-DD" format

    url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}&aqi=no'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()['current']
        temp = data['temp_c']
        situation = data['condition']['text']
        feels = data['feelslike_c']
        emoji = data['condition']['icon']
        bot.reply_to(message, f'{city}\n{situation}\nThe current temperature is {temp}, feels like {feels}. \n')
    else:
        bot.reply_to(message, 'Error getting weather information.')

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")

# Start the bot
bot.polling()
