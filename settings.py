from aiogram.types import ReplyKeyboardMarkup as km
from aiogram.types import KeyboardButton as kb
from aiogram.types import InlineKeyboardMarkup as im
from aiogram.types import InlineKeyboardButton as ib

class Config:
    def __init__(self):
        self.TOKEN = '6665343438:AAGf_30HMMUAnJeS5e1CYgWNvJY-Nf1nWbc'

        self.WORLD_NAME_RUS = 'Игольчатое Королевство'
        self.WORLD_NAME_ENG = 'The Needle Kingdom'


class Markup:
    zones = im(row_width=1, inline_keyboard=[
        [ib("🌲 Лес", callback_data="forest")],
        [ib("🌱 Болото", callback_data="swamp")],
        [ib("🛡 Кланы", callback_data="clan")],
        [ib("🔥 HotKeys", callback_data="hotkeys")]
    ])

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

    forest = im(row_width=1, inline_keyboard=[
        [ib("🫐 Поляна", callback_data="glade")],
        [ib("🪵 Лесорубка", callback_data="logging")],
        [ib("🏠 Особня", callback_data="mansion")],
    ])

    swamp = im(row_width=1, inline_keyboard=[
        [ib("🫐 Поляна", callback_data="glade")],
        [ib("🪵 Лесорубка", callback_data="logging")],
        [ib("🏚 Изба", callback_data="cottage")],
        [ib("🕳 Скважина", callback_data="oilwell")],

    ])

    hotkeys = im(row_width=1, inline_keyboard=[
        [ib("⛏ Шахта", callback_data="mine")],
        [ib("🌿 Травы", callback_data="grass")],
        [ib("🐺 Фауна", callback_data="fauna")]
    ])

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

    glade = im(row_width=1, inline_keyboard=[
        [ib("Ягодная Радуга", callback_data="glade1")],
        [ib("Малиновая Поляна", callback_data="glade2")],
        [ib("Голубичный Уголок", callback_data="glade3")],
        [ib("Клубника Пикник", callback_data="glade4")],
        [ib("Земляничный Рай", callback_data="glade5")],
        [ib("Шиповниковый Коридор", callback_data="glade6")],
        [ib("Клюквенный Берег", callback_data="glade7")],
        [ib("Брусничная Роща", callback_data="glade8")],
        [ib("Ароматный Край", callback_data="glade9")],
        [ib("Черничная Оазис", callback_data="glade10")],
        [ib("Морошка Крапива", callback_data="glade11")],
        [ib("Красноягодный Угол", callback_data="glade12")]
    ])

    logging = im(row_width=1, inline_keyboard=[
        [ib("Бревенчатый Лагерь", callback_data="logging1")],
        [ib("Пилорама Гроза", callback_data="logging2")],
        [ib("Топорище", callback_data="logging3")],
        [ib("Дровосекова Задача", callback_data="logging4")],
        [ib("Лесная Рубка", callback_data="logging5")],
        [ib("Секачи Призраки", callback_data="logging6")],
        [ib("Рубильный Край", callback_data="logging7")],
        [ib("Сосновая Палуба", callback_data="logging8")],
        [ib("Тигель Древесины", callback_data="logging9")],
        [ib("Осиная Мастерская", callback_data="logging10")],
        [ib("Расколотый Дуб", callback_data="logging11")],
        [ib("Лесной Трофей", callback_data="logging12")]
    ])

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

    berry = km(resize_keyboard=True, keyboard=[[kb("Добыть ягоды")]])
    log = km(resize_keyboard=True, keyboard=[[kb("Добыть бревна")]])
