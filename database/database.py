from sqlite3 import connect as con, OperationalError as oe
from aiogram.dispatcher.filters.state import State, StatesGroup

from datetime import datetime as dt
from hashlib import md5

class DataBase:
    class UserData(StatesGroup):
        name = State()


    class User:
        def __init__(self, id:int, name:str):
            self.id = id
            self.name = name

            self.create_user()

        def create_user(self):
            with con('database/main.db') as c:
                c.execute(
                    f'''
                        INSERT INTO users VALUES(
                            {self.id}, "{self.name}", 2000,
                            "Королевство", 20, 100,
                            "None", "None", "None", "None",
                            "{dt.now().strftime('%Y-%b-%d %H:%M:%S')}"
                        )
                    '''
                )
                c.execute(f'INSERT INTO forest VALUES({self.id}, 0,0,0,0)')
                c.execute(f'INSERT INTO mine VALUES({self.id}, 0,0,0,0,0,0,0,0,0,0,0)')


    def __init__(self):
        pass

    def check(self, id:int):
        with con('database/main.db') as c:
            res = c.execute('SELECT * FROM users')
            return True if len([*res]) > 0 else False

    def get(self, id:int, table:str, field:str):
        with con('database/main.db') as c:
            res = c.execute(f'SELECT {field} FROM {table} WHERE id={id}')

            return [*res][0]