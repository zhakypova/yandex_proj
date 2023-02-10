import os

import telebot
from celery import shared_task
from account.models import User, Author

bot = telebot.TeleBot(os.environ.get('TELEGRAM_TOKEN'),
                      parse_mode=None)

@shared_task
def send_message(chat_id, message):
    chat_id = []
    for user in User.objects.all():
        chat_id.append(user.telegram_chat_id)
    bot.send_message(chat_id, message)







