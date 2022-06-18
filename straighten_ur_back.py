import os
import random
import time
import schedule

from telegram.ext import CommandHandler, MessageHandler, Filters, Updater

from telegram import ReplyKeyboardMarkup

from dotenv import load_dotenv

load_dotenv()
secret_token = os.getenv('TOKEN')
updater = Updater(token=secret_token)


def straighten_ur_back(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    button = ReplyKeyboardMarkup([
        ['/my_contacts'],
        ['/time_setting']
        ],
        resize_keyboard=True)
    context.bot.send_message(
        chat_id=chat.id,
        text='Привет, {}. Выпрями спину!'.format(name),
        reply_markup=button
    )


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
        'В Ы П Р Я М И С П И Н У'
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
        ],
        resize_keyboard=True)
    context.bot.send_message(
        chat_id=chat.id,
        text='1. Напоминать раз в день (в 14:00)\n'
        '2. Напоминать 3 раза в день (14:00, 16:00, 18:00)\n'
        '3. Напоминать каждые 2 часа (14:00-20:00)\n'
        'Выберите:',
        reply_markup=buttons
        )


def one(update, context):
    chat = update.effective_chat
    context.bot.send_message(
        chat_id=chat.id,
        text='Вам будет приходить напоминание раз в день (в 14:00)'
    )
    schedule.every().day.at("14:00").do(
        straighten_ur_back_random, update, context)

    while True:
        schedule.run_pending()
        time.sleep(1)


def two(update, context):
    chat = update.effective_chat
    context.bot.send_message(
        chat_id=chat.id,
        text='Вам будет приходить напоминание 3 '
             'раза в день (14:00, 16:00, 18:00)'
    )
    schedule.every().day.at("14:00").do(
        straighten_ur_back_random, update, context)
    schedule.every().day.at("16:00").do(
        straighten_ur_back_random, update, context)
    schedule.every().day.at("18:00").do(
        straighten_ur_back_random, update, context)

    while True:
        schedule.run_pending()
        time.sleep(1)


def three(update, context):
    chat = update.effective_chat
    context.bot.send_message(
        chat_id=chat.id,
        text='Вам будет приходить напоминание '
             'каждые 2 часа (14:00-20:00)',
    )
    schedule.every().day.at("14:00").do(
        straighten_ur_back_random, update, context)
    schedule.every().day.at("16:00").do(
        straighten_ur_back_random, update, context)
    schedule.every().day.at("18:00").do(
        straighten_ur_back_random, update, context)
    schedule.every().day.at("20:00").do(
        straighten_ur_back_random, update, context)

    while True:
        schedule.run_pending()
        time.sleep(1)


updater.dispatcher.add_handler(CommandHandler('start', straighten_ur_back))
updater.dispatcher.add_handler(CommandHandler('my_contacts', my_contacts))
updater.dispatcher.add_handler(
    CommandHandler(
        'time_setting', straighten_ur_back_timer))
updater.dispatcher.add_handler(CommandHandler('1', one))
updater.dispatcher.add_handler(CommandHandler('1', two))
updater.dispatcher.add_handler(CommandHandler('1', three))
updater.dispatcher.add_handler(
    MessageHandler(Filters.text, straighten_ur_back_random))

if __name__ == '__main__':
    updater.start_polling()
    updater.idle()
