# Initials
import logging
from os import environ
from pathlib import Path
from sys import path

import django

BASE_DIR = Path(__file__).resolve().parent

path.append(f'{BASE_DIR}/core/settings.py')
path.append(f'{BASE_DIR}/core/')
environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings') 
django.setup()

# Imports 
import telebot
from decouple import config
from django.contrib.auth import get_user_model
from telebot import apihelper

# Main Codes


TOKEN = config("TOKEN")
DEBUG = config("DEBUG")
if DEBUG:
	logger = telebot.logger
	telebot.logger.setLevel(logging.DEBUG) # Outputs debug messages to console.

apihelper.proxy = {
	# 'https': 'socks5h://127.0.0.1:9050',
	# 'http':'http://127.0.0.1:8118',
	# 'https':'https://127.0.0.1:8118'
}

bot = telebot.TeleBot(TOKEN)

User = get_user_model()





if __name__ == '__main__':
	print("Start polling...")
	bot.infinity_polling()
	# bot.polling()



