from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message, CallbackQuery

from settings import Config, Markup
from database.database import DataBase

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext


class HedBot(Config, Markup, DataBase):
    def __init__(self):
        super().__init__()

        self.storage = MemoryStorage()
        self.bot = Bot(self.TOKEN, parse_mode='html')
        self.dp = Dispatcher(self.bot, storage=self.storage)

    async def start(self, msg: Message):
        chat = msg.chat
        if chat.id > 0:
            if not self.check(chat.id):
                await self.UserData().name.set()
                await msg.answer("<b>Добрый день! Пожалуйста, введите ваше имя</b>")
            else:
                name = self.get(chat.id, 'users', 'name')[0]
                await msg.answer(f"<b>Добрый день, <u><a href='tg://user?id={chat.id}'>{name}</a></u>!</b>")

    async def name(self, msg: Message, state: FSMContext):
        chat = msg.chat
        if chat.id > 0:
            async with state.proxy() as data:
                data['name'] = msg.text
                self.User(chat.id, msg.text)

                await state.finish()

            await msg.answer(f"<b>Добро пожаловать в <u>{self.WORLD_NAME_RUS}</u>, {msg.text}</b>!")


    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

    async def move(self, msg: Message):
        chat = msg.chat
        if chat.id > 0 and self.check(chat.id):
            await msg.answer("<b>Для начала выберите зону перемещения: </b>", reply_markup=self.zones)

    async def callback(self, call: CallbackQuery):
        msg = call.message
        chat = msg.chat

        match call.data:
            case "forest":
                await self.bot.edit_message_text(
                    chat_id=chat.id,
                    message_id=msg.message_id,
                    text="<b>Далле выберите область: </b>",
                    reply_markup=self.forest
                )


    def run(self):
        self.dp.register_message_handler(self.start, commands=['start'], state=None)
        self.dp.register_message_handler(self.name, state=self.UserData().name)

        self.dp.register_message_handler(self.move, commands=['map'])
        self.dp.register_callback_query_handler(self.callback, lambda call:True)
        executor.start_polling(
            self.dp, skip_updates=True
        )


if __name__ == '__main__':
    hed_bot = HedBot()
    hed_bot.run()
