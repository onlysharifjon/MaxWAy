from loader import dp
from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.inline_buttons import Guruch,Salat

sonGuruch = {
    'count': 1,
}


@dp.message_handler(text="Guruch")
async def guruch(message: types.Message):
    await message.answer("Mahsulot miqdorini tanlang")
    await message.answer_photo(photo=open('images/guruch.jpg', 'rb'), caption="""
Guruch 
Shirin makkajo'xori bilan pishirilgan lazer guruch
 

Guruch 7 000 x 1 = 7 000
Umumiy: 7 000 UZS""", reply_markup=Guruch)


@dp.callback_query_handler(text='plusguruch')
async def plusGuruch(call: types.CallbackQuery):
    print(sonGuruch)
    sonGuruch['count'] += 1

    Guruch = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minusguruch"),
                InlineKeyboardButton(text=str(sonGuruch['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plusguruch")
            ],
            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ]
        ]
    )

    summaguruch = 7000 * sonGuruch['count']
    new_caption = f"""
Guruch 
Shirin makkajo'xori bilan pishirilgan lazer guruch 


Guruch 7 000 x {sonGuruch['count']} = {summaguruch}
Umumiy: {summaguruch} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/guruch.jpg', 'rb'), chat_id=call.message.chat.id,
                                    message_id=call.message.message_id, caption=new_caption
                                    ), reply_markup=Guruch,
    )


@dp.callback_query_handler(text='minusguruch')
async def minusGuruch(call: types.CallbackQuery):
    print(sonGuruch)

    if sonGuruch['count'] > 1:
        sonGuruch['count'] -= 1

        Guruch = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="minusguruch"),
                    InlineKeyboardButton(text=str(sonGuruch['count']), callback_data='0'),
                    InlineKeyboardButton(text='+', callback_data="plusguruch")
                ],

                [
                    InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
                ]
            ]
        )

        summaguruch = 7000 * sonGuruch['count']
        new_caption = f"""
Guruch 
Shirin makkajo'xori bilan pishirilgan lazer guruch


Guruch 7 000 x {sonGuruch['count']} = {summaguruch}
Umumiy: {summaguruch} UZS"""

        await call.message.edit_media(
            media=types.InputMediaPhoto(open('images/guruch.jpg', 'rb'), caption=new_caption),
            reply_markup=Guruch
        )
    else:
        await call.answer("1dan kam mahsulot tanlash mumkin emas")


#-----------------------------------------------------------------------------------------------------------------------

sonSalat = {
    'count': 1,
}


@dp.message_handler(text="Salat")
async def salat(message: types.Message):
    await message.answer("Mahsulot miqdorini tanlang")
    await message.answer_photo(photo=open('images/salat.jpg', 'rb'), caption="""
Salat 
Salat qizil karam aralashmasi
 

Salat 7 000 x 1 = 7 000
Umumiy: 7 000 UZS""", reply_markup=Salat)


@dp.callback_query_handler(text='plussalat')
async def plusSalat(call: types.CallbackQuery):
    print(sonSalat)
    sonSalat['count'] += 1

    Salat = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minussalat"),
                InlineKeyboardButton(text=str(sonSalat['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plussalat")
            ],
            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ]
        ]
    )

    summasalat = 7000 * sonSalat['count']
    new_caption = f"""
Salat 
Salat qizil karam aralashmasi 


Salat 7 000 x {sonSalat['count']} = {summasalat}
Umumiy: {summasalat} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/salat.jpg', 'rb'), chat_id=call.message.chat.id,
                                    message_id=call.message.message_id, caption=new_caption
                                    ), reply_markup=Salat,
    )


@dp.callback_query_handler(text='minussalat')
async def minusSalat(call: types.CallbackQuery):
    print(sonSalat)

    if sonSalat['count'] > 1:
        sonSalat['count'] -= 1

        Salat = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="minussalat"),
                    InlineKeyboardButton(text=str(sonSalat['count']), callback_data='0'),
                    InlineKeyboardButton(text='+', callback_data="plussalat")
                ],

                [
                    InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
                ]
            ]
        )

        summasalat = 7000 * sonSalat['count']
        new_caption = f"""
Salat 
Salat qizil karam aralashmasi


Salat 7 000 x {sonSalat['count']} = {summasalat}
Umumiy: {summasalat} UZS"""

        await call.message.edit_media(
            media=types.InputMediaPhoto(open('images/salat.jpg', 'rb'), caption=new_caption),
            reply_markup=Salat
        )
    else:
        await call.answer("1dan kam mahsulot tanlash mumkin emas")
