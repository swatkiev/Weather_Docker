#pip install requests==2.28.2
#pip install python-telegram-bot==13.15
#python version 3.10 or higher (prefer 3.13 -> pip install standard-imghdr)
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import requests

# Замените на ваш токен
BOT_TOKEN = 'PUT HERE YOUR TOKEN FROM BOT_FATHER'
APPID = 'PUT HERE YOUR API KEY FROM openweathermap.org'

def start(update: Update, context: CallbackContext) -> None:
    """Отправляет приветственное сообщение и клавиатуру с запросом местоположения."""
    keyboard = [
        [KeyboardButton("Где я?", request_location=True)]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text('Привет! Нажми на кнопку, чтобы поделиться местоположением:', reply_markup=reply_markup)

def location(update: Update, context: CallbackContext) -> None:
    """Обрабатывает полученную геолокацию."""
    location = update.message.location
    latitude = location.latitude
    longitude = location.longitude

    try:
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units=metric&lat={latitude}&lon={longitude}&lang=ru&appid={APPID}")

    except:
        print("No internet access :(")

    response_json = response.json()
    temp = response_json["main"]["temp"]
    city = response_json["name"]
    descrip = response_json["weather"][0]["description"]
    temp2 = round(temp)
    update.message.reply_text(f'Погода в {city} - температура воздуха: {temp2}°C, {descrip}')

def main():
    """Запускает бота."""
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.location, location))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
