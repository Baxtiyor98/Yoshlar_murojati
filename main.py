from telegram.ext import Updater, CommandHandler,ConversationHandler,\
    CallbackQueryHandler,MessageHandler, Filters
from Conversation import *
def main():
    updater = Updater(token='1836503986:AAGsyOfdw5zQBXNrdchVTQXq410wWJlf3lI',use_context = True)
    dispatcher = updater.dispatcher
    photo_handler = MessageHandler(Filters.photo, photo)
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            'start': [MessageHandler(Filters.text, start)],
            # 'ajrat': [MessageHandler(Filters.text, ajrat)],
            'fname': [MessageHandler(Filters.text, get_fname)],
            'contact': [MessageHandler(Filters.text, get_contact)],
            'main': [MessageHandler(Filters.contact, message)],
            'tuman': [CallbackQueryHandler(tuman)],
            'main_menu': [CallbackQueryHandler(main_menu)],
            'other': [MessageHandler(Filters.text, other_buttons_from_main_menu)],
            'normativ': [CallbackQueryHandler(normativ_menu)],
            'check': [CallbackQueryHandler(check_join)],
            'setting': [CallbackQueryHandler(setting)],
            'change_lang': [CallbackQueryHandler(change_lang)],
            'delete': [CallbackQueryHandler(delete)],
            'my_kabinet': [CallbackQueryHandler(My_kabinet)],

            # 'fname_ru': [MessageHandler(Filters.text, get_fname_ru)],
            # 'contact_ru': [MessageHandler(Filters.text, get_contact_ru)],
            # 'main_ru': [MessageHandler(Filters.contact, message_ru)],
            # 'tuman_ru': [CallbackQueryHandler(tuman_ru)],
            # 'main_menu_ru': [CallbackQueryHandler(main_menu_ru)],
            # 'other_ru': [MessageHandler(Filters.text, other_buttons_from_main_menu_ru)],
            # 'normativ_ru': [CallbackQueryHandler(normativ_menu_ru)],
            # 'check_ru': [CallbackQueryHandler(check_join_ru)],
            # 'setting_ru': [CallbackQueryHandler(setting_ru)],
            # 'change_lang_ru': [CallbackQueryHandler(change_lang_ru)],
            # 'delete_ru': [CallbackQueryHandler(delete_ru)],
            # 'my_kabinet_ru': [CallbackQueryHandler(My_kabinet_ru)],
        },
        fallbacks=[CommandHandler('start',start)]
    )
    dispatcher.add_handler(conv_handler)
    dispatcher.add_handler(CallbackQueryHandler(inline_callback_region))
    dispatcher.add_handler(photo_handler)



    updater.start_polling()
    updater.idle()
main()