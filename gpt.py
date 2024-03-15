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

token = "6723323916:AAFOC91aYdCuv_3qXTx65AV_4GXbkxXEa9E"
bot = telebot.TeleBot(token=token)

def long_message(message):
    bot.send_message(message.chat.id, 'Задача слишком длинная :(')
    logging.info("Пользователь ввел слишком длинный текст")

def generation_answer(message, user_id, promt, promt_2, markup1):
    logging.info("Пользователь ввел задачу")
    bot.send_message(message.chat.id, 'Ответ генерируется. Подождите...')
    task = message.text
    assistant_content = message.text
    task__(user_id, task)
    # answer = resp.json()['choices'][0]['message']['content']
    # gpt_response = resp.json()['choices'][0]['message']['content']
    # bot.send_message(message.chat.id, gpt_response, reply_markup=markup1)

    resp = requests.post(  # POST запрос
        # эндпоинт
        'http://158.160.135.104:1234/v1/chat/completions',
        # заголовок
        headers={"Content-Type": "application/json"},
        # тело запроса
        json={
            "messages": [
                {"role": "user", "content": f'{promt} {task} {promt_2}'},
            ],
            "temperature": 0.7,
            "max_tokens": 512,
        }
    )
    answer = resp.json()['choices'][0]['message']['content']
    answer__(user_id, answer)
    # gpt_response = resp.json()['choices'][0]['message']['content']
    bot.send_message(message.chat.id, answer, reply_markup=markup1)
    logging.info("Пользователь получил ответ")

def continue_answer(message, user_id, promt, promt_2, markup1, task, sl):
    if sl['status'] == True:
        assistant_content = "let's solve the problem step by step: " + task
        logging.info("Пользователь нажал 'Продолжить'")

        resp = requests.post(  # POST запрос
            # эндпоинт
            'http://158.160.135.104:1234/v1/chat/completions',
            # заголовок
            headers={"Content-Type": "application/json"},
            # тело запроса
            json={
                "messages": [
                    {"role": "user", "content": assistant_content},
                ],
                "temperature": 0.7,
                "max_tokens": 512,
            }
        )
        answer = resp.json()['choices'][0]['message']['content']
        answer__(user_id, answer)
        bot.send_message(message.chat.id, answer, reply_markup=markup1)
        logging.info("Пользователь получил продолжение ответа")

    else:
        bot.send_message(message.chat.id, 'Сначала задайте вопрос')
        logging.info("Пользователь нажал 'Продолжить' без ввода текста")

































