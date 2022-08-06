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


@dp.inline_handler(lambda x: x.query == "")
async def empty_inline(query: types.InlineQuery):
    await query.answer(
        results=[
            types.InlineQueryResultArticle(
               id=query.id,
               title="Noto'g'ri so'rov",
               description="Kiritgan misolingizni tekshiring:",
               input_message_content=types.InputMessageContent(
                        message_text=f"<code>{query.query}</code>\n\nNo'to'g'ri misol!"
                    ) 
            )
        ],
    )
    

@dp.inline_handler()
async def _inline(query: types.InlineQuery):
    ns = vars(math).copy()
    ns['__builtins__'] = None
    try:
        res = eval(query.query, ns)
        await query.answer(
            results=[
                types.InlineQueryResultArticle(
                    id=query.id,
                    title="Natija",
                    description=str(res),
                    input_message_content=types.InputMessageContent(
                        message_text=query.query +" = "+ str(res),
                        parse_mode=types.ParseMode.HTML                        
                    )
                )    
            ], 
            cache_time=10,
            is_personal=True
        )
    except Exception as e:
        print(e)
        await query.answer(
            results=[
                types.InlineQueryResultArticle(
                id=query.id,
                title="Noto'g'ri so'rov",
                description="Kiritgan misolingizni tekshiring:",
                input_message_content=types.InputMessageContent(
                            message_text=f"<code>{query.query}</code>\n\nNo'to'g'ri misol!",
                            parse_mode=types.ParseMode.HTML
                        ) 
                )
            ],
        )
        
