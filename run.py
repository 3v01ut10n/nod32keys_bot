import telebot
from telebot import apihelper
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

import config
import utils


bot = telebot.TeleBot(config.token)
apihelper.proxy = config.proxy


def main_menu_keyboard():
    """Main menu in Telegram bot"""
    main_menu = InlineKeyboardMarkup(row_width=1)  # 1 = each button on a new line
    main_menu.add(InlineKeyboardButton('Send keys', callback_data='send_keys'),
                  InlineKeyboardButton('Which keys are right for me?', callback_data='about_keys'),
                  InlineKeyboardButton('Help', callback_data='help')
                  )
    return main_menu


# Bot commands
@bot.message_handler(commands=['start'])
def send_start(message):
    bot.send_message(message.chat.id, 'bot@nod32keys:~$ main_menu', reply_markup=main_menu_keyboard())


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, 'The bot can send keys for the Eset NOD32 antivirus. '
                                      'The keys are updated every 8 hours.\nTo start work, send the /start command')


# Events on pressing menu buttons
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'send_keys':
        bot.send_message(call.from_user.id, utils.send_keys(), parse_mode='Markdown')
    elif call.data == 'about_keys':
        bot.send_message(call.from_user.id, utils.ABOUT_KEYS_MESSAGE, parse_mode='Markdown')
    elif call.data == 'help':
        bot.send_message(call.from_user.id, 'The bot can send keys for the Eset NOD32 antivirus. '
                                            'The keys are updated every 8 hours.\nTo start work, send the /start command')


# Directs to the menu when entering unfamiliar text
@bot.message_handler(content_types=['text'])
def answer_unknown_text(message):
    bot.send_message(message.from_user.id, 'I don\'t understand you. To call the menu write /start')


if __name__ == "__main__":
    bot.polling()
