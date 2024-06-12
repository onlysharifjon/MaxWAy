from loader import dp
from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.inline_buttons import Gamburger,Chizburger,Bigburger



sonGamburger = {
    'count': 1,
}


@dp.message_handler(text="Gamburger")
async def gamburger(message: types.Message):
    await message.answer("Mahsulot miqdorini tanlang")
    await message.answer_photo(photo=open('images/gamburger.jpg', 'rb'), caption="""
Gamburger 
Burger bulochkasi, tuzlangan bodring, pomidor, go'shtli Patti, qizil piyoz, aysberg, Burger sousi
 

Gamburger 25 000 x 1 = 25 000
Umumiy: 25 000 UZS""", reply_markup=Gamburger)


@dp.callback_query_handler(text='plusgamburger')
async def plusgam(call: types.CallbackQuery):
    print(sonGamburger)
    sonGamburger['count'] += 1

    Gamburger = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minusgamburger"),
                InlineKeyboardButton(text=str(sonGamburger['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plusgamburger")
            ],
            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ]
        ]
    )

    summagamburger = 25000 * sonGamburger['count']
    new_caption = f"""
Gamburger 
Burger bulochkasi, tuzlangan bodring, pomidor, go'shtli Patti, qizil piyoz, aysberg, Burger sousi


Gamburger 25 000 x  {sonGamburger['count']} = {summagamburger}
Umumiy: {summagamburger} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/gamburger.jpg', 'rb'), chat_id=call.message.chat.id,
                                    message_id=call.message.message_id, caption=new_caption
                                    ), reply_markup=Gamburger,
    )


@dp.callback_query_handler(text='minusgamburger')
async def minusgam(call: types.CallbackQuery):
    print(sonGamburger)

    if sonGamburger['count'] > 1:
        sonGamburger['count'] -= 1

        Gamburger = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="minusgamburger"),
                    InlineKeyboardButton(text=str(sonGamburger['count']), callback_data='0'),
                    InlineKeyboardButton(text='+', callback_data="plusgamburger")
                ],

                [
                    InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
                ]
            ]
        )

        summagamburger = 25000 * sonGamburger['count']
        new_caption = f"""
Gamburger 
Burger bulochkasi, tuzlangan bodring, pomidor, go'shtli Patti, qizil piyoz, aysberg, Burger sousi


Gamburger 25 000 x  {sonGamburger['count']} = {summagamburger}
Umumiy: {summagamburger} UZS"""

        await call.message.edit_media(
            media=types.InputMediaPhoto(open('images/gamburger.jpg', 'rb'), caption=new_caption),
            reply_markup=Gamburger
        )
    else:
        await call.answer("1dan kam mahsulot tanlash mumkin emas")


#-----------------------------------------------------------------------------------------------------------------------


sonChizburger = {
    'count': 1,
}


@dp.message_handler(text="Chizburger")
async def chizburger(message: types.Message):
    await message.answer("Mahsulot miqdorini tanlang")
    await message.answer_photo(photo=open('images/chizburger.jpg', 'rb'), caption="""
Chizburger 
Burger bulochkasi, tuzlangan bodring, pomidor, go'shtli Patti, qizil piyoz, aysberg, Burger sousi, Xoxland pishlog'i
 

Chizburger 28 000 x 1 = 28 000
Umumiy: 28 000 UZS""", reply_markup=Chizburger)


@dp.callback_query_handler(text='pluschizburger')
async def pluschiz(call: types.CallbackQuery):
    print(sonChizburger)
    sonChizburger['count'] += 1

    Chizburger = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minuschizburger"),
                InlineKeyboardButton(text=str(sonBigburger['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="pluschizburger")
            ],
            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ]
        ]
    )

    summachizburger = 28000 * sonBigburger['count']
    new_caption = f"""
Chizburger 
Burger bulochkasi, tuzlangan bodring, pomidor, go'shtli Patti, qizil piyoz, aysberg, Burger sousi, Xoxland pishlog'i


Chizburger 28 000 x  {sonBigburger['count']} = {summachizburger}
Umumiy: {summachizburger} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/chizburger.jpg', 'rb'), chat_id=call.message.chat.id,
                                    message_id=call.message.message_id, caption=new_caption
                                    ), reply_markup=Chizburger,
    )


@dp.callback_query_handler(text='minuschizburger')
async def minuschiz(call: types.CallbackQuery):
    print(sonBigburger)

    if sonBigburger['count'] > 1:
        sonBigburger['count'] -= 1

        Chizburger = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="minuschizburger"),
                    InlineKeyboardButton(text=str(sonBigburger['count']), callback_data='0'),
                    InlineKeyboardButton(text='+', callback_data="pluschizburger")
                ],

                [
                    InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
                ]
            ]
        )

        summachizburger = 28000 * sonBigburger['count']
        new_caption = f"""
Chizburger 
Burger bulochkasi, tuzlangan bodring, pomidor, go'shtli Patti, qizil piyoz, aysberg, Burger sousi, Xoxland pishlog'i


Chizburger 28 000 x  {sonChizburger['count']} = {summachizburger}
Umumiy: {summachizburger} UZS"""

        await call.message.edit_media(
            media=types.InputMediaPhoto(open('images/chizburger.jpg', 'rb'), caption=new_caption),
            reply_markup=Chizburger
        )
    else:
        await call.answer("1dan kam mahsulot tanlash mumkin emas")


#-----------------------------------------------------------------------------------------------------------------------


sonBigburger = {
    'count': 1,
}


@dp.message_handler(text="Bigburger")
async def bigburger(message: types.Message):
    await message.answer("Mahsulot miqdorini tanlang")
    await message.answer_photo(photo=open('images/bigburger.jpg', 'rb'), caption="""
Bigburger 
Burger bulochkasi, tuzlangan bodring, pomidor, 2 ta go'shtli Patti, qizil piyoz, aysberg, Burger sousi, Xoxland pishloq
 

Bigburger 40 000 x 1 = 40 000
Umumiy: 40 000 UZS""", reply_markup=Bigburger)


@dp.callback_query_handler(text='plusbigburger')
async def plusbigburger(call: types.CallbackQuery):
    print(sonBigburger)
    sonBigburger['count'] += 1

    Bigburger = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minusbigburger"),
                InlineKeyboardButton(text=str(sonBigburger['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plusbigburger")
            ],
            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ]
        ]
    )

    summabigburger = 40000 * sonBigburger['count']
    new_caption = f"""
Bigburger 
Burger bulochkasi, tuzlangan bodring, pomidor, 2 ta go'shtli Patti, qizil piyoz, aysberg, Burger sousi, Xoxland pishloq


Bigburger 40 000 x  {sonBigburger['count']} = {summabigburger}
Umumiy: {summabigburger} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/bigburger.jpg', 'rb'), chat_id=call.message.chat.id,
                                    message_id=call.message.message_id, caption=new_caption
                                    ), reply_markup=Bigburger,
    )


@dp.callback_query_handler(text='minusbigburger')
async def minusburger(call: types.CallbackQuery):
    print(sonBigburger)

    if sonBigburger['count'] > 1:
        sonBigburger['count'] -= 1

        Bigburger = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="minusbigburger"),
                    InlineKeyboardButton(text=str(sonBigburger['count']), callback_data='0'),
                    InlineKeyboardButton(text='+', callback_data="plusbigburger")
                ],

                [
                    InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
                ]
            ]
        )

        summabigburger = 40000 * sonBigburger['count']
        new_caption = f"""
Bigburger 
Burger bulochkasi, tuzlangan bodring, pomidor, 2 ta go'shtli Patti, qizil piyoz, aysberg, Burger sousi, Xoxland pishloq


Bigburger 40 000 x  {sonBigburger['count']} = {summabigburger}
Umumiy: {summabigburger} UZS"""

        await call.message.edit_media(
            media=types.InputMediaPhoto(open('images/bigburger.jpg', 'rb'), caption=new_caption),
            reply_markup=Bigburger
        )
    else:
        await call.answer("1dan kam mahsulot tanlash mumkin emas")