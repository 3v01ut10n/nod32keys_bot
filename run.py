import telebot
import config
from eset_bot import *
from telebot import apihelper
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


bot = telebot.TeleBot(config.token)
apihelper.proxy = config.proxy

print(TIME_NOW + 'Bot activated')
autoupdate_key()


def main_menu_keyboard():
    """Главное меню"""
    main_menu = InlineKeyboardMarkup()
    main_menu.row_width = 1  # 1 = каждый пункт с новой строки
    main_menu.add(InlineKeyboardButton('Отправить ключи', callback_data='send_keys'),
                  InlineKeyboardButton('Какие ключи мне подойдут?', callback_data='about_keys'),
                  InlineKeyboardButton('Помощь', callback_data='help')
                 )
    return main_menu


# команды /start и /help
@bot.message_handler(commands=['start'])
def send_start(message):
        bot.send_message(message.chat.id, 'bot@nod32keys:~$ main_menu', reply_markup=main_menu_keyboard())


@bot.message_handler(commands=['help'])
def send_help(message):
        bot.send_message(message.chat.id, 'Бот умеет отправлять ключи для антивируса Eset NOD32. Ключи обновляются раз в 8 часов.\nДля начала работы, отправь команду /start')


# события на нажатия кнопок меню
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'send_keys':
        bot.send_message(call.from_user.id, send_keys(), parse_mode='Markdown')
    elif call.data == 'about_keys':
        bot.send_message(call.from_user.id, ABOUT_KEYS_MESSAGE, parse_mode='Markdown')
    elif call.data == 'help':
        bot.send_message(call.from_user.id, 'Бот умеет отправлять ключи для антивируса Eset NOD32. Ключи обновляются раз в 8 часов.\nДля начала работы, отправь команду /start')


# посылает в меню при вводе незнакомого текста
@bot.message_handler(content_types=['text'])
def answer_unknown_text(message):
        bot.send_message(message.from_user.id, 'Я тебя не понимаю. Для вызова меню напиши /start')


if __name__ == "__main__":
    bot.polling()
