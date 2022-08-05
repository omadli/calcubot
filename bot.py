import math
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


@dp.inline_handler(lambda x: x.text == "")
async def empty_inline(query: types.InlineQuery):
    await query.answer()
    

@dp.inline_handler()
async def _inline(query: types.InlineQuery):
    ns = vars(math).copy()
    ns['__builtins__'] = None
    res = eval(query.text, ns)
    await query.answer(
        results=[
            types.InlineQueryResultArticle(
                id=query.id,
                title="Natija",
                description=str(res),
                input_message_content=types.InputMessageContent(
                    message_text=query.text +" = "+ str(res)
                )
            )    
        ], 
        cache_time=10,
        is_personal=True
        )
