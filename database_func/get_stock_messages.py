import sqlite3
from sqlite3 import Connection, Cursor


async def get_stock_messages(id: int) -> int:

    connection: Connection = sqlite3.connect('database/bot_users.db')
    cursor: Cursor = connection.cursor()

    cursor.execute('''SELECT stock_messages FROM users WHERE id = ?''', (id, ))
    stock_messages = cursor.fetchone()

    connection.commit()

    cursor.close()
    connection.close()

    return int(stock_messages[0])
