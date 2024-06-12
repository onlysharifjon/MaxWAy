from loader import dp
from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.inline_buttons import Moxito, Ice_tea, Fuse_tea, Bonaqua, Stakan, Qora_choy, Kok_choy, \
    Limonli_choy, Fanta, Amerikano, Kapuchino, Latte

sonMoxito = {
    'count': 1,
}


@dp.message_handler(text="Moxito")
async def moxito(message: types.Message):
    await message.answer("Mahsulot miqdorini tanlang")
    await message.answer_photo(photo=open('images/moxito.jpg', 'rb'), caption="""
Moxito 
   

Moxito 15 000 x 1 = 15 000
Umumiy: 15 000 UZS""", reply_markup=Moxito)


@dp.callback_query_handler(text='plusmoxito')
async def plusMoxito(call: types.CallbackQuery):
    print(sonMoxito)
    sonMoxito['count'] += 1

    Moxito = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minusmoxito"),
                InlineKeyboardButton(text=str(sonMoxito['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plusmoxito")
            ],
            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ]
        ]
    )

    summamoxito= 15000 * sonMoxito['count']
    new_caption = f"""
Moxito


Moxito 15 000 x {sonMoxito['count']} = {summamoxito}
Umumiy: {summamoxito} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/moxito.jpg', 'rb'), chat_id=call.message.chat.id,
                                    message_id=call.message.message_id, caption=new_caption
                                    ), reply_markup=Moxito,
    )


@dp.callback_query_handler(text='minusmoxito')
async def minusMoxito(call: types.CallbackQuery):
    print(sonMoxito)

    if sonMoxito['count'] > 1:
        sonMoxito['count'] -= 1

        Moxito = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="minusmoxito"),
                    InlineKeyboardButton(text=str(sonMoxito['count']), callback_data='0'),
                    InlineKeyboardButton(text='+', callback_data="plusmoxito")
                ],

                [
                    InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
                ]
            ]
        )

        summamoxito = 15000 * sonMoxito['count']
        new_caption = f"""
Moxito


Moxito 15 000 x {sonMoxito['count']} = {summamoxito}
Umumiy: {summamoxito} UZS"""

        await call.message.edit_media(
            media=types.InputMediaPhoto(open('images/moxito.jpg', 'rb'), caption=new_caption),
            reply_markup=Moxito
        )
    else:
        await call.answer("1dan kam mahsulot tanlash mumkin emas")


#-----------------------------------------------------------------------------------------------------------------------4


sonIcetea = {
    'count': 1,
}


@dp.message_handler(text="Ice Tea")
async def icetea(message: types.Message):
    await message.answer("Mahsulot miqdorini tanlang")
    await message.answer_photo(photo=open('images/icetea.jpg', 'rb'), caption="""
Ice Tea 
   

Ice Tea 15 000 x 1 = 15 000
Umumiy: 15 000 UZS""", reply_markup=Ice_tea)


@dp.callback_query_handler(text='plusicetea')
async def plusIcetea(call: types.CallbackQuery):
    print(sonIcetea)
    sonIcetea['count'] += 1

    Ice_tea = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minusicetea"),
                InlineKeyboardButton(text=str(sonIcetea['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plusicetea")
            ],
            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ]
        ]
    )

    summaicetea = 15000 * sonIcetea['count']
    new_caption = f"""
Ice Tea


Ice Tea 15 000 x {sonIcetea['count']} = {summaicetea}
Umumiy: {summaicetea} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/icetea.jpg', 'rb'), chat_id=call.message.chat.id,
                                    message_id=call.message.message_id, caption=new_caption
                                    ), reply_markup=Ice_tea,
    )


@dp.callback_query_handler(text='minusicetea')
async def minusIcetea(call: types.CallbackQuery):
    print(sonIcetea)

    if sonIcetea['count'] > 1:
        sonIcetea['count'] -= 1

        Ice_tea = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="minusicetea"),
                    InlineKeyboardButton(text=str(sonIcetea['count']), callback_data='0'),
                    InlineKeyboardButton(text='+', callback_data="plusicetea")
                ],

                [
                    InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
                ]
            ]
        )

        summaicetea = 15000 * sonIcetea['count']
        new_caption = f"""
Ice Tea


Ice Tea 15 000 x {sonIcetea['count']} = {summaicetea}
Umumiy: {summaicetea} UZS"""

        await call.message.edit_media(
            media=types.InputMediaPhoto(open('images/icetea.jpg', 'rb'), caption=new_caption),
            reply_markup=Ice_tea
        )
    else:
        await call.answer("1dan kam mahsulot tanlash mumkin emas")


#-----------------------------------------------------------------------------------------------------------------------

sonFusetea = {
    'count': 1,
}


@dp.message_handler(text="Fuse Tea")
async def fusetea(message: types.Message):
    await message.answer("Mahsulot miqdorini tanlang")
    await message.answer_photo(photo=open('images/fusetea.jpg', 'rb'), caption="""
Fuse tea 
   

Fuse tea 10 000 x 1 = 10 000
Umumiy: 10 000 UZS""", reply_markup=Fuse_tea)


@dp.callback_query_handler(text='plusfusetea')
async def plusFusetea(call: types.CallbackQuery):
    print(sonFusetea)
    sonFusetea['count'] += 1

    Fuse_tea = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minusfusetea"),
                InlineKeyboardButton(text=str(sonFusetea['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plusfusetea")
            ],
            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ]
        ]
    )

    summafusetea = 10000 * sonFusetea['count']
    new_caption = f"""
Fuse tea


Fuse tea 10 000 x {sonFusetea['count']} = {summafusetea}
Umumiy: {summafusetea} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/fusetea.jpg', 'rb'), chat_id=call.message.chat.id,
                                    message_id=call.message.message_id, caption=new_caption
                                    ), reply_markup=Fuse_tea,
    )


@dp.callback_query_handler(text='minusfusetea')
async def minusfusetea(call: types.CallbackQuery):
    print(sonFusetea)

    if sonFusetea['count'] > 1:
        sonFusetea['count'] -= 1

        Fuse_tea = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="minusfusetea"),
                    InlineKeyboardButton(text=str(sonFusetea['count']), callback_data='0'),
                    InlineKeyboardButton(text='+', callback_data="plusfusetea")
                ],

                [
                    InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
                ]
            ]
        )

        summafusetea = 10000 * sonFusetea['count']
        new_caption = f"""
Fuse tea


Fuse tea 10 000 x {sonFusetea['count']} = {summafusetea}
Umumiy: {summafusetea} UZS"""

        await call.message.edit_media(
            media=types.InputMediaPhoto(open('images/fusetea.jpg', 'rb'), caption=new_caption),
            reply_markup=Fuse_tea
        )
    else:
        await call.answer("1dan kam mahsulot tanlash mumkin emas")


#-----------------------------------------------------------------------------------------------------------------------

sonBonaqua = {
    'count': 1,
}


@dp.message_handler(text="Bonaqua")
async def bonaqua(message: types.Message):
    await message.answer("Mahsulot miqdorini tanlang")
    await message.answer_photo(photo=open('images/bonaqau.jpg', 'rb'), caption="""
Bonaqua 
  

Bonaqua 5 000 x 1 = 5 000
Umumiy: 5 000 UZS""", reply_markup=Bonaqua)


@dp.callback_query_handler(text='plusbonaqua')
async def plusBonaqua(call: types.CallbackQuery):
    print(sonBonaqua)
    sonBonaqua['count'] += 1

    Bonaqua = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minusbonaqua"),
                InlineKeyboardButton(text=str(sonBonaqua['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plusbonaqua")
            ],
            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ]
        ]
    )

    summabonaqua = 5000 * sonBonaqua['count']
    new_caption = f"""
Bonaqua


Bonaqua 5 000 x {sonBonaqua['count']} = {summabonaqua}
Umumiy: {summabonaqua} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/bonaqau.jpg', 'rb'), chat_id=call.message.chat.id,
                                    message_id=call.message.message_id, caption=new_caption
                                    ), reply_markup=Bonaqua,
    )


@dp.callback_query_handler(text='minusbonaqua')
async def minusBonaqua(call: types.CallbackQuery):
    print(sonBonaqua)

    if sonBonaqua['count'] > 1:
        sonBonaqua['count'] -= 1

        Bonaqua = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="minusbonaqua"),
                    InlineKeyboardButton(text=str(sonBonaqua['count']), callback_data='0'),
                    InlineKeyboardButton(text='+', callback_data="plusbonaqua")
                ],

                [
                    InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
                ]
            ]
        )

        summabonaqua = 5000 * sonBonaqua['count']
        new_caption = f"""
Bonaqua


Bonaqua 5 000 x {sonBonaqua['count']} = {summabonaqua}
Umumiy: {summabonaqua} UZS"""

        await call.message.edit_media(
            media=types.InputMediaPhoto(open('images/bonaqau.jpg', 'rb'), caption=new_caption),
            reply_markup=Bonaqua
        )
    else:
        await call.answer("1dan kam mahsulot tanlash mumkin emas")


#-----------------------------------------------------------------------------------------------------------------------


sonstakan = {
    'count': 1,
}


@dp.message_handler(text="Bir martali stakan")
async def stakan(message: types.Message):
    await message.answer("Mahsulot miqdorini tanlang")
    await message.answer_photo(photo=open('images/stakan.jpg', 'rb'), caption="""
Bir martali stakan 
    

Bir martali stakan 1 000 x 1 = 1 000
Umumiy: 1 000 UZS""", reply_markup=Stakan)


@dp.callback_query_handler(text='plusstakan')
async def plusStakan(call: types.CallbackQuery):
    print(sonstakan)
    sonstakan['count'] += 1

    Stakan = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minusstakan"),
                InlineKeyboardButton(text=str(sonstakan['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plusstakan")
            ],
            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ]
        ]
    )

    summastakan = 1000 * sonstakan['count']
    new_caption = f"""
Bir martali stakan


Bir martali stakan 1 000 x {sonstakan['count']} = {summastakan}
Umumiy: {summastakan} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/stakan.jpg', 'rb'), chat_id=call.message.chat.id,
                                    message_id=call.message.message_id, caption=new_caption
                                    ), reply_markup=Stakan,
    )


@dp.callback_query_handler(text='minusstakan')
async def minusStakan(call: types.CallbackQuery):
    print(sonstakan)

    if sonstakan['count'] > 1:
        sonstakan['count'] -= 1

        Stakan = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="minusstakan"),
                    InlineKeyboardButton(text=str(sonstakan['count']), callback_data='0'),
                    InlineKeyboardButton(text='+', callback_data="plusstakan")
                ],

                [
                    InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
                ]
            ]
        )

        summastakan = 1000 * sonstakan['count']
        new_caption = f"""
Bir martali stakan


Bir martali stakan 1 000 x {sonstakan['count']} = {summastakan}
Umumiy: {summastakan} UZS"""

        await call.message.edit_media(
            media=types.InputMediaPhoto(open('images/stakan.jpg', 'rb'), caption=new_caption),
            reply_markup=Stakan
        )
    else:
        await call.answer("1dan kam mahsulot tanlash mumkin emas")

#-----------------------------------------------------------------------------------------------------------------------


sonQorachoy = {
    'count': 1,
}


@dp.message_handler(text="Qora choy")
async def qorachoy(message: types.Message):
    await message.answer("Mahsulot miqdorini tanlang")
    await message.answer_photo(photo=open('images/qorachoy.jpg', 'rb'), caption="""
Qora choy 
Qora choy (ta’bga kora shakar) 

Qora choy 5 000 x 1 = 5 000
Umumiy: 5 000 UZS""", reply_markup=Qora_choy)


@dp.callback_query_handler(text='plusqorachoy')
async def plusQorachoy(call: types.CallbackQuery):
    print(sonQorachoy)
    sonQorachoy['count'] += 1

    Qora_choy = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minusqorachoy"),
                InlineKeyboardButton(text=str(sonQorachoy['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plusqorachoy")
            ],
            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ]
        ]
    )

    summaqorachoy = 5000 * sonQorachoy['count']
    new_caption = f"""
Qora choy 
Qora choy (ta’bga kora shakar)

Qora choy 5 000 x {sonQorachoy['count']} = {summaqorachoy}
Umumiy: {summaqorachoy} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/qorachoy.jpg', 'rb'), chat_id=call.message.chat.id,
                                    message_id=call.message.message_id, caption=new_caption
                                    ), reply_markup=Qora_choy,
    )


@dp.callback_query_handler(text='minusqorachoy')
async def minusQorachoy(call: types.CallbackQuery):
    print(sonQorachoy)

    if sonQorachoy['count'] > 1:
        sonQorachoy['count'] -= 1

        Qora_choy = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="minusqorachoy"),
                    InlineKeyboardButton(text=str(sonQorachoy['count']), callback_data='0'),
                    InlineKeyboardButton(text='+', callback_data="plusqorachoy")
                ],

                [
                    InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
                ]
            ]
        )

        summaqorachoy = 5000 * sonQorachoy['count']
        new_caption = f"""
Qora choy 
Qora choy (ta’bga kora shakar)

Qora choy 5 000 x {sonQorachoy['count']} = {summaqorachoy}
Umumiy: {summaqorachoy} UZS"""

        await call.message.edit_media(
            media=types.InputMediaPhoto(open('images/qorachoy.jpg', 'rb'), caption=new_caption),
            reply_markup=Qora_choy
        )
    else:
        await call.answer("1dan kam mahsulot tanlash mumkin emas")

#-----------------------------------------------------------------------------------------------------------------------


sonKokchoy = {
    'count': 1,
}


@dp.message_handler(text="Ko'k choy")
async def kokchoy(message: types.Message):
    await message.answer("Mahsulot miqdorini tanlang")
    await message.answer_photo(photo=open('images/kokchoy.jpg', 'rb'), caption="""
Ko'k choy 
Ko’k choy (ta’bga kora shakar) 

Ko'k choy 5 000 x 1 = 5 000
Umumiy: 5 000 UZS""", reply_markup=Kok_choy)


@dp.callback_query_handler(text='pluskokchoy')
async def plusKokchoy(call: types.CallbackQuery):
    print(sonKokchoy)
    sonKokchoy['count'] += 1

    Kok_choy = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minuskokchoy"),
                InlineKeyboardButton(text=str(sonKokchoy['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="pluskokchoy")
            ],
            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ]
        ]
    )

    summakokchoy = 5000 * sonKokchoy['count']
    new_caption = f"""
Ko'k choy 
Ko'k choy (ta’bga kora shakar)

Ko'k choy 5 000 x {sonKokchoy['count']} = {summakokchoy}
Umumiy: {summakokchoy} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/kokchoy.jpg', 'rb'), chat_id=call.message.chat.id,
                                    message_id=call.message.message_id, caption=new_caption
                                    ), reply_markup=Kok_choy,
    )


@dp.callback_query_handler(text='minuskokchoy')
async def minusKokchoy(call: types.CallbackQuery):
    print(sonKokchoy)

    if sonKokchoy['count'] > 1:
        sonKokchoy['count'] -= 1

        Kok_choy = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="minuskokchoy"),
                    InlineKeyboardButton(text=str(sonKokchoy['count']), callback_data='0'),
                    InlineKeyboardButton(text='+', callback_data="pluskokchoy")
                ],

                [
                    InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
                ]
            ]
        )

        summakokchoy = 5000 * sonKokchoy['count']
        new_caption = f"""
Ko'k choy 
Ko'k choy (ta’bga kora shakar)

Ko'k choy 5 000 x {sonKokchoy['count']} = {summakokchoy}
Umumiy: {summakokchoy} UZS"""

        await call.message.edit_media(
            media=types.InputMediaPhoto(open('images/kokchoy.jpg', 'rb'), caption=new_caption),
            reply_markup=Kok_choy
        )
    else:
        await call.answer("1dan kam mahsulot tanlash mumkin emas")


#-----------------------------------------------------------------------------------------------------------------------


sonLimonlichoy = {
    'count': 1,
}


@dp.message_handler(text="Limonli choy")
async def limonlichoy(message: types.Message):
    await message.answer("Mahsulot miqdorini tanlang")
    await message.answer_photo(photo=open('images/limonlichoy.jpg', 'rb'), caption="""
Limonli choy 
Limonli choy (ta’bga kora shakar) 

Limonli choy 7 000 x 1 = 7 000
Umumiy: 7 000 UZS""", reply_markup=Limonli_choy)


@dp.callback_query_handler(text='pluslimonlichoy')
async def plusLimonlichoy(call: types.CallbackQuery):
    print(sonLimonlichoy)
    sonLimonlichoy['count'] += 1

    Limonli_choy = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minuslimonlichoy"),
                InlineKeyboardButton(text=str(sonLimonlichoy['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="pluslimonlichoy")
            ],
            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ]
        ]
    )

    summalimonlichoy = 7000 * sonLimonlichoy['count']
    new_caption = f"""
Limonli choy 
Limonli choy (ta’bga kora shakar)

Limonli choy 7 000 x {sonLimonlichoy['count']} = {summalimonlichoy}
Umumiy: {summalimonlichoy} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/limonlichoy.jpg', 'rb'), chat_id=call.message.chat.id,
                                    message_id=call.message.message_id, caption=new_caption
                                    ), reply_markup=Limonli_choy,
    )


@dp.callback_query_handler(text='minuslimonlichoy')
async def minusLimonlichoy(call: types.CallbackQuery):
    print(sonLimonlichoy)

    if sonLimonlichoy['count'] > 1:
        sonLimonlichoy['count'] -= 1

        Limonli_choy = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="minuslimonlichoy"),
                    InlineKeyboardButton(text=str(sonLimonlichoy['count']), callback_data='0'),
                    InlineKeyboardButton(text='+', callback_data="pluslimonlichoy")
                ],

                [
                    InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
                ]
            ]
        )

        summalimonlichoy = 7000 * sonLimonlichoy['count']
        new_caption = f"""
Limonli choy 
Limonli choy (ta’bga kora shakar)

Limonli choy 7 000 x {sonLimonlichoy['count']} = {summalimonlichoy}
Umumiy: {summalimonlichoy} UZS"""

        await call.message.edit_media(
            media=types.InputMediaPhoto(open('images/limonlichoy.jpg', 'rb'), caption=new_caption),
            reply_markup=Limonli_choy
        )
    else:
        await call.answer("1dan kam mahsulot tanlash mumkin emas")


#-----------------------------------------------------------------------------------------------------------------------


sonFanta = {
    'count': 1,
}


@dp.message_handler(text="Fanta")
async def fanta(message: types.Message):
    await message.answer("Mahsulot miqdorini tanlang")
    await message.answer_photo(photo=open('images/fanta.jpg', 'rb'), caption="""
Fanta 500 ml 
   

Fanta 500 ml 10 000 x 1 = 10 000""", reply_markup=Fanta)


@dp.callback_query_handler(text='plusfanta')
async def plusFanta(call: types.CallbackQuery):
    print(sonFanta)
    sonFanta['count'] += 1

    Fanta = InlineKeyboardMarkup(
        inline_keyboard=[

            [
                InlineKeyboardButton(text='⬇️ Hajm ⬇️', callback_data='0')
            ],
            [
                InlineKeyboardButton(text='✅0,5l', callback_data='0')
            ],
            [
                InlineKeyboardButton(text='-', callback_data="minusfanta"),
                InlineKeyboardButton(text=str(sonFanta['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plusfanta")
            ],
            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ]
        ]
    )

    summafanta = 10000 * sonFanta['count']
    new_caption = f"""
Fanta 500 ml

Fanta 500 ml 10 000 x {sonFanta['count']} = {summafanta}
Umumiy: {summafanta} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/fanta.jpg', 'rb'), chat_id=call.message.chat.id,
                                    message_id=call.message.message_id, caption=new_caption
                                    ), reply_markup=Fanta,
    )


@dp.callback_query_handler(text='minusfanta')
async def minusFanta(call: types.CallbackQuery):
    print(sonFanta)

    if sonFanta['count'] > 1:
        sonFanta['count'] -= 1

        Fanta = InlineKeyboardMarkup(
            inline_keyboard=[

                [
                    InlineKeyboardButton(text='⬇️ Hajm ⬇️', callback_data='0')
                ],
                [
                    InlineKeyboardButton(text='✅0,5l', callback_data='0')
                ],
                [
                    InlineKeyboardButton(text='-', callback_data="minusfanta"),
                    InlineKeyboardButton(text=str(sonFanta['count']), callback_data='0'),
                    InlineKeyboardButton(text='+', callback_data="plusfanta")
                ],

                [
                    InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
                ]
            ]
        )

        summafanta = 10000 * sonFanta['count']
        new_caption = f"""
Fanta 500 ml

Fanta 500 ml 10 000 x {sonFanta['count']} = {summafanta}
Umumiy: {summafanta} UZS"""

        await call.message.edit_media(
            media=types.InputMediaPhoto(open('images/fanta.jpg', 'rb'), caption=new_caption),
            reply_markup=Fanta
        )
    else:
        await call.answer("1dan kam mahsulot tanlash mumkin emas")


#-----------------------------------------------------------------------------------------------------------------------


sonAmerikano = {
    'count': 1,
}


@dp.message_handler(text="Amerikano")
async def amerikano(message: types.Message):
    await message.answer("Mahsulot miqdorini tanlang")
    await message.answer_photo(photo=open('images/amerikano.jpg', 'rb'), caption="""
Amerikano 
Tabiiy donli qahva (espresso, suv)
 

Amerikano 12 000 x 1 = 12 000

Umumiy: 12 000 UZS""", reply_markup=Amerikano)


@dp.callback_query_handler(text='plusamerikano')
async def plusAmerikano(call: types.CallbackQuery):
    print(sonAmerikano)
    sonAmerikano['count'] += 1

    Amerikano = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minusamerikano"),
                InlineKeyboardButton(text=str(sonAmerikano['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plusamerikano")
            ],
            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ]
        ]
    )

    summaamerikano = 12000 * sonAmerikano['count']
    new_caption = f"""
Amerikano 
Tabiiy donli qahva (espresso, suv)

Amerikano 12 000 x {sonAmerikano['count']} = {summaamerikano}

Umumiy: {summaamerikano} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/amerikano.jpg', 'rb'), chat_id=call.message.chat.id,
                                    message_id=call.message.message_id, caption=new_caption
                                    ), reply_markup=Amerikano,
    )


@dp.callback_query_handler(text='minusamerikano')
async def minusAmerikano(call: types.CallbackQuery):
    print(sonAmerikano)

    if sonAmerikano['count'] > 1:
        sonAmerikano['count'] -= 1

        Amerikano = InlineKeyboardMarkup(
            inline_keyboard=[

                [
                    InlineKeyboardButton(text='-', callback_data="minusamerikano"),
                    InlineKeyboardButton(text=str(sonAmerikano['count']), callback_data='0'),
                    InlineKeyboardButton(text='+', callback_data="plusamerikano")
                ],

                [
                    InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
                ]
            ]
        )

        summaamerikano = 12000 * sonAmerikano['count']
        new_caption = f"""
Amerikano 
Tabiiy donli qahva (espresso, suv)

Amerikano 12 000 x {sonAmerikano['count']} = {summaamerikano}

Umumiy: {summaamerikano} UZS"""

        await call.message.edit_media(
            media=types.InputMediaPhoto(open('images/amerikano.jpg', 'rb'), caption=new_caption),
            reply_markup=Amerikano
        )
    else:
        await call.answer("1dan kam mahsulot tanlash mumkin emas")


#-----------------------------------------------------------------------------------------------------------------------


sonKapuchino = {
    'count': 1,
}


@dp.message_handler(text="Kapuchino")
async def kapuchino(message: types.Message):
    await message.answer("Mahsulot miqdorini tanlang")
    await message.answer_photo(photo=open('images/kapuchino.jpg', 'rb'), caption="""
Kapuchino 
Tabiiy donli qahva (espresso, sut, suv)
 

Kapuchino 14 000 x 1 = 14 000

Umumiy: 14 000 UZS""", reply_markup=Kapuchino)


@dp.callback_query_handler(text='pluskapuchino')
async def plusKapuchino(call: types.CallbackQuery):
    print(sonKapuchino)
    sonKapuchino['count'] += 1

    Kapuchino = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minuskapuchino"),
                InlineKeyboardButton(text=str(sonKapuchino['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="pluskapuchino")
            ],
            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ]
        ]
    )

    summakapuchino = 14000 * sonKapuchino['count']
    new_caption = f"""
Kapuchino 
Tabiiy donli qahva (espresso, sut, suv)

Kapuchino 14 000 x {sonKapuchino['count']} = {summakapuchino}

Umumiy: {summakapuchino} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/kapuchino.jpg', 'rb'), chat_id=call.message.chat.id,
                                    message_id=call.message.message_id, caption=new_caption
                                    ), reply_markup=Kapuchino,
    )


@dp.callback_query_handler(text='minuskapuchino')
async def minusKapuchino(call: types.CallbackQuery):
    print(sonKapuchino)

    if sonKapuchino['count'] > 1:
        sonKapuchino['count'] -= 1

        Kapuchino = InlineKeyboardMarkup(
            inline_keyboard=[

                [
                    InlineKeyboardButton(text='-', callback_data="minuskapuchino"),
                    InlineKeyboardButton(text=str(sonKapuchino['count']), callback_data='0'),
                    InlineKeyboardButton(text='+', callback_data="pluskapuchino")
                ],

                [
                    InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
                ]
            ]
        )

        summakapuchino = 14000 * sonKapuchino['count']
        new_caption = f"""
Kapuchino 
Tabiiy donli qahva (espresso, sut, suv)

Kapuchino 14 000 x {sonKapuchino['count']} = {summakapuchino}

Umumiy: {summakapuchino} UZS"""

        await call.message.edit_media(
            media=types.InputMediaPhoto(open('images/kapuchino.jpg', 'rb'), caption=new_caption),
            reply_markup=Kapuchino
        )
    else:
        await call.answer("1dan kam mahsulot tanlash mumkin emas")

#-----------------------------------------------------------------------------------------------------------------------

sonLatte = {
    'count': 1,
}


@dp.message_handler(text="Latte")
async def latte(message: types.Message):
    await message.answer("Mahsulot miqdorini tanlang")
    await message.answer_photo(photo=open('images/latte.jpg', 'rb'), caption="""
Latte 
Tabiiy donli qahva (espresso, sut, suv)
 

Latte 14 000 x 1 = 14 000

Umumiy: 14 000 UZS""", reply_markup=Latte)


@dp.callback_query_handler(text='pluslatte')
async def plusLatte(call: types.CallbackQuery):
    print(sonLatte)
    sonLatte['count'] += 1

    Latte = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minuslatte"),
                InlineKeyboardButton(text=str(sonLatte['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="pluslatte")
            ],
            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ]
        ]
    )

    summalatte = 14000 * sonLatte['count']
    new_caption = f"""
Latte 
Tabiiy donli qahva (espresso, sut, suv)

Latte 14 000 x {sonLatte['count']} = {summalatte}

Umumiy: {summalatte} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/latte.jpg', 'rb'), chat_id=call.message.chat.id,
                                    message_id=call.message.message_id, caption=new_caption
                                    ), reply_markup=Latte,
    )


@dp.callback_query_handler(text='minuslatte')
async def minusLatte(call: types.CallbackQuery):
    print(sonLatte)

    if sonLatte['count'] > 1:
        sonLatte['count'] -= 1

        Latte = InlineKeyboardMarkup(
            inline_keyboard=[

                [
                    InlineKeyboardButton(text='-', callback_data="minuslatte"),
                    InlineKeyboardButton(text=str(sonLatte['count']), callback_data='0'),
                    InlineKeyboardButton(text='+', callback_data="pluslatte")
                ],

                [
                    InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
                ]
            ]
        )

        summalatte = 14000 * sonLatte['count']
        new_caption = f"""
Latte 
Tabiiy donli qahva (espresso, sut, suv)

Latte 14 000 x {sonLatte['count']} = {summalatte}

Umumiy: {summalatte} UZS"""

        await call.message.edit_media(
            media=types.InputMediaPhoto(open('images/latte.jpg', 'rb'), caption=new_caption),
            reply_markup=Latte
        )
    else:
        await call.answer("1dan kam mahsulot tanlash mumkin emas")
