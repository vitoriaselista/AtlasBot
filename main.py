import requests
import telebot

api_key = 'API-KEY-HERE'

# Initialize the Telebot library
bot = telebot.TeleBot('YOUR-TELEGRAMBOT-KEY-HERE')

# Define a new handler for the "/moon" command
@bot.message_handler(commands=['moon'])
def handle_moon_command(message):
    cidade = message.text.split(' ')[1].title()
    data = 'today'  # You can also use "tomorrow" or a specific date in "YYYY-MM-DD" format

    url = f'http://api.weatherapi.com/v1/astronomy.json?key={api_key}&q={cidade}&dt={data}'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()['astronomy']
        moon_phase = data['astro']['moon_phase']
        moonrise = data['astro']['moonrise']
        moonset = data['astro']['moonset']
        sunrise = data['astro']['sunrise']
        sunset = data['astro']['sunset']
        bot.reply_to(message, f'City: {cidade}\nThe current moon phase is {moon_phase}, moon rises at {moonrise} and sets at {moonset}. \n'
                              f'The sun rises at {sunrise} and sets at {sunset}.')
    else:
        bot.reply_to(message, 'Error getting moon information.')


# Start the bot
bot.polling()
