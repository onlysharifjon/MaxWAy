from loader import dp
from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.inline_buttons import Tiramisu,Brauni,Sansebastian,Yongoqlidonat,Karamel_donat,Qulupnayli_donat

sonTiramisu = {
    'count': 1,
}


@dp.message_handler(text="Tiramisu")
async def tiramisu(message: types.Message):
    await message.answer("Mahsulot miqdorini tanlang")
    await message.answer_photo(photo=open('images/tiramisu.jpg', 'rb'), caption="""
Tiramisu 
Savoyardi pechene, mascarpone, qahva
 

Tiramisu 22 000 x 1 = 22 000
Umumiy: 22 000 UZS""", reply_markup=Tiramisu)


@dp.callback_query_handler(text='plustiramisu')
async def plusTiramisu(call: types.CallbackQuery):
    print(sonTiramisu)
    sonTiramisu['count'] += 1

    Tiramisu = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minustiramisu"),
                InlineKeyboardButton(text=str(sonTiramisu['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plustiramisu")
            ],
            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ]
        ]
    )

    summatiramisu = 22000 * sonTiramisu['count']
    new_caption = f"""
Tiramisu 
Savoyardi pechene, mascarpone, qahva 


Tiramisu 22 000 x {sonTiramisu['count']} = {summatiramisu}
Umumiy: {summatiramisu} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/tiramisu.jpg', 'rb'), chat_id=call.message.chat.id,
                                    message_id=call.message.message_id, caption=new_caption
                                    ), reply_markup=Tiramisu,
    )


@dp.callback_query_handler(text='minustiramisu')
async def minusTiramisu(call: types.CallbackQuery):
    print(sonTiramisu)

    if sonTiramisu['count'] > 1:
        sonTiramisu['count'] -= 1

        Tiramisu = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="minustiramisu"),
                    InlineKeyboardButton(text=str(sonTiramisu['count']), callback_data='0'),
                    InlineKeyboardButton(text='+', callback_data="plustiramisu")
                ],

                [
                    InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
                ]
            ]
        )

        summatiramisu = 22000 * sonTiramisu['count']
        new_caption = f"""
Tiramisu 
Savoyardi pechene, mascarpone, qahva


Tiramisu 22 000 x {sonTiramisu['count']} = {summatiramisu}
Umumiy: {summatiramisu} UZS"""

        await call.message.edit_media(
            media=types.InputMediaPhoto(open('images/tiramisu.jpg', 'rb'), caption=new_caption),
            reply_markup=Tiramisu
        )
    else:
        await call.answer("1dan kam mahsulot tanlash mumkin emas")


#-----------------------------------------------------------------------------------------------------------------------

sonBrauni = {
    'count': 1,
}


@dp.message_handler(text="Brauni")
async def brauni(message: types.Message):
    await message.answer("Mahsulot miqdorini tanlang")
    await message.answer_photo(photo=open('images/brauni.jpg', 'rb'), caption="""
Brauni 
Qora shokolad, yong'oq va shokoladli pechene
 

Brauni 22 000 x 1 = 22 000
Umumiy: 22 000 UZS""", reply_markup=Brauni)


@dp.callback_query_handler(text='plusbrauni')
async def plusBrauni(call: types.CallbackQuery):
    print(sonBrauni)
    sonBrauni['count'] += 1

    Brauni = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minusbrauni"),
                InlineKeyboardButton(text=str(sonBrauni['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plusbrauni")
            ],
            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ]
        ]
    )

    summabrauni = 22000 * sonBrauni['count']
    new_caption = f"""
Brauni 
Qora shokolad, yong'oq va shokoladli pechene 


Brauni 22 000 x {sonBrauni['count']} = {summabrauni}
Umumiy: {summabrauni} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/brauni.jpg', 'rb'), chat_id=call.message.chat.id,
                                    message_id=call.message.message_id, caption=new_caption
                                    ), reply_markup=Brauni,
    )


@dp.callback_query_handler(text='minusbrauni')
async def minusBrauni(call: types.CallbackQuery):
    print(sonBrauni)

    if sonBrauni['count'] > 1:
        sonBrauni['count'] -= 1

        Brauni = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="minusbrauni"),
                    InlineKeyboardButton(text=str(sonBrauni['count']), callback_data='0'),
                    InlineKeyboardButton(text='+', callback_data="plusbrauni")
                ],

                [
                    InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
                ]
            ]
        )

        summabrauni = 22000 * sonBrauni['count']
        new_caption = f"""
Brauni 
Qora shokolad, yong'oq va shokoladli pechene


Brauni 22 000 x {sonBrauni['count']} = {summabrauni}
Umumiy: {summabrauni} UZS"""

        await call.message.edit_media(
            media=types.InputMediaPhoto(open('images/brauni.jpg', 'rb'), caption=new_caption),
            reply_markup=Brauni
        )
    else:
        await call.answer("1dan kam mahsulot tanlash mumkin emas")

#-----------------------------------------------------------------------------------------------------------------------

sonSansebastian = {
    'count': 1,
}


@dp.message_handler(text="San-sebastian")
async def sansebastian(message: types.Message):
    await message.answer("Mahsulot miqdorini tanlang")
    await message.answer_photo(photo=open('images/san_sebastian.jpg', 'rb'), caption="""
San-sebastian 
Savoyardi kukilari, mascarpone, kahva


San-sebastian 22 000 x 1 = 22 000
Umumiy: 22 000 UZS""", reply_markup=Sansebastian)


@dp.callback_query_handler(text='plussansebastian')
async def plusSansebastian(call: types.CallbackQuery):
    print(sonSansebastian)
    sonSansebastian['count'] += 1

    Sansebastian = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minussansebastian"),
                InlineKeyboardButton(text=str(sonSansebastian['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plussansebastian")
            ],
            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ]
        ]
    )

    summasansebastian = 22000 * sonSansebastian['count']
    new_caption = f"""
San-sebastian 
Savoyardi kukilari, mascarpone, kahva 


San-sebastian 22 000 x {sonSansebastian['count']} = {summasansebastian}
Umumiy: {summasansebastian} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/san_sebastian.jpg', 'rb'), chat_id=call.message.chat.id,
                                    message_id=call.message.message_id, caption=new_caption
                                    ), reply_markup=Sansebastian,
    )


@dp.callback_query_handler(text='minussansebastian')
async def minusSansebastian(call: types.CallbackQuery):
    print(sonSansebastian)

    if sonSansebastian['count'] > 1:
        sonSansebastian['count'] -= 1

        Sansebastian = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="minussansebastian"),
                    InlineKeyboardButton(text=str(sonSansebastian['count']), callback_data='0'),
                    InlineKeyboardButton(text='+', callback_data="plussansebastian")
                ],

                [
                    InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
                ]
            ]
        )

        summasansebastian = 22000 * sonSansebastian['count']
        new_caption = f"""
San-sebastian 
Savoyardi kukilari, mascarpone, kahva


San-sebastian 22 000 x {sonSansebastian['count']} = {summasansebastian}
Umumiy: {summasansebastian} UZS"""

        await call.message.edit_media(
            media=types.InputMediaPhoto(open('images/san_sebastian.jpg', 'rb'), caption=new_caption),
            reply_markup=Sansebastian
        )
    else:
        await call.answer("1dan kam mahsulot tanlash mumkin emas")


#-----------------------------------------------------------------------------------------------------------------------

sonYongoqlidonat = {
    'count': 1,
}


@dp.message_handler(text="Yo'ng'oqli donat")
async def yongoqlidonat(message: types.Message):
    await message.answer("Mahsulot miqdorini tanlang")
    await message.answer_photo(photo=open('images/yongoqlidonat.jpg', 'rb'), caption="""
Yo'ng'oqli donat 
  

Yo'ng'oqli donat 16 000 x 1 = 16 000
Umumiy: 16 000 UZS""", reply_markup=Yongoqlidonat)


@dp.callback_query_handler(text='plusyongoqlidonat')
async def plusYongoqlidonatn(call: types.CallbackQuery):
    print(sonYongoqlidonat)
    sonYongoqlidonat['count'] += 1

    Yongoqlidonat = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minusyongoqlidonat"),
                InlineKeyboardButton(text=str(sonYongoqlidonat['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plusyongoqlidonat")
            ],
            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ]
        ]
    )

    summayongoqlidonat= 16000 * sonYongoqlidonat['count']
    new_caption = f"""
Yo'ng'oqli donat 


Yo'ng'oqli donat 16 000 x {sonYongoqlidonat['count']} = {summayongoqlidonat}
Umumiy: {summayongoqlidonat} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/yongoqlidonat.jpg', 'rb'), chat_id=call.message.chat.id,
                                    message_id=call.message.message_id, caption=new_caption
                                    ), reply_markup=Yongoqlidonat,
    )


@dp.callback_query_handler(text='minusyongoqlidonat')
async def minusYongoqlidonat(call: types.CallbackQuery):
    print(sonYongoqlidonat)

    if sonYongoqlidonat['count'] > 1:
        sonYongoqlidonat['count'] -= 1

        Yongoqlidonat = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="minusyongoqlidonat"),
                    InlineKeyboardButton(text=str(sonYongoqlidonat['count']), callback_data='0'),
                    InlineKeyboardButton(text='+', callback_data="plusyongoqlidonat")
                ],

                [
                    InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
                ]
            ]
        )

        summayongoqlidonat = 16000 * sonYongoqlidonat['count']
        new_caption = f"""
Yo'ng'oqli donat


Yo'ng'oqli donat 16 000 x {sonYongoqlidonat['count']} = {summayongoqlidonat}
Umumiy: {summayongoqlidonat} UZS"""

        await call.message.edit_media(
            media=types.InputMediaPhoto(open('images/yongoqlidonat.jpg', 'rb'), caption=new_caption),
            reply_markup=Yongoqlidonat
        )
    else:
        await call.answer("1dan kam mahsulot tanlash mumkin emas")


#-----------------------------------------------------------------------------------------------------------------------


sonKarameldonat = {
    'count': 1,
}


@dp.message_handler(text="Karamel donat")
async def karameldonat(message: types.Message):
    await message.answer("Mahsulot miqdorini tanlang")
    await message.answer_photo(photo=open('images/karameldonat.jpg', 'rb'), caption="""
Karamel donat 
  

Karamel donat 16 000 x 1 = 16 000
Umumiy: 16 000 UZS""", reply_markup=Karamel_donat)


@dp.callback_query_handler(text='pluskarameldonat')
async def plusKarameldonat(call: types.CallbackQuery):
    print(sonKarameldonat)
    sonKarameldonat['count'] += 1

    Karamel_donat = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minuskarameldonat"),
                InlineKeyboardButton(text=str(sonKarameldonat['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="pluskarameldonat")
            ],
            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ]
        ]
    )

    summakarameldonat = 16000 * sonKarameldonat['count']
    new_caption = f"""
Karamel donat 


Karamel donat 16 000 x {sonKarameldonat['count']} = {summakarameldonat}
Umumiy: {summakarameldonat} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/karameldonat.jpg', 'rb'), chat_id=call.message.chat.id,
                                    message_id=call.message.message_id, caption=new_caption
                                    ), reply_markup=Karamel_donat,
    )


@dp.callback_query_handler(text='minuskarameldonat')
async def minusKarameldonat(call: types.CallbackQuery):
    print(sonKarameldonat)

    if sonKarameldonat['count'] > 1:
        sonKarameldonat['count'] -= 1

        Karamel_donat = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="minuskarameldonat"),
                    InlineKeyboardButton(text=str(sonKarameldonat['count']), callback_data='0'),
                    InlineKeyboardButton(text='+', callback_data="pluskarameldonat")
                ],

                [
                    InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
                ]
            ]
        )

        summakarameldonat = 16000 * sonKarameldonat['count']
        new_caption = f"""
Karamel donat


Karamel donat 16 000 x {sonKarameldonat['count']} = {summakarameldonat}
Umumiy: {summakarameldonat} UZS"""

        await call.message.edit_media(
            media=types.InputMediaPhoto(open('images/karameldonat.jpg', 'rb'), caption=new_caption),
            reply_markup=Karamel_donat
        )
    else:
        await call.answer("1dan kam mahsulot tanlash mumkin emas")


#-----------------------------------------------------------------------------------------------------------------------


sonQulupnaylidonat = {
    'count': 1,
}


@dp.message_handler(text="Qulupnayli donat")
async def qulupnaylidonat(message: types.Message):
    await message.answer("Mahsulot miqdorini tanlang")
    await message.answer_photo(photo=open('images/qulupnaylidonat.jpg', 'rb'), caption="""
Qulupnayli donat 
  

Qulupnayli donat 16 000 x 1 = 16 000
Umumiy: 16 000 UZS""", reply_markup=Qulupnayli_donat)


@dp.callback_query_handler(text='plusqulupnaylidonat')
async def plusQulupnaylidonat(call: types.CallbackQuery):
    print(sonQulupnaylidonat)
    sonQulupnaylidonat['count'] += 1

    Qulupnayli_donat = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minusqulupnaylidonat"),
                InlineKeyboardButton(text=str(sonQulupnaylidonat['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plusqulupnaylidonat")
            ],
            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ]
        ]
    )

    summaqulupnaylidonat = 16000 * sonQulupnaylidonat['count']
    new_caption = f"""
Qulupnayli donat 


Qulupnayli donat 16 000 x {sonQulupnaylidonat['count']} = {summaqulupnaylidonat}
Umumiy: {summaqulupnaylidonat} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/qulupnaylidonat.jpg', 'rb'), chat_id=call.message.chat.id,
                                    message_id=call.message.message_id, caption=new_caption
                                    ), reply_markup=Qulupnayli_donat,
    )


@dp.callback_query_handler(text='minusqulupnaylidonat')
async def minusQulupnaylidonat(call: types.CallbackQuery):
    print(sonQulupnaylidonat)

    if sonQulupnaylidonat['count'] > 1:
        sonQulupnaylidonat['count'] -= 1

        Qulupnayli_donat = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="minusqulupnaylidonat"),
                    InlineKeyboardButton(text=str(sonQulupnaylidonat['count']), callback_data='0'),
                    InlineKeyboardButton(text='+', callback_data="plusqulupnaylidonat")
                ],

                [
                    InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
                ]
            ]
        )

        summaqulupnaylidonat = 16000 * sonQulupnaylidonat['count']
        new_caption = f"""
Qulupnayli donat


Qulupnayli donat 16 000 x {sonQulupnaylidonat['count']} = {summaqulupnaylidonat}
Umumiy: {summaqulupnaylidonat} UZS"""

        await call.message.edit_media(
            media=types.InputMediaPhoto(open('images/qulupnaylidonat.jpg', 'rb'), caption=new_caption),
            reply_markup=Qulupnayli_donat
        )
    else:
        await call.answer("1dan kam mahsulot tanlash mumkin emas")