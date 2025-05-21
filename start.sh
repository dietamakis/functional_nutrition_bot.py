#!/bin/bash

# Запустить фальшивый HTTP-сервер на 10000 порту
python3 -m http.server 10000 &

# Запустить Telegram-бота
python3 functional_nutrition_bot.py
