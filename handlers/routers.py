from aiogram import types, Router
from aiogram.filters import Command
from handlers.public_rout.rout_start import start_rout
from handlers.creator_rout.get_logs_rout import get_logs_rout


router: Router = Router()


@router.message(Command('start'))
async def start_routing(message: types.Message):

    await start_rout(message)


@router.message(Command('search'))
async def search_routing(message: types.Message):

    print('hello')


@router.message(Command('get_logs'))
async def get_logs_routing(message: types.Message):

    await get_logs_rout(message)


@router.message()
async def unknown_command(message: types.Message):

    await message.answer('Unknown command\n'
                         'Enter /help to get help')
