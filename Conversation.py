from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ParseMode
from Registratsiya import *
from keyboards import *


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Iltimos, tilni tanlang👇',
                             reply_markup=get_language())
    if is_logged(update.effective_chat.id):
        user = Registration(update.effective_chat.id)
        return 'other'
    else:
        return 'fname'
def get_fname(update, context):
    message = update.message.text
    context.bot.send_message(chat_id=update.effective_chat.id,
                                         text='Assalom alaykum, hurmatli foydalanuvchi, iltimos ro\'yxatdan o\'ting! '
                                              '\nIsm familiyangizni kiriting:')
    return 'contact'
def get_contact(update, context):
    message = update.message.text
    user = Registration(update.effective_chat.id)
    user.update_reg('f_name', message)
    context.bot.send_message(chat_id=update.effective_chat.id, text=f'{message}! \nIltimos, nomerni ulashish tugmasini bosing' ,
                                 reply_markup = get_contact1())
    return 'main'

def message(update, context):
    user = Registration(update.effective_chat.id)
    contact = update.message.contact
    phone = contact.phone_number
    user.update_reg('phone', phone)
    context.bot.send_message(chat_id=update.effective_chat.id, text='Viloyatingizni tanlang!',
                             reply_markup=inline_callback_region())
    return 'tuman'

def tuman(update, context):
    query = update.callback_query
    user = Registration(update.effective_chat.id)
    user.update_reg('viloyat', f'{get_region()[int(query.data) - 1][0]}')
    context.bot.send_message(chat_id=update.effective_chat.id, text='Tumaningizni tanlang',
                             reply_markup=inline_callback_tuman(int(query.data)))
    query.message.delete()
    return 'main_menu'

def main_menu(update, context):
    print('Main_menu ishladi')
    query = update.callback_query
    user = Registration(update.effective_chat.id)
    print('Tuman:',tuman_write(int(query.data))[0][0])
    user.update_reg('tuman', f'{tuman_write(int(query.data))[0][0]}')
    context.bot.send_message(chat_id=update.effective_chat.id, text='Ro\'yxatdan muvaffaqqiyatli o\'tdingiz!')
    context.bot.send_message(chat_id=update.effective_chat.id, text='Kerakli bo`limni tanlang👇',
                             reply_markup=menu_keyb())
    query.message.delete()
    return 'other'

def other_buttons_from_main_menu(update, context):
    print('Boshqa buttonlar ishladi')
    mess = update.message.text

    if mess == "Русский язык🇷🇺":
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=f'Скоро будет работать и для русского языка. Пожалуйста, нажмите /start')
        print('2 ishladi')
        return 'start'

    if mess == 'O`zbek tili🇺🇿':
        context.bot.send_message(chat_id=update.effective_chat.id, text='Kerakli bo`limni tanlang👇',
                                 reply_markup=menu_keyb())
        print('1 ishladi')
    x = get_menu()
    print(x)
    for i in x:
        if i[1] == mess:
            print(mess,i[0])

            if i[0] == 5:
                print('Main menu:', i[0])
                context.bot.send_message(chat_id = update.effective_chat.id , text = f'🗒Normativ huquqiy hujjatlar bo`limi👇',
                    reply_markup=ReplyKeyboardRemove())
                context.bot.send_message(chat_id=update.effective_chat.id, text='Soha turini tanlang',
                                         reply_markup=inline_callback_normativ_menu())
                return 'normativ'
            if i[0]==6:
                context.bot.send_message(chat_id=update.effective_chat.id, text='⚙️Sozlamalar',
                                         reply_markup=InlineKeyboardMarkup(setting1()))
                return 'setting'
            if i[0]==7:
                context.bot.send_message(chat_id=update.effective_chat.id, text='🏠️Mening kabinetim',
                                         reply_markup=InlineKeyboardMarkup(my_kabinet()))
                return 'my_kabinet'
            if i[0] == 1 or i[0] == 2 or i[0] == 3:
                text = get_main_menu_link(i[0])[0]
                print(text)
                context.bot.send_message(chat_id=update.effective_chat.id,text=f'A\'zo bo\'lish uchun link👇\n \n{text}',
                                         reply_markup = InlineKeyboardMarkup(join_button()))
                return 'check'
            if i[0] == 4:
                text = get_main_menu_link(i[0])[0]
                context.bot.send_photo(chat_id=update.effective_chat.id,
                                      photo=open("C:/Python/Yosh_bot_3/1.png", 'rb'),
                                      caption=f'Havolaga o\'tish uchun link👇\n \n{text}',
                                      reply_markup = InlineKeyboardMarkup(join_button2()))
                return 'check'
def photo(update, context):
    message = update.message.text
    context.bot.send_photo(chat_id = update.effective_chat.id, text = 'Rasm fayl')
def normativ_menu(update, context):
    query = update.callback_query
    x = get_normativ_link(query.data)
    for i in x:
        print(query.data,i[0])
        query.message.reply_html(text=f'{i[0]}')
    if query.data == '0':
        query.message.delete()
        context.bot.send_message(chat_id=update.effective_chat.id, text='Kerakli bo`limni tanlang👇',
                             reply_markup=menu_keyb())
        return 'other'

def check_join(update, context):
    query = update.callback_query
    if query.data == '1':
        return
    if query.data == '0':
        query.message.delete()
        context.bot.send_message(chat_id=update.effective_chat.id, text='Kerakli bo`limni tanlang👇',
                                reply_markup=menu_keyb())
        return 'other'
def setting(update, context):
    query = update.callback_query
    if query.data == 'lang':
        query.message.delete()
        context.bot.send_message(chat_id=update.effective_chat.id, text='Tilni o\'zgartirmoqchimisiz?',
                                 reply_markup=InlineKeyboardMarkup(lang_setting()))
        return 'change_lang'

    if query.data == 'del':
        query.message.delete()
        context.bot.send_message(chat_id=update.effective_chat.id, text='Akkountingizni o\'chirmoqchimisiz?',
                                 reply_markup=InlineKeyboardMarkup(delete_akk()))
        return 'delete'
    if query.data == 'exit':
        query.message.delete()
        print('exit setting worked')
        context.bot.send_message(chat_id=update.effective_chat.id, text='Kerakli bo`limni tanlang👇',
                                 reply_markup=menu_keyb())
        return 'other'
def change_lang(update, context):
    query = update.callback_query
    if query.data == 'yes':
        query.message.delete()
        context.bot.send_message(chat_id=update.effective_chat.id, text='Iltimos, tilni tanlang👇',
                                 reply_markup=get_language())
        return 'start'
    if query.data == 'no':
        query.message.delete()
        query.message.reply_text(text='Til o\'zgarishsiz qoldirildi!')
        query.message.reply_text(text='⚙️Sozlamalar',
                                 reply_markup=InlineKeyboardMarkup(setting1()))
        return 'setting'
def delete(update, context):
    query = update.callback_query
    tg_id = update.effective_chat.id
    if query.data == 'no':
        query.message.delete()
        query.message.reply_text(text='Siz bilan yana birgamiz☺️')
        query.bot.send_message(chat_id=update.effective_chat.id, text='⚙️Sozlamalar',
                                 reply_markup=InlineKeyboardMarkup(setting1()))
        return 'setting'
    if query.data == 'yes':
        delete_acc(tg_id)
        if not is_logged(tg_id):
            query.message.delete()
            query.message.reply_text(text='Siznning akkauntingiz o\'chirildii️! /start bosing')
            return 'start'

def My_kabinet(update, context):
    query = update.callback_query
    if query.data == '1':
        query.message.reply_text(text='Siz birorta tadbirdan ro`yxatdan o`tmagansiz')
    if query.data == '2':
        query.message.reply_text(text='Sizda murojaatlar mavjud emas')
    if query.data == '3':
        query.message.reply_text(text='Sizda g`oyalar soni mavjud emas')
    if query.data == '0':
        query.message.delete()
        context.bot.send_message(chat_id=update.effective_chat.id, text='Kerakli bo`limni tanlang👇',
                                 reply_markup=menu_keyb())
        return 'other'