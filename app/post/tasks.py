import os

import telebot
from celery import shared_task
from account.models import User, Author

bot = telebot.TeleBot(os.environ.get('TELEGRAM_TOKEN'),
                      parse_mode=None)


@shared_task
def send_message(message):
    recipient_ids = []
    for user in Author.objects.all():
        recipient_ids.append(user.telegram_chat_id)
    for recipient in recipient_ids:
        bot.send_message(recipient, message)





