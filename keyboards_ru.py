from telegram import InlineKeyboardButton,InlineKeyboardMarkup,ReplyKeyboardMarkup,KeyboardButton
from connectDB_ru import *

def get_language():
    join = ReplyKeyboardMarkup([
        [
            'O`zbek tili🇺🇿'
        ],
        [
            'Русский язык🇷🇺'
        ],
        # [
        #     'English language🇺🇸'
        # ]
    ],resize_keyboard=True,
    one_time_keyboard=True)
    return join
def get_contact1_ru():
    con_keyboard = KeyboardButton(text="Поделиться номером", request_contact=True)
    custom_keyboard = [[con_keyboard]]
    return ReplyKeyboardMarkup(custom_keyboard, resize_keyboard=True,one_time_keyboard=True)
def inline_callback_region():
    regions = get_region_ru()
    region = []
    t = []
    for x in regions:
        t.append(InlineKeyboardButton(f'{x[1]}', callback_data=f'{x[0]}'))
        if len(t)==2:
            region.append(t)
            t = []
        elif len(regions)-len(region) == 7:
            region.append(t)
            t=[]
    return InlineKeyboardMarkup(region)

def inline_callback_tuman(reg_id):
    print(reg_id)
    tumanlar = get_tuman_ru(reg_id)
    tuman = []
    t = []
    for x in tumanlar:
        t.append(InlineKeyboardButton(f'{x[2]}', callback_data=f'{x[1]}'))
        tuman.append(t)
        t=[]
    a = InlineKeyboardMarkup(
        tuman,
    )
    return InlineKeyboardMarkup(tuman)

def menu_keyb():
    main = get_menu_ru()
    menu = []
    for i in main:
        menu.append([i[1]])
    main_menu = ReplyKeyboardMarkup(
        menu,
        resize_keyboard=True,
        one_time_keyboard=True
    )
    return main_menu

def other_button_from_main_menu(mn_id):
    print('Asosiy menyudan tanlangan id:',mn_id)
    link = get_main_menu_link_ru(mn_id)
    l = []
    for i in link:
        l.append(f'{i[1]}')
    return l[0]

def join_button_ru():
    join = [
        [
            InlineKeyboardButton('Подписаться', callback_data='1',url= 't.me/argos_uz')
        ],
        [
            InlineKeyboardButton('Отмена', callback_data='0')
        ],
    ]
    return join
def join_button2_ru():
    join = [
        [
            InlineKeyboardButton('Перейти по ссылке', callback_data='1',url= 'http://daftar.mehnat.uz')
        ],
        [
            InlineKeyboardButton('Отмена', callback_data='0')
        ],
    ]
    return join
def setting1_ru():
    setting = [
        [
            InlineKeyboardButton('Поменять язык', callback_data='lang'),
            InlineKeyboardButton('Удалить аккаунт', callback_data='del')
        ],
        [
            InlineKeyboardButton('🔙', callback_data='exit')
        ]
    ]
    return setting
def lang_setting_ru():
    language_setting = [
        [
            InlineKeyboardButton('Да✅', callback_data='yes'),
            InlineKeyboardButton('Нет❌', callback_data='no')
        ]
    ]
    return language_setting
def delete_akk_ru():
    delete_account = [
        [
            InlineKeyboardButton('Да✅', callback_data='yes'),
            InlineKeyboardButton('Нет❌', callback_data='no')
        ]
    ]
    return delete_account
def my_kabinet_ru():
    my_kabinet = [
        [
            InlineKeyboardButton('Список зарегистрированных мероприятий', callback_data='1')
        ],
        [
            InlineKeyboardButton('Мои обращения', callback_data='2'),
            InlineKeyboardButton('Мои идеи', callback_data='3')
        ],
        [
            InlineKeyboardButton('🔙', callback_data='0')
        ]
    ]
    return my_kabinet
def inline_callback_normativ_menu():
    norm = get_normativ_menu_ru()
    a = []
    b = []
    for x in norm:
        b.append(InlineKeyboardButton(f'{x[1]}', callback_data=f'{x[0]}'))
        if len(b)==2:
            a.append(b)
            b = []
        elif len(norm)-len(a) == 7:
            a.append(b)
            b=[]
    a.append([InlineKeyboardButton('🔙', callback_data='0')])
    return InlineKeyboardMarkup(a)


