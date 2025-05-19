
import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor

API_TOKEN = os.getenv("API_TOKEN")  # Токен берётся из настроек Render

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.add(
    KeyboardButton("📋 Программа питания"),
    KeyboardButton("🍲 Разрешённые продукты"),
    KeyboardButton("🚫 Запрещённые продукты"),
)
main_menu.add(
    KeyboardButton("❓ Частые вопросы"),
    KeyboardButton("📤 Связаться с автором")
)

@dp.message_handler(commands=['start', 'menu'])
async def send_welcome(message: types.Message):
    await message.answer(
        "Добро пожаловать в бота *Программа функционального питания*!\nВыберите раздел из меню ниже:",
        parse_mode="Markdown",
        reply_markup=main_menu
    )

@dp.message_handler(lambda message: message.text == "📋 Программа питания")
async def program_handler(message: types.Message):
    text = (
        "Переход на функциональное питание включает:\n"
        "- 3–6 приёмов пищи в день\n"
        "- Удаление перекусов\n"
        "- Введение овощей по 0.5 ч.л. в привычные блюда\n"
        "- Исключение сахара, глютена и молока\n"
        "- Активные прогулки и вода каждый день"
    )
    await message.answer(text)

@dp.message_handler(lambda message: message.text == "🍲 Разрешённые продукты")
async def allowed_products_handler(message: types.Message):
    text = (
        "Разрешённые продукты:\n"
        "- Мясо, рыба, яйца\n"
        "- Овощи (кроме картофеля)\n"
        "- Гречка, пшено, овёс\n"
        "- Ягоды, цитрусовые\n"
        "- Бульоны, супы\n"
        "- Натуральные масла"
    )
    await message.answer(text)

@dp.message_handler(lambda message: message.text == "🚫 Запрещённые продукты")
async def forbidden_products_handler(message: types.Message):
    text = (
        "Запрещённые продукты:\n"
        "- Сахар, сладости, выпечка\n"
        "- Молочные продукты\n"
        "- Фастфуд, чипсы\n"
        "- Картофель, рис, пшеница\n"
        "- Сухофрукты, арахис, кешью"
    )
    await message.answer(text)

@dp.message_handler(lambda message: message.text == "❓ Частые вопросы")
async def faq_handler(message: types.Message):
    text = (
        "Часто задаваемые вопросы:\n"
        "— Что делать, если ребёнок не ест?\n"
        "Ответ: не настаивать, предложить еду позже после прогулки.\n\n"
        "— Как вводить новые продукты?\n"
        "Ответ: постепенно, начиная с 0.5 чайной ложки."
    )
    await message.answer(text)

@dp.message_handler(lambda message: message.text == "📤 Связаться с автором")
async def contact_handler(message: types.Message):
    await message.answer("Связаться с автором: @ваш_никнейм или напишите в поддержку.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
