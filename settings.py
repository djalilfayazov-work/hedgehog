from aiogram.types import ReplyKeyboardMarkup as km
from aiogram.types import KeyboardButton as kb
from aiogram.types import InlineKeyboardMarkup as im
from aiogram.types import InlineKeyboardButton as ib

class Config:
    def __init__(self):
        self.TOKEN = '6665343438:AAGf_30HMMUAnJeS5e1CYgWNvJY-Nf1nWbc'

        self.WORLD_NAME_RUS = 'Игольчатое Королевство'
        self.WORLD_NAME_ENG = 'The Needle Kingdom'

        self.__BOT_ID = 6665343438

class Markup:
    zones = im(row_width=1, inline_keyboard=[
        [ib("🌲 Лес", callback_data="forest")],
        [ib("🌱 Болото", callback_data="swamp")],
        [ib("🛡 Кланы", callback_data="clan")],
        [ib("🔥 HotKeys", callback_data="hotkeys")]
    ])

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

    forest = im(row_width=1, inline_keyboard=[
        [ib("🫐 Поляна", callback_data="forest_glade")],
        [ib("🪵 Лесорубка", callback_data="forest_logging")]
    ])

    swamp = im(row_width=1, inline_keyboard=[
        [ib("🫐 Поляна", callback_data="swamp_glade")],
        [ib("🪵 Лесорубка", callback_data="swamp_logging")],
        [ib("🏚 Изба", callback_data="cottage")],
        [ib("🕳 Скважина", callback_data="oilwell")],
    ])

    hotkeys = km(resize_keyboard=True, keyboard=[
        [kb("⛏ Шахта")],[kb("🌿 Травы")],
        [kb("🐺 Фауна")],[kb("🏠 Особня")]
    ])

    clan = im(row_width=5, inline_keyboard=[
        [
            ib("r3gF", callback_data="r3gF"), ib("FNpG", callback_data="FNpG"),
            ib("tbkF", callback_data="tbkF"), ib("AHWj", callback_data="AHWj"),
        ],
        [
            ib("JOZc", callback_data="JOZc"), ib("4Km9", callback_data="4Km9"),
            ib("U7Zp", callback_data="U7Zp"), ib("P23g", callback_data="P23g"),
        ],
        [
            ib("OVJ6", callback_data="OVJ6"), ib("L4cs", callback_data="L4cs"),
            ib("x5Po", callback_data="x5Po"), ib("6JVD", callback_data="6JVD"),
        ],
        [   ib("3slz", callback_data="3slz"), ib("ARYP", callback_data="ARYP"),
            ib("ybLS", callback_data="ybLS"), ib("sklQ", callback_data="sklQ"),
        ],
        [
            ib("PL8F", callback_data="PL8F"), ib("iYex", callback_data="iYex"),
            ib("53WN", callback_data="53WN"), ib("sRG1", callback_data="sRG1"),
        ],
        [
            ib("jgM3", callback_data="jgM3"), ib("1xXJ", callback_data="1xXJ"),
            ib("uZWK", callback_data="uZWK"), ib("DrJW", callback_data="DrJW"),
        ]
    ])

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

    forest_glade = im(row_width=1, inline_keyboard=[
        [ib("Ягодная Радуга", callback_data="glade1")],
        [ib("Малиновая Поляна", callback_data="glade2")],
        [ib("Голубичный Уголок", callback_data="glade3")],
        [ib("Клубника Пикник", callback_data="glade4")],
        [ib("Земляничный Рай", callback_data="glade5")],
        [ib("Шиповниковый Коридор", callback_data="glade6")]
    ])
    swamp_glade = im(row_width=1, inline_keyboard=[
        [ib("Клюквенный Берег", callback_data="glade7")],
        [ib("Брусничная Роща", callback_data="glade8")],
        [ib("Ароматный Край", callback_data="glade9")],
        [ib("Черничная Оазис", callback_data="glade10")],
        [ib("Морошка Крапива", callback_data="glade11")],
        [ib("Красноягодный Угол", callbacka_data="glade12")]
    ])

    forest_logging = im(row_width=1, inline_keyboard=[
        [ib("Бревенчатый Лагерь", callback_data="logging1")],
        [ib("Пилорама Гроза", callback_data="logging2")],
        [ib("Топорище", callback_data="logging3")],
        [ib("Дровосекова Задача", callback_data="logging4")],
        [ib("Лесная Рубка", callback_data="logging5")],
        [ib("Секачи Призраки", callback_data="logging6")]
    ])
    swamp_logging = im(row_width=1, inline_keyboard=[
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

    ut1 = im(row_width=1, inline_keyboard=[
        [ib("🗺 Главная карта", callback_data="main_map")],
        [ib("❌ Cancel", callback_data="cancel_move")]
    ])
    ut2 = im(row_width=2, inline_keyboard=[[
        ib("🗺 Главная карта", callback_data="main_map"),
        ib("❌ Cancel", callback_data="cancel_move")
    ]])
