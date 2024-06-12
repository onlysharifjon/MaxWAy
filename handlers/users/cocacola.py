#
# import logging
# from aiogram import types
# from aiogram.types import InputMediaPhoto
# from aiogram.utils import executor
# from loader import dp, bot
# from keyboards.inline.inline_buttons import get_keyboard, products
#
# # Boshlang'ich mahsulot hajmi va miqdori
# default_volume = '1.5'
# default_quantity = 1
#
# logging.basicConfig(level=logging.INFO)
#
# @dp.message_handler(text="Coca Cola")
# async def start_command(message: types.Message):
#     volume = default_volume
#     quantity = default_quantity
#     price = products[volume] * quantity
#
#     keyboard = get_keyboard(volume, quantity)
#     caption = f"Coca Cola {volume}l\nNarxi: {price} UZS\nMiqdori: {quantity} ta"
#
#     with open("images/cocacola.jpg", 'rb') as photo:
#         await message.answer_photo(photo, caption=caption, reply_markup=keyboard)
#
# @dp.callback_query_handler()
# async def process_callback(callback_query: types.CallbackQuery):
#     data = callback_query.data
#     message = callback_query.message
#
#     volume = message.caption.split('Coca Cola ')[1].split('l')[0]
#     quantity = int(message.caption.split('Miqdori: ')[1].split(' ')[0])
#
#     if data.startswith('volume_'):
#         volume = data.split('_')[1]
#     elif data == 'increase':
#         quantity += 1
#     elif data == 'decrease':
#         if quantity > 1:
#             quantity -= 1
#         else:
#             await bot.answer_callback_query(callback_query.id, "1dan kam mahsulot tanlash mumkin emas")
#             return
#
#     price = products[volume] * quantity
#
#     keyboard = get_keyboard(volume, quantity)
#     caption = f"Coca Cola {volume}l\nNarxi: {price} UZS\nMiqdori: {quantity} ta"
#
#     with open("images/cocacola.jpg", 'rb') as photo:
#         media = InputMediaPhoto(media=photo, caption=caption)
#         await bot.edit_message_media(
#             media=media,
#             chat_id=message.chat.id,
#             message_id=message.message_id,
#             reply_markup=keyboard
#         )
#
#
#
#
