from config import API_TOKEN
from aiogram import Bot, Dispatcher, executor, types


bot = Bot(token=API_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def cmd_start(message: types.Message) -> None:
    await message.answer(f"Assalomu alaykum {message.from_user.get_mention(as_html=True)}")


@dp.message_handler(commands=['help', 'about'])
async def cmd_help(message: types.Message) -> None:
    await message.answer("Help")

