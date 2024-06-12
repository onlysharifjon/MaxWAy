from loader import dp
from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.inline_buttons import Fri_katta,Fri_standart,Fri_mini,Po_derevenski,Naggets_box,Mix_box

sonFrikatta = {
    'count': 1,
}


@dp.message_handler(text="Kartoshka fri katta")
async def frikatta(message: types.Message):
    await message.answer("Mahsulot miqdorini tanlang")
    await message.answer_photo(photo=open('images/kartoshkafrikatta.jpg', 'rb'), caption="""
Kartoshka fri katta 
  

Kartoshka fri katta 18 000 x 1 = 18 000
Umumiy: 18 000 UZS""", reply_markup=Fri_katta)


@dp.callback_query_handler(text='plusfrikatta')
async def plusFrikatta(call: types.CallbackQuery):
    print(sonFrikatta)
    sonFrikatta['count'] += 1

    Fri_katta = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minusfrikatta"),
                InlineKeyboardButton(text=str(sonFrikatta['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plusfrikatta")
            ],
            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ]
        ]
    )

    summafrikatta = 18000 * sonFrikatta['count']
    new_caption = f"""
Kartoshka fri katta 


Kartoshka fri katta 18 000 x {sonFrikatta['count']} = {summafrikatta}
Umumiy: {summafrikatta} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/kartoshkafrikatta.jpg', 'rb'), chat_id=call.message.chat.id,
                                    message_id=call.message.message_id, caption=new_caption
                                    ), reply_markup=Fri_katta,
    )


@dp.callback_query_handler(text='minusfrikatta')
async def minusFrikatta(call: types.CallbackQuery):
    print(sonFrikatta)

    if sonFrikatta['count'] > 1:
        sonFrikatta['count'] -= 1

        Fri_katta = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="minusfrikatta"),
                    InlineKeyboardButton(text=str(sonFrikatta['count']), callback_data='0'),
                    InlineKeyboardButton(text='+', callback_data="plusfrikatta")
                ],

                [
                    InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
                ]
            ]
        )

        summafrikatta = 18000 * sonFrikatta['count']
        new_caption = f"""
Kartoshka fri katta 


Kartoshka fri katta 18 000 x {sonFrikatta['count']} = {summafrikatta}
Umumiy: {summafrikatta} UZS"""

        await call.message.edit_media(
            media=types.InputMediaPhoto(open('images/kartoshkafrikatta.jpg', 'rb'), caption=new_caption),
            reply_markup=Fri_katta
        )
    else:
        await call.answer("1dan kam mahsulot tanlash mumkin emas")

#-----------------------------------------------------------------------------------------------------------------------


sonFristandart = {
    'count': 1,
}


@dp.message_handler(text="Kartoshka fri  standart")
async def fristandart(message: types.Message):
    await message.answer("Mahsulot miqdorini tanlang")
    await message.answer_photo(photo=open('images/kartoshkafristandart.jpg', 'rb'), caption="""
Kartoshka fri  standart 
  

Kartoshka fri  standart 14 000 x 1 = 14 000
Umumiy: 14 000 UZS""", reply_markup=Fri_standart)


@dp.callback_query_handler(text='plusfristandart')
async def plusFristandart(call: types.CallbackQuery):
    print(sonFristandart)
    sonFristandart['count'] += 1

    Fri_standart = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minusfristandart"),
                InlineKeyboardButton(text=str(sonFristandart['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plusfristandart")
            ],
            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ]
        ]
    )

    summafristandart = 14000 * sonFristandart['count']
    new_caption = f"""
Kartoshka fri  standart 


Kartoshka fri  standart 14 000 x {sonFristandart['count']} = {summafristandart}
Umumiy: {summafristandart} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/kartoshkafristandart.jpg', 'rb'), chat_id=call.message.chat.id,
                                    message_id=call.message.message_id, caption=new_caption
                                    ), reply_markup=Fri_standart,
    )


@dp.callback_query_handler(text='minusfristandart')
async def minusFristandart(call: types.CallbackQuery):
    print(sonFristandart)

    if sonFristandart['count'] > 1:
        sonFristandart['count'] -= 1

        Fri_standart = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="minusfristandart"),
                    InlineKeyboardButton(text=str(sonFristandart['count']), callback_data='0'),
                    InlineKeyboardButton(text='+', callback_data="plusfristandart")
                ],

                [
                    InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
                ]
            ]
        )

        summafristandart = 14000 * sonFristandart['count']
        new_caption = f"""
Kartoshka fri  standart 


Kartoshka fri  standart 14 000 x {sonFristandart['count']} = {summafristandart}
Umumiy: {summafristandart} UZS"""

        await call.message.edit_media(
            media=types.InputMediaPhoto(open('images/kartoshkafristandart.jpg', 'rb'), caption=new_caption),
            reply_markup=Fri_standart
        )
    else:
        await call.answer("1dan kam mahsulot tanlash mumkin emas")


#-----------------------------------------------------------------------------------------------------------------------


sonFrimini = {
    'count': 1,
}


@dp.message_handler(text="Kartoshka fri  mini")
async def frimini(message: types.Message):
    await message.answer("Mahsulot miqdorini tanlang")
    await message.answer_photo(photo=open('images/kartoshkafirimini.jpg', 'rb'), caption="""
Kartoshka fri  mini 
  

Kartoshka fri  mini 9 000 x 1 = 9 000
Umumiy: 9 000 UZS""", reply_markup=Fri_mini)


@dp.callback_query_handler(text='plusfrimini')
async def plusFrimini(call: types.CallbackQuery):
    print(sonFrimini)
    sonFrimini['count'] += 1

    Fri_mini = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minusfrimini"),
                InlineKeyboardButton(text=str(sonFrimini['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plusfrimini")
            ],
            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ]
        ]
    )

    summafrimini = 9000 * sonFrimini['count']
    new_caption = f"""
Kartoshka fri  mini 


Kartoshka fri  mini 9 000 x {sonFrimini['count']} = {summafrimini}
Umumiy: {summafrimini} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/kartoshkafirimini.jpg', 'rb'), chat_id=call.message.chat.id,
                                    message_id=call.message.message_id, caption=new_caption
                                    ), reply_markup=Fri_mini,
    )


@dp.callback_query_handler(text='minusfrimini')
async def minusFrimini(call: types.CallbackQuery):
    print(sonFrimini)

    if sonFrimini['count'] > 1:
        sonFrimini['count'] -= 1

        Fri_mini = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="minusfrimini"),
                    InlineKeyboardButton(text=str(sonFrimini['count']), callback_data='0'),
                    InlineKeyboardButton(text='+', callback_data="plusfrimini")
                ],

                [
                    InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
                ]
            ]
        )

        summafrimini = 9000 * sonFrimini['count']
        new_caption = f"""
Kartoshka fri  mini 


Kartoshka fri  mini 9 000 x {sonFrimini['count']} = {summafrimini}
Umumiy: {summafrimini} UZS"""

        await call.message.edit_media(
            media=types.InputMediaPhoto(open('images/kartoshkafirimini.jpg', 'rb'), caption=new_caption),
            reply_markup=Fri_mini
        )
    else:
        await call.answer("1dan kam mahsulot tanlash mumkin emas")


#-----------------------------------------------------------------------------------------------------------------------


sonPoderevenski = {
    'count': 1,
}


@dp.message_handler(text="Po derevenski")
async def frimini(message: types.Message):
    await message.answer("Mahsulot miqdorini tanlang")
    await message.answer_photo(photo=open('images/poderevenski.jpg', 'rb'), caption="""
Po derevenski 
   

Po derevenski 15 000 x 1 = 15 000
Umumiy: 15 000 UZS""", reply_markup=Po_derevenski)


@dp.callback_query_handler(text='pluspoderevenski')
async def plusPoderevenski(call: types.CallbackQuery):
    print(sonPoderevenski)
    sonPoderevenski['count'] += 1

    Po_derevenski = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minuspoderevenski"),
                InlineKeyboardButton(text=str(sonPoderevenski['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="pluspoderevenski")
            ],
            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ]
        ]
    )

    summapoderevenski = 15000 * sonPoderevenski['count']
    new_caption = f"""
Po derevenski 


Po derevenski 15 000 x  {sonPoderevenski['count']} = {summapoderevenski}
Umumiy: {summapoderevenski} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/poderevenski.jpg', 'rb'), chat_id=call.message.chat.id,
                                    message_id=call.message.message_id, caption=new_caption
                                    ), reply_markup=Po_derevenski,
    )


@dp.callback_query_handler(text='minuspoderevenski')
async def minusPoderevenski(call: types.CallbackQuery):
    print(sonPoderevenski)

    if sonPoderevenski['count'] > 1:
        sonPoderevenski['count'] -= 1

        Po_derevenski = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="minuspoderevenski"),
                    InlineKeyboardButton(text=str(sonPoderevenski['count']), callback_data='0'),
                    InlineKeyboardButton(text='+', callback_data="pluspoderevenski")
                ],

                [
                    InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
                ]
            ]
        )

        summapoderevenski = 15000 * sonPoderevenski['count']
        new_caption = f"""
Po derevenski 


Po derevenski 15 000 x  {sonPoderevenski['count']} = {summapoderevenski}
Umumiy: {summapoderevenski} UZS"""

        await call.message.edit_media(
            media=types.InputMediaPhoto(open('images/poderevenski.jpg', 'rb'), caption=new_caption),
            reply_markup=Po_derevenski
        )
    else:
        await call.answer("1dan kam mahsulot tanlash mumkin emas")


#-----------------------------------------------------------------------------------------------------------------------


sonNaggetsbox = {
    'count': 1,
}


@dp.message_handler(text="Naggets BOX")
async def naggetsbox(message: types.Message):
    await message.answer("Mahsulot miqdorini tanlang")
    await message.answer_photo(photo=open('images/naggetsbox.jpg', 'rb'), caption="""
Naggets BOX 
naggetslar (5 dona), kartoshka fri (100 gr) 

Naggets BOX 22 000 x 1 = 22 000
Umumiy: 22 000 UZS""", reply_markup=Naggets_box)


@dp.callback_query_handler(text='plusnaggetsbox')
async def plusNaggetsbox(call: types.CallbackQuery):
    print(sonNaggetsbox)
    sonNaggetsbox['count'] += 1

    Naggets_box = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minusnaggetsbox"),
                InlineKeyboardButton(text=str(sonNaggetsbox['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plusnaggetsbox")
            ],
            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ]
        ]
    )

    summanaggetsbox = 22000 * sonNaggetsbox['count']
    new_caption = f"""
Naggets BOX 
naggetslar (5 dona), kartoshka fri (100 gr)

Naggets BOX 22 000 x  {sonNaggetsbox['count']} = {summanaggetsbox}
Umumiy: {summanaggetsbox} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/naggetsbox.jpg', 'rb'), chat_id=call.message.chat.id,
                                    message_id=call.message.message_id, caption=new_caption
                                    ), reply_markup=Naggets_box,
    )


@dp.callback_query_handler(text='minusnaggetsbox')
async def minusNaggetsbox(call: types.CallbackQuery):
    print(sonNaggetsbox)

    if sonNaggetsbox['count'] > 1:
        sonNaggetsbox['count'] -= 1

        Naggets_box = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="minusnaggetsbox"),
                    InlineKeyboardButton(text=str(sonNaggetsbox['count']), callback_data='0'),
                    InlineKeyboardButton(text='+', callback_data="plusnaggetsbox")
                ],

                [
                    InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
                ]
            ]
        )

        summanaggetsbox = 22000 * sonNaggetsbox['count']
        new_caption = f"""
Naggets BOX 
naggetslar (5 dona), kartoshka fri (100 gr)

Naggets BOX 22 000 x {sonNaggetsbox['count']} = {summanaggetsbox}
Umumiy: {summanaggetsbox} UZS"""

        await call.message.edit_media(
            media=types.InputMediaPhoto(open('images/naggetsbox.jpg', 'rb'), caption=new_caption),
            reply_markup=Naggets_box
        )
    else:
        await call.answer("1dan kam mahsulot tanlash mumkin emas")


#-----------------------------------------------------------------------------------------------------------------------

sonMixbox = {
    'count': 1,
}


@dp.message_handler(text="Mix Box")
async def naggetsbox(message: types.Message):
    await message.answer("Mahsulot miqdorini tanlang")
    await message.answer_photo(photo=open('images/mixbox.jpg', 'rb'), caption="""
Mix Box 
kartoshka fri 60 g, naggetslar 4 dona, stripslar 2 dona    

Mix Box 27 000 x 1 = 27 000
Umumiy: 27 000 UZS""", reply_markup=Mix_box)


@dp.callback_query_handler(text='plusmixbox')
async def plusMixbox(call: types.CallbackQuery):
    print(sonMixbox)
    sonMixbox['count'] += 1

    Mix_box = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minusmixbox"),
                InlineKeyboardButton(text=str(sonMixbox['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plusmixbox")
            ],
            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ]
        ]
    )

    summamixbox= 27000 * sonMixbox['count']
    new_caption = f"""
Mix Box 
kartoshka fri 60 g, naggetslar 4 dona, stripslar 2 dona

Mix Box 27 000 x  {sonMixbox['count']} = {summamixbox}
Umumiy: {summamixbox} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/mixbox.jpg', 'rb'), chat_id=call.message.chat.id,
                                    message_id=call.message.message_id, caption=new_caption
                                    ), reply_markup=Mix_box,
    )


@dp.callback_query_handler(text='minusmixbox')
async def minusMixbox(call: types.CallbackQuery):
    print(sonMixbox)

    if sonMixbox['count'] > 1:
        sonMixbox['count'] -= 1

        Mix_box = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="minusmixbox"),
                    InlineKeyboardButton(text=str(sonMixbox['count']), callback_data='0'),
                    InlineKeyboardButton(text='+', callback_data="plusmixbox")
                ],

                [
                    InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
                ]
            ]
        )

        summamixbox = 27000 * sonMixbox['count']
        new_caption = f"""
Mix Box 
kartoshka fri 60 g, naggetslar 4 dona, stripslar 2 dona

Mix Box 27 000 x {sonMixbox['count']} = {summamixbox}
Umumiy: {summamixbox} UZS"""

        await call.message.edit_media(
            media=types.InputMediaPhoto(open('images/mixbox.jpg', 'rb'), caption=new_caption),
            reply_markup=Mix_box
        )
    else:
        await call.answer("1dan kam mahsulot tanlash mumkin emas")
