# from Conversation import *
# from Conversation_ru import *
#
# def start(update, context):
#     context.bot.send_message(chat_id=update.effective_chat.id, text='Iltimos, tilni tanlang\n'
#                                                                     'Пожалуйста, выберите язык👇',
#                              reply_markup=get_language())
#
#     return 'ajrat'
#
# def ajrat(update, context):
#     message = update.message.text
#     if message == 'O`zbek tili🇺🇿':
#         print('tanladi uz')
#         if not is_logged(update.effective_chat.id):
#             user = Registration(update.effective_chat.id)
#             print('otherga otdi')
#             return 'other'
#         else:
#             context.bot.send_message(chat_id=update.effective_chat.id,
#                                      text='Assalom alaykum, hurmatli foydalanuvchi, iltimos ro\'yxatdan o\'ting! '
#                                           '\nIsm familiyangizni kiriting:')
#             return 'contact'
#     if message == 'Русский язык🇷🇺':
#         print('tanladi ru')
#         if not is_logged(update.effective_chat.id):
#             user = Registration(update.effective_chat.id)
#             print('Ichkarida ru')
#             return 'other_ru'
#         else:
#             print('ishlamadi ru')
#             return 'fname_ru'
