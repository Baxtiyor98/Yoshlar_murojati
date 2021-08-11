from telegram import InlineKeyboardButton,InlineKeyboardMarkup,ReplyKeyboardMarkup,KeyboardButton
from connectDB import *

def get_language():
    join = ReplyKeyboardMarkup([
        [
            'O`zbek tili🇺🇿'
        ],
        [
            'Русский язык🇷🇺'
        ]
    ],resize_keyboard=True,
    one_time_keyboard=True)
    return join
def get_contact1():
    con_keyboard = KeyboardButton(text="Nomerni ulashish", request_contact=True)
    custom_keyboard = [[con_keyboard]]
    return ReplyKeyboardMarkup(custom_keyboard, resize_keyboard=True,one_time_keyboard=True)
def inline_callback_region():
    regions = get_region()
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
    tumanlar = get_tuman(reg_id)
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
    main = get_menu()
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
    link = get_main_menu_link(mn_id)
    l = []
    for i in link:
        l.append(f'{i[1]}')
    return l[0]

def join_button():
    join = [
        [
            InlineKeyboardButton('A\'zo bo\'lish', callback_data='1',url= 't.me/argos_uz')
        ],
        [
            InlineKeyboardButton('Bekor qilish', callback_data='0')
        ],
    ]
    return join
def join_button2():
    join = [
        [
            InlineKeyboardButton('Havolaga o\'tish', callback_data='1',url= 'http://daftar.mehnat.uz')
        ],
        [
            InlineKeyboardButton('Bekor qilish', callback_data='0')
        ],
    ]
    return join
def setting1():
    setting = [
        [
            InlineKeyboardButton('Tilni o`zgartirish', callback_data='lang'),
            InlineKeyboardButton('Akkauntni o`chirish', callback_data='del')
        ],
        [
            InlineKeyboardButton('🔙', callback_data='exit')
        ]
    ]
    return setting
def lang_setting():
    language_setting = [
        [
            InlineKeyboardButton('Ha✅', callback_data='yes'),
            InlineKeyboardButton('Yo`q❌', callback_data='no')
        ]
    ]
    return language_setting
def delete_akk():
    delete_account = [
        [
            InlineKeyboardButton('Ha✅', callback_data='yes'),
            InlineKeyboardButton('Yo`q❌', callback_data='no')
        ]
    ]
    return delete_account
def my_kabinet():
    my_kabinet = [
        [
            InlineKeyboardButton('Ro`yhatdan o`tilgan tadbirlar', callback_data='1')
        ],
        [
            InlineKeyboardButton('Murojaatlarim', callback_data='2'),
            InlineKeyboardButton('G`oyalarim', callback_data='3')
        ],
        [
            InlineKeyboardButton('🔙', callback_data='0')
        ]
    ]
    return my_kabinet
def inline_callback_normativ_menu():
    norm = get_normativ_menu()
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


