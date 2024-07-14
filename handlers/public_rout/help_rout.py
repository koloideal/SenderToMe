from aiogram.types import Message


async def help_rout(message: Message) -> None:

    await message.answer('<b>The bot\'s functionality consists in mediation between the user and the creator '
                         '(<a href="https://t.me/kolo_id">kolo</a>)\n\n'
                         'More precisely: bot sends the messages entered to the creator, filtering spam\n\n'
                         'The user can send only 2 messages</b>', parse_mode='HTML', disable_web_page_preview=True)
