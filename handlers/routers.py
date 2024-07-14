from aiogram import types, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from handlers.creator_rout.get_users import get_users_rout
from handlers.public_rout.help_rout import help_rout
from handlers.public_rout.rout_start import start_rout
from handlers.creator_rout.get_logs_rout import get_logs_rout
from handlers.public_rout.send_rout import send_rout, second_step_send, MessageWait

router: Router = Router()


@router.message(Command('start'))
async def start_routing(message: types.Message):

    await start_rout(message)


@router.message(Command('send'))
async def send_routing(message: types.Message, state: FSMContext):

    await send_rout(message, state)


@router.message(Command('help'))
async def help_routing(message: types.Message):

    await help_rout(message)


@router.message(Command('get_logs'))
async def get_logs_routing(message: types.Message):

    await get_logs_rout(message)


@router.message(Command('get_users'))
async def get_users_routing(message: types.Message):

    await get_users_rout(message)


@router.message(MessageWait.waiting_for_get_message)
async def second_step_send_routing(message: types.Message, state: FSMContext):

    await second_step_send(message, state)


@router.message()
async def unknown_command(message: types.Message):

    await message.answer('Unknown command\n'
                         'Enter /help to get help')
