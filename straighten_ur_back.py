import os
import logging
import requests
import random
import time
import schedule
import sys

from telegram.ext import CommandHandler, MessageHandler, Filters, Updater

from telegram import ReplyKeyboardMarkup

from dotenv import load_dotenv


URL = 'https://api.thecatapi.com/v1/images/search'
NEW_URL = 'https://api.thedogapi.com/v1/images/search'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RETRY_TIME = 150
ZERO = 0


load_dotenv()
secret_token = os.getenv('TOKEN')
updater = Updater(token=secret_token)


def get_new_image():
    """Данная функция, с помощью API, получает фото котиков или собак"""
    try:
        response = requests.get(URL)
    except Exception as error:
        logging.error(f'Ошибка при запросе к основному API: {error}')
        response = requests.get(NEW_URL)

    response = response.json()
    random_cat = response[ZERO].get('url')
    return random_cat


def straighten_ur_back(update, context):
    """Данная функция отсылает сообщение в телеграм бота."""
    chat = update.effective_chat
    name = update.message.chat.first_name
    button = ReplyKeyboardMarkup([
        ['/my_contacts'],
        ['/time_setting'],
        ['/newcat'],
        ],
        resize_keyboard=True)
    context.bot.send_message(
        chat_id=chat.id,
        text='Привет, {}. Выпрями спину и посмотри '
        'какого котика я тебе нашел'.format(name),
        reply_markup=button
    )
    context.bot.send_photo(chat.id, get_new_image())


def new_cat(update, context):
    """Данная функция отправляет котиков или собак в телеграм-чат (new_cat)"""
    chat = update.effective_chat
    context.bot.send_photo(chat.id, get_new_image())


def straighten_ur_back_random(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    list = [
        'Выпрями спину',
        f'Выпрями спину {name}',
        'Сейчас же выпрями свою спину',
        'Повторяю в последний раз, выпрями спину',
        'Спину выпрями',
        f'VIPRYUAMI SPINU {name.upper()}',
        f'{name} ВЫПРЯМИ СПИНУ',
        'Спину',
        'Выпрямись',
        'Выпрями свою спину',
        'Да выпрями свою спину наконец!',
        '"Выпрями спину" на англисйком будет "Straighten your back"',
        'Straighten ur back',
        'В Ы П Р Я М И С П И Н У',
        f'{name}, спина не болит?'
    ]
    random_index = random.choice(list)
    context.bot.send_message(
        chat_id=chat.id,
        text=random_index,
    )


def my_contacts(update, context):
    chat = update.effective_chat

    context.bot.send_message(
        chat_id=chat.id,
        text='Мой телеграм: @maidaritsydenov\nМоя почта: tmaidari@mail.ru',
    )


def straighten_ur_back_timer(update, context):
    chat = update.effective_chat
    buttons = ReplyKeyboardMarkup([
        ['/1'],
        ['/2'],
        ['/3'],
        ['/4'],
        ],
        resize_keyboard=True)
    context.bot.send_message(
        chat_id=chat.id,
        text='1. Напоминать 2 раза в день в 10:00 и 15:00\n'
        '2. Напоминать 3 раза в день в 10:00, 14:00 и 17:00\n'
        '3. Напоминать каждые 2 часа (10:00-20:00)\n'
        '4. Напоминать каждый час (10:00-20:00)\n'
        'Выберите:',
        reply_markup=buttons
        )


def one(update, context):
    chat = update.effective_chat
    context.bot.send_message(
        chat_id=chat.id,
        text='Вам будет приходить напоминание 2 раза в день в 10:00 и 15:00'
    )
    schedule.every().day.at("10:00").do(
        straighten_ur_back_random, update, context)
    schedule.every().day.at("15:00").do(
        straighten_ur_back_random, update, context)
    while True:
        try:
            schedule.run_pending()
            time.sleep(RETRY_TIME)
        except Exception as exc:
            message = 'Модуль Scheule не работает как надо'
            raise exc(message)


def two(update, context):
    chat = update.effective_chat
    context.bot.send_message(
        chat_id=chat.id,
        text='Вам будет приходить напоминание 3 '
             'раза в день в 10:00, 14:00 и 17:00)'
    )
    schedule.every().day.at("10:00").do(
        straighten_ur_back_random, update, context)
    schedule.every().day.at("14:00").do(
        straighten_ur_back_random, update, context)
    schedule.every().day.at("17:00").do(
        straighten_ur_back_random, update, context)
    while True:
        try:
            schedule.run_pending()
            time.sleep(RETRY_TIME)
        except Exception as exc:
            message = 'Модуль Scheule не работает как надо'
            raise exc(message)


def three(update, context):
    chat = update.effective_chat
    context.bot.send_message(
        chat_id=chat.id,
        text='Вам будет приходить напоминание '
             'каждые 2 часа (10:00-20:00)',
    )
    schedule.every().day.at("10:00").do(
        straighten_ur_back_random, update, context)
    schedule.every().day.at("12:00").do(
        straighten_ur_back_random, update, context)
    schedule.every().day.at("14:00").do(
        straighten_ur_back_random, update, context)
    schedule.every().day.at("16:00").do(
        straighten_ur_back_random, update, context)
    schedule.every().day.at("18:00").do(
        straighten_ur_back_random, update, context)
    schedule.every().day.at("20:00").do(
        straighten_ur_back_random, update, context)
    while True:
        try:
            schedule.run_pending()
            time.sleep(RETRY_TIME)
        except Exception as exc:
            message = 'Модуль Scheule не работает как надо'
            raise exc(message)


def four(update, context):
    chat = update.effective_chat
    context.bot.send_message(
        chat_id=chat.id,
        text='Вам будет приходить напоминание каждый час (10:00-20:00)'
    )
    schedule.every().day.at("10:00").do(
        straighten_ur_back_random, update, context)
    schedule.every().day.at("11:00").do(
        straighten_ur_back_random, update, context)
    schedule.every().day.at("12:00").do(
        straighten_ur_back_random, update, context)
    schedule.every().day.at("13:00").do(
        straighten_ur_back_random, update, context)
    schedule.every().day.at("14:00").do(
        straighten_ur_back_random, update, context)
    schedule.every().day.at("15:00").do(
        straighten_ur_back_random, update, context)
    schedule.every().day.at("16:00").do(
        straighten_ur_back_random, update, context)
    schedule.every().day.at("17:00").do(
        straighten_ur_back_random, update, context)
    schedule.every().day.at("18:00").do(
        straighten_ur_back_random, update, context)
    schedule.every().day.at("19:00").do(
        straighten_ur_back_random, update, context)
    schedule.every().day.at("20:00").do(
        straighten_ur_back_random, update, context)
    while True:
        try:
            schedule.run_pending()
            time.sleep(RETRY_TIME)
        except Exception as exc:
            message = 'Модуль Scheule не работает как надо'
            raise exc(message)


def main():
    updater = Updater(token=secret_token)
    updater.dispatcher.add_handler(CommandHandler('start', straighten_ur_back))
    updater.dispatcher.add_handler(CommandHandler('my_contacts', my_contacts))
    updater.dispatcher.add_handler(CommandHandler('newcat', new_cat))
    updater.dispatcher.add_handler(
        CommandHandler(
            'time_setting', straighten_ur_back_timer))
    updater.dispatcher.add_handler(CommandHandler('1', one))
    updater.dispatcher.add_handler(CommandHandler('2', two))
    updater.dispatcher.add_handler(CommandHandler('3', three))
    updater.dispatcher.add_handler(CommandHandler('4', four))
    updater.dispatcher.add_handler(
        MessageHandler(Filters.text, straighten_ur_back_random))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    log_format = (
        '%(asctime)s [%(levelname)s] - '
        '(%(filename)s).%(funcName)s:%(lineno)d - %(message)s'
    )

    log_file = os.path.join(BASE_DIR, 'output.log')
    log_stream = sys.stdout
    logging.basicConfig(
        level=logging.INFO,
        format=log_format,
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler(log_stream)
        ]
    )

    try:
        main()
    except KeyboardInterrupt as exc:
        logging.info(f"You went out!{exc}")
