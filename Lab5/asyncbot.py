from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from config import TOKEN
from aiogram.types import ReplyKeyboardRemove,ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

bot = Bot(token=TOKEN)#создаем бота
dp = Dispatcher(bot)#диспетчер для отлавливания сообщений от пользователя

button1=KeyboardButton("👊получи в бубен,бот")

mykeyboard=ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

mykeyboard.add(button1)


@dp.message_handler(commands=['button'])#обработка команды start
async def process_start_command(message):
    await message.reply("лови клавиатуру",reply_markup=mykeyboard)

@dp.message_handler(commands=['start'])#обработка команды start
async def process_start_command(message):
    await message.reply("Привет!\nНапиши мне что-нибудь!")

@dp.message_handler()#обработка любого текстового сообщения от пользователя
async def echo_message(msg: types.Message):
    if msg.text == "👊получи в бубен,бот":
        await bot.send_message(msg.from_user.id, "ай больно, за что?")

if __name__ == '__main__':
    executor.start_polling(dp)