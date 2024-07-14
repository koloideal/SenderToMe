import sqlite3
from sqlite3 import Connection, Cursor


async def decrease_stock_messages(id: int) -> None:

    connection: Connection = sqlite3.connect('database/bot_users.db')
    cursor: Cursor = connection.cursor()

    cursor.execute('''UPDATE users SET stock_messages = (stock_messages + ?) WHERE id = ?''', (-1, id))

    connection.commit()

    cursor.close()
    connection.close()
