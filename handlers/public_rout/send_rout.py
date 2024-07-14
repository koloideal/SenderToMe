from aiogram import types
from configparser import ConfigParser
from aiogram.fsm.context import FSMContext
from database_func.get_stock_messages import get_stock_messages
from aiogram.fsm.state import StatesGroup, State
from database_func.decrease_stock_messages import decrease_stock_messages


class MessageWait(StatesGroup):
    waiting_for_get_message: State = State()


config = ConfigParser()
config.read('secret_data/config.ini')

creator_id = int(config['Telegram']['creator_id'])


async def send_rout(message: types.Message, state: FSMContext) -> None:

    user_id: int = message.from_user.id

    stock_messages = await get_stock_messages(user_id)

    if stock_messages > 0:

        await message.reply(f'After this message, you will have <b>{stock_messages - 1} message(s)</b> left',
                            parse_mode='HTML')

        await message.answer('<b><i>Enter your message for <a href="https://t.me/kolo_id">kolo</a></i></b>',
                             parse_mode='HTML', disable_web_page_preview=True)

        await state.set_state(MessageWait.waiting_for_get_message)

    else:

        await message.answer('<b>You\'ve run out of messages that you could send to '
                             '<a href="https://t.me/kolo_id">kolo</a></b>',
                             parse_mode='HTML', disable_web_page_preview=True)


async def second_step_send(message: types.Message, state: FSMContext) -> None:

    from main import bot

    await bot.send_message(chat_id=creator_id, text=f'<b>New message from @{message.from_user.username}</b>\n\n'
                                                    f'<span class="tg-spoiler">{message.text}</span>', parse_mode='HTML')

    await message.answer('The message has been sent successfully')

    await decrease_stock_messages(message.from_user.id)

    await state.clear()
