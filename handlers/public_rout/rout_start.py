from aiogram import types
from database_func.user_to_database import user_to_database
from configparser import ConfigParser

config = ConfigParser()
config.read('secret_data/config.ini')

creator_id = int(config['Telegram']['creator_id'])


async def start_rout(message: types.Message) -> None:

    user_id: int = message.from_user.id

    case1 = user_id == creator_id
    case2 = user_id != creator_id

    creator_case = case1 and not case2
    user_case = case2 and not case1

    if creator_case:

        await message.answer(f"Hi, Creator\n\n"
                             f"What do you want to do today? 💭"
                             f"\n\nFor help click <b><i>/help</i></b> 👈\n\n"
                             f"----------Creator commands👇----------\n\n"
                             f"Get logs - <b><i>/get_logs</i></b> 👈\n\n"
                             f"Get users - <b><i>/get_users</i></b> 👈"
                             f"\n\n\n<b><i>made by you 🫵</i></b>")

    elif user_case:

        await message.answer(f"Hi, я <b>SenderToMe</b>🤖\n\n"
                             f"Bot, who will send your message to my creator -"
                             f" <b><a href='https://t.me/kolo_id'>kolo</a></b> 💭"
                             f"\n\nFor help click <b><i>/help</i></b> 👈\n\n"
                             f"To send a message click <b><i>/send</i></b> 👈"
                             f"\n\n\n<b><i>made by <a href='https://t.me/kolo_id'>kolo</a></i></b>",
                             disable_web_page_preview=True)

    await user_to_database(message)
