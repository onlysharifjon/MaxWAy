from loader import dp
from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.inline_buttons import Ketchup,Pishloqli_sous,Sarimsoqli_sous,Xalapeno,Shirin_sous


sonKetchup = {
    'count': 1,
}


@dp.message_handler(text="Ketchup")
async def ketchup(message: types.Message):
    await message.answer("Mahsulot miqdorini tanlang")
    await message.answer_photo(photo=open('images/ketchup.jpg', 'rb'), caption="""
Ketchup 
   

Ketchup 3 000 x 1 = 3 000
Umumiy: 3 000 UZS""", reply_markup=Ketchup)


@dp.callback_query_handler(text='plusketchup')
async def plusKetchup(call: types.CallbackQuery):
    print(sonKetchup)
    sonKetchup['count'] += 1

    Ketchup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minusketchup"),
                InlineKeyboardButton(text=str(sonKetchup['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plusketchup")
            ],
            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ]
        ]
    )

    summaketchup = 3000 * sonKetchup['count']
    new_caption = f"""
Ketchup


Ketchup 3 000 x {sonKetchup['count']} = {summaketchup}
Umumiy: {summaketchup} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/ketchup.jpg', 'rb'), chat_id=call.message.chat.id,
                                    message_id=call.message.message_id, caption=new_caption
                                    ), reply_markup=Ketchup,
    )


@dp.callback_query_handler(text='minusketchup')
async def minusKetchup(call: types.CallbackQuery):
    print(sonKetchup)

    if sonKetchup['count'] > 1:
        sonKetchup['count'] -= 1

        Ketchup = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="minusketchup"),
                    InlineKeyboardButton(text=str(sonKetchup['count']), callback_data='0'),
                    InlineKeyboardButton(text='+', callback_data="plusketchup")
                ],

                [
                    InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
                ]
            ]
        )

        summaketchup = 3000 * sonKetchup['count']
        new_caption = f"""
Ketchup


Ketchup 3 000 x {sonKetchup['count']} = {summaketchup}
Umumiy: {summaketchup} UZS"""

        await call.message.edit_media(
            media=types.InputMediaPhoto(open('images/ketchup.jpg', 'rb'), caption=new_caption),
            reply_markup=Ketchup
        )
    else:
        await call.answer("1dan kam mahsulot tanlash mumkin emas")


#-----------------------------------------------------------------------------------------------------------------------

sonPishloqlisous = {
    'count': 1,
}


@dp.message_handler(text="Pishloqli sous")
async def pishloqlisous(message: types.Message):
    await message.answer("Mahsulot miqdorini tanlang")
    await message.answer_photo(photo=open('images/pishloqlisous.jpg', 'rb'), caption="""
Pishloqli sous 
  

Pishloqli sous 3 000 x 1 = 3 000
Umumiy: 3 000 UZS""", reply_markup=Pishloqli_sous)


@dp.callback_query_handler(text='pluspishloqlisous')
async def plusPishloqlisous(call: types.CallbackQuery):
    print(sonPishloqlisous)
    sonPishloqlisous['count'] += 1

    Pishloqli_sous = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minuspishloqlisous"),
                InlineKeyboardButton(text=str(sonPishloqlisous['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="pluspishloqlisous")
            ],
            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ]
        ]
    )

    summapishloqlisous = 3000 * sonPishloqlisous['count']
    new_caption = f"""
Pishloqli sous 


Pishloqli sous 3 000 x {sonPishloqlisous['count']} = {summapishloqlisous}
Umumiy: {summapishloqlisous} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/pishloqlisous.jpg', 'rb'), chat_id=call.message.chat.id,
                                    message_id=call.message.message_id, caption=new_caption
                                    ), reply_markup=Pishloqli_sous,
    )


@dp.callback_query_handler(text='minuspishloqlisous')
async def minusPishloqlisous(call: types.CallbackQuery):
    print(sonPishloqlisous)

    if sonPishloqlisous['count'] > 1:
        sonPishloqlisous['count'] -= 1

        Pishloqli_sous = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="minuspishloqlisous"),
                    InlineKeyboardButton(text=str(sonPishloqlisous['count']), callback_data='0'),
                    InlineKeyboardButton(text='+', callback_data="pluspishloqlisous")
                ],

                [
                    InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
                ]
            ]
        )

        summapishloqlisous = 3000 * sonPishloqlisous['count']
        new_caption = f"""
Pishloqli sous 


Pishloqli sous 3 000 x {sonPishloqlisous['count']} = {summapishloqlisous}
Umumiy: {summapishloqlisous} UZS"""

        await call.message.edit_media(
            media=types.InputMediaPhoto(open('images/pishloqlisous.jpg', 'rb'), caption=new_caption),
            reply_markup=Pishloqli_sous
        )
    else:
        await call.answer("1dan kam mahsulot tanlash mumkin emas")


#-----------------------------------------------------------------------------------------------------------------------


sonSarimsoqlisous = {
    'count': 1,
}


@dp.message_handler(text="Sarimsoqli sous")
async def sarimsoqlisous(message: types.Message):
    await message.answer("Mahsulot miqdorini tanlang")
    await message.answer_photo(photo=open('images/sarimsoqlisous.jpg', 'rb'), caption="""
Sarimsoqli sous 
   

Sarimsoqli sous 3 000 x 1 = 3 000
Umumiy: 3 000 UZS""", reply_markup=Sarimsoqli_sous)


@dp.callback_query_handler(text='plussarimsoqlisous')
async def plusSarimsoqlisous(call: types.CallbackQuery):
    print(sonSarimsoqlisous)
    sonSarimsoqlisous['count'] += 1

    Sarimsoqli_sous = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minussarimsoqlisous"),
                InlineKeyboardButton(text=str(sonSarimsoqlisous['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plussarimsoqlisous")
            ],
            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ]
        ]
    )

    summasarimsoqlisous = 3000 * sonSarimsoqlisous['count']
    new_caption = f"""
Sarimsoqli sous 


Sarimsoqli sous 3 000 x {sonSarimsoqlisous['count']} = {summasarimsoqlisous}
Umumiy: {summasarimsoqlisous} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/sarimsoqlisous.jpg', 'rb'), chat_id=call.message.chat.id,
                                    message_id=call.message.message_id, caption=new_caption
                                    ), reply_markup=Sarimsoqli_sous,
    )


@dp.callback_query_handler(text='minussarimsoqlisous')
async def minusSarimsoqlisous(call: types.CallbackQuery):
    print(sonSarimsoqlisous)

    if sonSarimsoqlisous['count'] > 1:
        sonSarimsoqlisous['count'] -= 1

        Sarimsoqli_sous = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="minussarimsoqlisous"),
                    InlineKeyboardButton(text=str(sonSarimsoqlisous['count']), callback_data='0'),
                    InlineKeyboardButton(text='+', callback_data="plussarimsoqlisous")
                ],

                [
                    InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
                ]
            ]
        )

        summasarimsoqlisous = 3000 * sonSarimsoqlisous['count']
        new_caption = f"""
Sarimsoqli sous 


Sarimsoqli sous 3 000 x {sonSarimsoqlisous['count']} = {summasarimsoqlisous}
Umumiy: {summasarimsoqlisous} UZS"""

        await call.message.edit_media(
            media=types.InputMediaPhoto(open('images/sarimsoqlisous.jpg', 'rb'), caption=new_caption),
            reply_markup=Sarimsoqli_sous
        )
    else:
        await call.answer("1dan kam mahsulot tanlash mumkin emas")

#-----------------------------------------------------------------------------------------------------------------------

sonXalapeno = {
    'count': 1,
}


@dp.message_handler(text="Xalapeno")
async def xalapeno(message: types.Message):
    await message.answer("Mahsulot miqdorini tanlang")
    await message.answer_photo(photo=open('images/xalapeno.jpg', 'rb'), caption="""
Xalapeno 
   

Xalapeno 3 000 x 1 = 3 000
Umumiy: 3 000 UZS""", reply_markup=Xalapeno)


@dp.callback_query_handler(text='plusxalapeno')
async def plusXalapeno(call: types.CallbackQuery):
    print(sonXalapeno)
    sonXalapeno['count'] += 1

    Xalapeno = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minusxalapeno"),
                InlineKeyboardButton(text=str(sonXalapeno['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plusxalapeno")
            ],
            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ]
        ]
    )

    summaxalapeno = 3000 * sonXalapeno['count']
    new_caption = f"""
Xalapeno


Xalapeno 3 000 x {sonXalapeno['count']} = {summaxalapeno}
Umumiy: {summaxalapeno} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/xalapeno.jpg', 'rb'), chat_id=call.message.chat.id,
                                    message_id=call.message.message_id, caption=new_caption
                                    ), reply_markup=Xalapeno,
    )


@dp.callback_query_handler(text='minusxalapeno')
async def minusXalapeno(call: types.CallbackQuery):
    print(sonXalapeno)

    if sonXalapeno['count'] > 1:
        sonXalapeno['count'] -= 1

        Xalapeno = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="minusxalapeno"),
                    InlineKeyboardButton(text=str(sonXalapeno['count']), callback_data='0'),
                    InlineKeyboardButton(text='+', callback_data="plusxalapeno")
                ],

                [
                    InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
                ]
            ]
        )

        summaxalapeno = 3000 * sonXalapeno['count']
        new_caption = f"""
Xalapeno 


Xalapeno 3 000 x {sonXalapeno['count']} = {summaxalapeno}
Umumiy: {summaxalapeno} UZS"""

        await call.message.edit_media(
            media=types.InputMediaPhoto(open('images/xalapeno.jpg', 'rb'), caption=new_caption),
            reply_markup=Xalapeno
        )
    else:
        await call.answer("1dan kam mahsulot tanlash mumkin emas")


#-----------------------------------------------------------------------------------------------------------------------


sonShirinsous = {
    'count': 1,
}


@dp.message_handler(text="Shirin va nordon sous")
async def shirinsous(message: types.Message):
    await message.answer("Mahsulot miqdorini tanlang")
    await message.answer_photo(photo=open('images/shirinsous.jpg', 'rb'), caption="""
Shirin va nordon sous 
  

Shirin va nordon sous 3 000 x 1 = 3 000
Umumiy: 3 000 UZS""", reply_markup=Shirin_sous)


@dp.callback_query_handler(text='plusshirinsous')
async def plusShirinsous(call: types.CallbackQuery):
    print(sonShirinsous)
    sonShirinsous['count'] += 1

    Shirin_sous = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minusshirinsous"),
                InlineKeyboardButton(text=str(sonShirinsous['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plusshirinsous")
            ],
            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ]
        ]
    )

    summashirinsous = 3000 * sonShirinsous['count']
    new_caption = f"""
Shirin va nordon sous


Shirin va nordon sous 3 000 x {sonShirinsous['count']} = {summashirinsous}
Umumiy: {summashirinsous} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/shirinsous.jpg', 'rb'), chat_id=call.message.chat.id,
                                    message_id=call.message.message_id, caption=new_caption
                                    ), reply_markup=Shirin_sous,
    )


@dp.callback_query_handler(text='minusshirinsous')
async def minusShirinsous(call: types.CallbackQuery):
    print(sonShirinsous)

    if sonShirinsous['count'] > 1:
        sonShirinsous['count'] -= 1

        Shirin_sous = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="minusshirinsous"),
                    InlineKeyboardButton(text=str(sonShirinsous['count']), callback_data='0'),
                    InlineKeyboardButton(text='+', callback_data="plusshirinsous")
                ],

                [
                    InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
                ]
            ]
        )

        summashirinsous = 3000 * sonShirinsous['count']
        new_caption = f"""
Shirin va nordon sous 


Shirin va nordon sous 3 000 x {sonShirinsous['count']} = {summashirinsous}
Umumiy: {summashirinsous} UZS"""

        await call.message.edit_media(
            media=types.InputMediaPhoto(open('images/shirinsous.jpg', 'rb'), caption=new_caption),
            reply_markup=Shirin_sous
        )
    else:
        await call.answer("1dan kam mahsulot tanlash mumkin emas")
