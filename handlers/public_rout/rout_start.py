from aiogram import types
from database_func.user_to_database import user_to_database
from configparser import ConfigParser

config = ConfigParser()
config.read('secret_data/config.ini')

creator_id = config['Telegram']['creator_id']


async def start_rout(message: types.Message) -> None:

    user_id: int = message.from_user.id

    case1 = user_id == creator_id
    case2 = user_id != creator_id

    creator_case = case1 and not case2
    user_case = case2 and not case1

    if creator_case:

        await message.answer(f"Здравствуй, Создатель\n\n"
                             f"Что хочешь сделать сегодня? 💭"
                             f"\n\nДля справки нажмите <b><i>/help</i></b> 👈\n\n"
                             f"Для начала работы нажмите <b><i>/search</i></b>👈\n\n"
                             f"----------Команды создателя👇----------\n\n"
                             f"Получить логи - <b><i>/get_logs</i></b> 👈"
                             f"\n\n\n<b><i>made by you 🫵</i></b>")

    elif user_case:

        await message.answer(f"Здравствуй, я <b>ReAssembler</b>🤖\n\nБот для сбора информации"
                             f" из чатов и каналов в <b><i>Telegram</i></b> 💭"
                             f"\n\nДля справки нажмите <b><i>/help</i></b> 👈\n\n"
                             f"Для начала работы нажмите <b><i>/search</i></b>👈"
                             f"\n\n\n<b><i>made by <a href='https://t.me/kolo_id'>kolo</a></i></b>",
                             disable_web_page_preview=True)

    await user_to_database(message)
