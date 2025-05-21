import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor

API_TOKEN = os.getenv("API_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# --- Блоки сценария и кнопок ---

WELCOME_TEXT = "Добро пожаловать на авторскую программу по переводу ребенка на функциональное питание!"
START_BTN = "Вы готовы начать программу?"
START_ANSWER_BTN = "Да! Начнем!"

FUNC_NUTRITION_TEXT = (
    "Функциональное питание — это питание, которое не просто насыщает организм, но и помогает восстанавливать его работу: "
    "снижает воспаление, улучшает пищеварение, балансирует микрофлору, укрепляет иммунитет и регулирует поведение."
)
FUNC_NUTRITION_BTN = "Почему дети становятся избирательными в еде?"

SELECTIVE_EATING_TEXT = (
    "Избирательность в питании — это ситуация, когда ребёнок отказывается от целых групп продуктов или питается крайне ограниченно.\n"
    "Такое поведение часто беспокоит родителей, ведь от сбалансированного питания напрямую зависит здоровье ребёнка.\n"
    "Существует множество причин, почему возникает избирательность в еде, и одна из них может быть вовсе не очевидной.\n"
    "Паразиты и еда: связь, о которой не принято говорить\n"
    "Наличие паразитов в организме ребёнка может напрямую влиять на его пищевое поведение. Некоторые виды (например, острицы, лямблии) могут вызывать нарушения пищеварения, аллергии, снижение аппетита или наоборот — тягу к определённым продуктам.\n"
    "Нарушения пищеварения, вызванные паразитами — вздутие, нестабильный стул, тошнота — часто фиксируются у детей с избирательностью в еде.\n"
    "Кроме того, паразиты активно \"требуют\" простые углеводы — это их основной источник питания. Поэтому у ребёнка может появиться сильная тяга к сладкому, мучному.\n"
    "Когда стоит задуматься о паразитах\n"
    "Если у ребёнка наблюдается избирательность в питании, особенно если она появилась резко или сопровождается проблемами с ЖКТ, рекомендуется обратиться к врачу и сдать анализы.\n"
    "Роль семьи и привычек в формировании пищевых предпочтений\n"
    "Ещё один важный фактор — это то, какие пищевые привычки формируются в семье. Если дома часто перекусывают, мало готовят домашних блюд, ребёнок перенимает эти модели.\n"
    "Дети не учатся уговорам — они учатся через пример.\n"
    "Также стоит понимать: если ребёнок постоянно получает \"вкусненькое\" между приёмами пищи — он не будет испытывать аппетита к обычной еде."
)
SELECTIVE_EATING_BTN = "Программа поможет вернуть ребёнку аппетит и расширить пищевые предпочтения — особенно если это сопровождается поддержкой семьи."

WHAT_TO_DO_BTN = "Что делать?"
WHAT_TO_DO_TEXT = (
    "Моральная поддержка\n"
    "Когда вы решаете наладить питание ребёнка, важно помнить: вы не просто меняете список продуктов — вы меняете семейные привычки.\n"
    "Представьте, как чувствует себя малыш, если он ест гречку с овощами, а рядом кто-то из семьи открывает шоколадку или пьёт газировку. Это сильно демотивирует.\n"
    "Именно поэтому лучше всего, если вся семья хотя бы на время будет придерживаться той же программы питания.\n"
    "Почему важно переходить на правильное питание всей семьёй\n"
    "✅ Ребёнку легче адаптироваться. Он чувствует, что не один — что это общее дело. Это снимает стресс и сопротивление.\n"
    "✅ Вы подаёте пример. Дети копируют поведение родителей. Если вы с удовольствием едите суп с овощами — ребёнок рано или поздно попробует тоже.\n"
    "✅ Выстраивается доверие. Ребёнок чувствует, что его не наказывают, не ограничивают, а заботятся о его здоровье.\n"
    "✅ Вы тоже улучшаете своё здоровье. Переходя на функциональное питание ради ребёнка, вы в итоге помогаете и себе.\n"
    "Когда семья — одна команда, любые перемены даются легче. Пусть ваш пример, терпение и любовь станут главным мотиватором для малыша!"
)
FAMILY_BTN = "Когда семья — одна команда, любые перемены даются легче. Пусть ваш пример, терпение и любовь станут главным мотиватором для малыша!"

READY_BTN = "Я готов/-а"
CHOOSE_CASE_TEXT = (
    "Выберите тот кейс, который ближе всего вам подходит:\n"
    "• Кейс №1. Ребёнок ест все что готовит родители. Пример: может иметь зависимость от сладкого и/или мучного.\n"
    "• Кейс №2. Ребёнок с небольшой избирательностью в питании. Пример: ребёнок может есть мясо или рыбу с макаронами, но не любит овощи.\n"
    "• Кейс №3. Ребёнок с большой избирательностью. Пример: ест только перекусами, не ест горячий еды совсем и т.д."
)
CASE1_BTN = "Кейс №1."
CASE2_BTN = "Кейс №2."
CASE3_BTN = "Кейс №3."


# --- Логика маршрутизации по кнопкам ---

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton(START_ANSWER_BTN))
    await message.answer(WELCOME_TEXT, reply_markup=keyboard)

@dp.message_handler(lambda msg: msg.text == START_ANSWER_BTN)
async def func_nutrition_handler(message: types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton(FUNC_NUTRITION_BTN))
    await message.answer(FUNC_NUTRITION_TEXT, reply_markup=keyboard)

@dp.message_handler(lambda msg: msg.text == FUNC_NUTRITION_BTN)
async def selective_eating_handler(message: types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton(SELECTIVE_EATING_BTN))
    await message.answer(SELECTIVE_EATING_TEXT, reply_markup=keyboard)

@dp.message_handler(lambda msg: msg.text == SELECTIVE_EATING_BTN)
async def what_to_do_handler(message: types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton(WHAT_TO_DO_BTN))
    await message.answer(WHAT_TO_DO_TEXT, reply_markup=keyboard)

@dp.message_handler(lambda msg: msg.text == WHAT_TO_DO_BTN)
async def family_handler(message: types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton(FAMILY_BTN))
    await message.answer(WHAT_TO_DO_TEXT, reply_markup=keyboard)

@dp.message_handler(lambda msg: msg.text == FAMILY_BTN)
async def ready_handler(message: types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton(READY_BTN))
    await message.answer(FAMILY_BTN, reply_markup=keyboard)

@dp.message_handler(lambda msg: msg.text == READY_BTN)
async def choose_case_handler(message: types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton(CASE1_BTN))
    keyboard.add(KeyboardButton(CASE2_BTN))
    keyboard.add(KeyboardButton(CASE3_BTN))
    await message.answer(CHOOSE_CASE_TEXT, reply_markup=keyboard)

@dp.message_handler()
async def default_handler(message: types.Message):
    await message.answer("Пожалуйста, используйте кнопки для навигации по программе.")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
