from aiogram import types
from configparser import ConfigParser
from aiogram.types import FSInputFile
from datetime import datetime
from aiogram.exceptions import TelegramBadRequest

config = ConfigParser()
config.read('secret_data/config.ini')

creator_id = int(config['Telegram']['creator_id'])


async def get_logs_rout(message: types.Message):

    user_id = message.from_user.id

    if user_id != creator_id:

        await message.answer('Unknown command\n'
                             'Enter /help to get help')

    else:

        full_file_name: str = f'secret_data/logs.txt'

        document: FSInputFile = FSInputFile(full_file_name)

        captions = f'before {datetime.now().strftime("%d-%m-%Y")}'

        try:

            await message.answer_document(document=document, caption=captions)

        except TelegramBadRequest:

            await message.answer('Logs are empty, enter /start and try again')
