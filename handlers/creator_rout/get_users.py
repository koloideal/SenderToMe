from aiogram import types
from aiogram.types import FSInputFile
from datetime import datetime
import sqlite3
from sqlite3 import Connection, Cursor
import json
import os
from sqlite3 import OperationalError
from configparser import ConfigParser


config = ConfigParser()
config.read('secret_data/config.ini')

creator_id = int(config['Telegram']['creator_id'])


async def get_users_rout(message: types.Message) -> None:

    user_id: int = message.from_user.id

    if user_id != creator_id:

        await message.answer('Unknown command, enter /help')

    else:

        try:

            connection: Connection = sqlite3.connect('database/bot_users.db')
            cursor: Cursor = connection.cursor()

            cursor.execute('''SELECT * FROM users''')

            all_users: list = cursor.fetchall()

        except OperationalError:

            await message.answer('Database is empty, enter /start and try again')

            cursor.close()
            connection.close()

            return

        else:

            cursor.close()
            connection.close()

        to_dump_data: dict = {}

        for user in all_users:

            to_dump_data[user[2]]: dict = {

                'id': user[0],
                'first_name': user[1],
                'username': user[2],
                'stock_messages': user[3]

            }

        full_file_name: str = f'secret_data/bot_users.json'

        with open(full_file_name, 'w', encoding='utf8') as file:

            json.dump(to_dump_data, file, indent=4, ensure_ascii=False)

        document: FSInputFile = FSInputFile(full_file_name)

        await message.answer_document(document=document, caption=f'before {datetime.now().strftime('%d-%m-%Y')}')

        os.remove(full_file_name)

    return
