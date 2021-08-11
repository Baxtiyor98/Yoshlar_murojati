from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ParseMode
from Registratsiya import *
from keyboards_ru import *

#
# def start(update, context):
#     context.bot.send_message(chat_id=update.effective_chat.id, text='Iltimos, tilni tanlang👇',
#                              reply_markup=get_language())
#     if is_logged(update.effective_chat.id):
#         user = Registration(update.effective_chat.id)
#         return 'other'
#     else:
#         return 'fname'
def get_fname_ru(update, context):
    # message = update.message.text
    context.bot.send_message(chat_id=update.effective_chat.id,
                                     text='Здравствуйте, уважаемый пользователь, пожалуйста пройдите регистрацию!'
                                          '\nВведите свое имя и фамилию:')
    return 'contact_ru'
def get_contact_ru(update, context):
    message = update.message.text
    if message == '/start':
        return 'start'
    else:
        user = Registration(update.effective_chat.id)
        user.update_reg('f_name_ru', message)
        context.bot.send_message(chat_id=update.effective_chat.id, text=f'{message}! \nПожалуйста, введите номер по формату  (+998YYXXXXXXX) или нажмите кнопку' ,
                                 reply_markup = get_contact1())
        return 'main_ru'

def message_ru(update, context):
    user = Registration(update.effective_chat.id)
    contact = update.message.contact
    phone = contact.phone_number
    user.update_reg('phone_ru', phone)
    context.bot.send_message(chat_id=update.effective_chat.id, text=' Пожалуйста выберите область!',
                             reply_markup=inline_callback_region())
    return 'tuman_ru'

def tuman_ru(update, context):
    query = update.callback_query
    user = Registration(update.effective_chat.id)
    user.update_reg('viloyat', f'{get_region()[int(query.data) - 1][1]}')
    context.bot.send_message(chat_id=update.effective_chat.id, text='Выберите район',
                             reply_markup=inline_callback_tuman(int(query.data)))
    query.message.delete()
    return 'main_menu_ru'

def main_menu_ru(update, context):
    query = update.callback_query
    user = Registration(update.effective_chat.id)
    user.update_reg('tuman', f'{get_tuman(int(query.data) // 10)[int(query.data) // 10 - 1][2]}')
    context.bot.send_message(chat_id=update.effective_chat.id, text='Вы успешно прошли регистрацию!')
    context.bot.send_message(chat_id=update.effective_chat.id, text='Выберите нужный отдел👇',
                             reply_markup=menu_keyb())
    query.message.delete()
    return 'other_ru'

def other_buttons_from_main_menu_ru(update, context):
    mess = update.message.text
    context.bot.send_message(chat_id=update.effective_chat.id, text='Выберите нужный отдел👇',
                                 reply_markup=menu_keyb())
    x = get_menu()
    for i in x:
        if i[1] == mess:
            if i[0] == 5:
                context.bot.send_message(chat_id = update.effective_chat.id , text = f'🗒Нормативно-правовые акты 👇',
                    reply_markup=ReplyKeyboardRemove())
                context.bot.send_message(chat_id=update.effective_chat.id, text='Выберите сферу',
                                         reply_markup=inline_callback_normativ_menu())
                return 'normativ_ru'
            if i[0]==6:
                context.bot.send_message(chat_id=update.effective_chat.id, text='⚙️Настройки',
                                         reply_markup=InlineKeyboardMarkup(setting1_ru()))
                return 'setting_ru'
            if i[0]==7:
                context.bot.send_message(chat_id=update.effective_chat.id, text='🏠️Мой кабинет',
                                         reply_markup=InlineKeyboardMarkup(my_kabinet_ru()))
                return 'my_kabinet_ru'
            if i[0] == 1 or i[0] == 2 or i[0] == 3:
                text = get_main_menu_link(i[0])[0]
                print(text)
                context.bot.send_message(chat_id=update.effective_chat.id,text=f'A\'zo bo\'lish uchun link👇\n \n{text}',
                                         reply_markup = InlineKeyboardMarkup(join_button_ru()))
                return 'check_ru'
            if i[0] == 4:
                text = get_main_menu_link(i[0])[0]
                context.bot.send_photo(chat_id=update.effective_chat.id,
                                      # text=f'Havolaga o\'tish uchun link👇\n \n{text}',
                                      photo=open("C:/Python/Yosh_bot_3/1.png", 'rb'),
                                      caption=f'Havolaga o\'tish uchun link👇\n \n{text}',
                                      reply_markup = InlineKeyboardMarkup(join_button2_ru()))
                return 'check_ru'
def photo_ru(update, context):
    message = update.message.text
    context.bot.send_photo(chat_id = update.effective_chat.id, text = 'Rasm fayl')
def normativ_menu_ru(update, context):
    query = update.callback_query
    x = get_normativ_link(query.data)
    for i in x:
        query.message.reply_html(text=f'{i[0]}')
    if query.data == '0':
        query.message.delete()
        context.bot.send_message(chat_id=update.effective_chat.id, text='Выберите нужный отдел👇',
                             reply_markup=menu_keyb())
        return 'other'

def check_join_ru(update, context):
    query = update.callback_query
    if query.data == '1':
        return
    if query.data == '0':
        query.message.delete()
        context.bot.send_message(chat_id=update.effective_chat.id, text='Выберите нужный отдел👇',
                                reply_markup=menu_keyb())
        return 'other_ru'
def setting_ru(update, context):
    query = update.callback_query
    if query.data == 'lang':
        query.message.delete()
        context.bot.send_message(chat_id=update.effective_chat.id, text='Вы хотите сменить язык?Поменять язык?',
                                 reply_markup=InlineKeyboardMarkup(lang_setting_ru()))
        return 'change_lang_ru'

    if query.data == 'del':
        query.message.delete()
        context.bot.send_message(chat_id=update.effective_chat.id, text='Хотите удалить аккаунт?',
                                 reply_markup=InlineKeyboardMarkup(delete_akk_ru()))
        return 'delete_ru'
    if query.data == 'exit':
        query.message.delete()
        context.bot.send_message(chat_id=update.effective_chat.id, text='Выберите нужный отдел👇',
                                 reply_markup=menu_keyb())
        return 'other_ru'
def change_lang_ru(update, context):
    query = update.callback_query
    if query.data == 'yes':
        query.message.delete()
        context.bot.send_message(chat_id=update.effective_chat.id, text='Пожалуйста, выберите язык👇',
                                 reply_markup=get_language())
        return 'start'
    if query.data == 'no':
        query.message.delete()
        query.message.reply_text(text='Язык остался без изменений!')
        query.message.reply_text(text='⚙Настройки',
                                 reply_markup=InlineKeyboardMarkup(setting1_ru()))
        return 'setting_ru'
def delete_ru(update, context):
    query = update.callback_query
    tg_id = update.effective_chat.id
    if query.data == 'no':
        query.message.delete()
        query.message.reply_text(text='Мы снова с тобой☺️')
        query.bot.send_message(chat_id=update.effective_chat.id, text='⚙Настройки',
                                 reply_markup=InlineKeyboardMarkup(setting1_ru()))
    if query.data == 'yes':
        delete_acc(tg_id)
        if not is_logged(tg_id):
            query.message.delete()
            query.message.reply_text(text='Ваш аккаунт удален из базыi️!')
            return 'start'

def My_kabinet_ru(update, context):
    query = update.callback_query
    if query.data == '1':
        query.message.reply_text(text='Вы не зарегистрированы ни в одном мероприятии')
    if query.data == '2':
        query.message.reply_text(text='У вас нет обращений')
    if query.data == '3':
        query.message.reply_text(text='Вы пока не отправляли идею')
    if query.data == '0':
        query.message.delete()
        context.bot.send_message(chat_id=update.effective_chat.id, text='Выберите нужный отдел👇',
                                 reply_markup=menu_keyb())
        return 'other_ru'