import telebot
from telebot.types import (
    InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton, Message,
)
import sqlite3
import logging
import requests
from transformers import AutoTokenizer
import json
from database import *
from gpt import *
token = "6723323916:AAFOC91aYdCuv_3qXTx65AV_4GXbkxXEa9E"
bot = telebot.TeleBot(token=token)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="log_file.txt",
    filemode="w",
)



def count_tokens(text):
    tokenizer = AutoTokenizer.from_pretrained("rhysjones/phi-2-orange")  # название модели
    return len(tokenizer.encode(text))

max_tokens_in_task = 512

@bot.message_handler(commands=['debug'])
def send_logs(message):
    with open("log_file.txt", "rb") as f:
        bot.send_document(message.chat.id, f)

@bot.message_handler(commands=['start'])
def start_command(message):
    user_id = message.from_user.id
    create_db()
    create_table()

    user_name = message.from_user.first_name
    logging.info("Отправка приветственного сообщения")
    bot.send_message(message.from_user.id, text=f"Приветствую тебя, {user_name}! Узнать о моих командах можно с помощью /help")
    insert_data(user_id)

@bot.message_handler(commands=['help'])
def help_command(message):
    logging.info("Отправка сообщения со списком команд")
    bot.send_message(message.from_user.id, text="/start - Перезапустить бота, /help - Информация обо всех командах, /about - Что может делать бот, /subjects - Списоу школьных предметов"
                                                "для более детального объяснения, /levels - Выбрать уровень объяснения")

@bot.message_handler(commands=['about'])
def about_command(message):
    logging.info("Отправка сообщения о функциональности бота")
    bot.send_message(message.from_user.id, text="Я могу ответить на любой твой вопрос! Выбери уровень объяснения (/levels), а также школьный предмет"
                                                "(/subjects), а потом просто введи свой запрос")

markup1 = ReplyKeyboardMarkup(resize_keyboard=True)  # заготовка для клавиатуры
markup1.add(KeyboardButton('Продолжить'))
markup1.add(KeyboardButton('/start'))
markup1.add(KeyboardButton('/help'))
markup1.add(KeyboardButton('/about'))






promt = ''
priomt_2 = ''
p = False
sl = {
    'status': p
}
print(sl['status'])


    #bot.send_message(message.chat.id, 'Уровень сложности выбран! Для выбора определенного предмета введи /subject')



promt = ''
promt_2 = ''

@bot.message_handler(commands=['subjects'])
def command_subjects(message):
    bot.send_message(message.chat.id, '/s_math - Математика, /s_physics - Физика, /s_history - История, s_chemistry - Химия, /s_clear - Отменить выбранный предмет')
    logging.info("Отправка списка предметов")

@bot.message_handler(commands=['s_math'])
def math(message):
    global promt
    global promt_2
    user_id = message.from_user.id
    print(user_id)
    bot.send_message(message.chat.id, 'Отлично! теперь можешь ввести задание! И помни. Ты всегда можешь изменить предмет и уровень объяснения (/subjects, /levels)')
    promt_2 = "Imagine that you are the world's leading expert in mathematics. Can you please help me solve this problem?"
    logging.info("Пользователь выбрал предмет 'Математика'")
    subject_math(user_id)

@bot.message_handler(commands=['s_physics'])
def physics(message):
    global promt
    global promt_2
    user_id = message.from_user.id
    bot.send_message(message.chat.id, 'Отлично! теперь можешь ввести задание! И помни. Ты всегда можешь изменить предмет и уровень объяснения (/subjects, /levels)')
    promt_2 = "Imagine that you are the world's leading expert in physics. Can you please help me solve this problem?"
    logging.info("Пользователь выбрал предмет 'Физика'")
    subject_physics(user_id)

@bot.message_handler(commands=['s_history'])
def history(message):
    global promt
    global promt_2
    user_id = message.from_user.id
    bot.send_message(message.chat.id, 'Отлично! теперь можешь ввести задание! И помни. Ты всегда можешь изменить предмет и уровень объяснения (/subjects, /levels)')
    promt_2 = "Imagine that you are the world's leading expert in history. Can you please help me solve this problem?"
    logging.info("Пользователь выбрал предмет 'История'")
    subject_history(user_id)

@bot.message_handler(commands=['s_chemistry'])
def chemistry(message):
    global promt
    global promt_2
    user_id = message.from_user.id
    bot.send_message(message.chat.id, 'Отлично! теперь можешь ввести задание! И помни. Ты всегда можешь изменить предмет и уровень объяснения (/subjects, /levels)')
    promt_2 = "Imagine that you are the world's leading expert in chemistry. Can you please help me solve this problem?"
    logging.info("Пользователь выбрал предмет 'Химия'")
    subject_chemistry(user_id)

@bot.message_handler(commands=['s_clear'])
def command_s_clear(message):
    global promt
    global promt_2
    user_id = message.from_user.id
    bot.send_message(message.chat.id, 'Предмет был успешно отменен. Чтобы заного его задать введите /subjects')
    promt_2 = "Imagine that you are the world's leading expert in chemistry. Can you please help me solve this problem?" #subjects
    logging.info("Пользователь отменил выбранный предмет")
    subject_clear(user_id)


@bot.message_handler(commands=['levels'])
def command_levels(message):
    bot.send_message(message.chat.id, '/l_basic - Базовый, /l_pro - Продвинутый /l_clear - Отменить выбранный уровень')
    logging.info("Отправка списка доступных уровней объяснения")

@bot.message_handler(commands=['l_basic'])
def basic_level(message):
    user_id = message.from_user.id
    bot.send_message(message.chat.id, 'Отлично! теперь можешь ввести задание! И помни. Ты всегда можешь изменить предмет и уровень объяснения (/subjects, /levels)'
                                      'а также вообще не выбирать его')
    global promt
    promt = 'Explain it in simple words'
    logging.info("Пользователь выбрал базовый уровень объяснения")
    lvl_basic(user_id)


@bot.message_handler(commands=['l_pro'])
def pro_level(message):
    user_id = message.from_user.id
    bot.send_message(message.chat.id, 'Отлично! теперь можешь ввести задание! И помни. Ты всегда можешь изменить предмет и уровень объяснения (/subjects, /levels)'
                                      'а также вообще не выбирать его')

    global promt
    promt = 'Explain it in more complicated words'
    logging.info("Пользователь выбрал продвинутый уровень объяснения")
    lvl_pro(user_id)

@bot.message_handler(commands=['l_clear'])
def level_clear(message):
    user_id = message.from_user.id
    bot.send_message(message.chat.id, 'Уровень объяснения отменен. Чтобы заного задать его введите /l_basic или /l_pro')
    global promt
    promt = '' #levels
    logging.info("Пользователь отменил выбранный уровень объяснения")
    lvl_clear(user_id)



@bot.message_handler(func=lambda message: True, content_types=['text'])
def neiroset(message):
    user_id = message.from_user.id
    global promt
    global priomt_2
    task = ''
    answer = ''
    max_tokens_in_task = 512
    if message.text != "Продолжить":
        sl['status'] = True
        if count_tokens(message.text) > max_tokens_in_task:
            long_message(message)
        else:
            generation_answer(message, user_id, promt, promt_2, markup1)
    else:
        continue_answer(message, user_id, promt, promt_2, markup1, task, sl)



logging.info("Бот запущен!!!")
bot.polling()







































