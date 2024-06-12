from loader import dp
from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.inline_buttons import Donar_kebab,Donar_box,NON

sonDonarkebab = {
    'count': 1,
}


@dp.message_handler(text="Donar kebab")
async def donarkebab(message: types.Message):
    await message.answer("Mahsulot miqdorini tanlang")
    await message.answer_photo(photo=open('images/donarkebab.jpg', 'rb'), caption="""
Donar kebab  
Mol go'shti donari-go'sht, makkajo'xori bilan guruch, kartoshka fri, qizil karam salati, pomidor sous
 

Donar kebab  42 000 x 1 = 42 000
Umumiy: 42 000 UZS""", reply_markup=Donar_kebab)


@dp.callback_query_handler(text='plusdonarkebab')
async def plusDonarkebab(call: types.CallbackQuery):
    print(sonDonarkebab)
    sonDonarkebab['count'] += 1

    Donar_kebab = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minusdonarkebab"),
                InlineKeyboardButton(text=str(sonDonarkebab['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plusdonarkebab")
            ],
            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ]
        ]
    )

    summadonarkebab = 42000 * sonDonarkebab['count']
    new_caption = f"""
Donar kebab  
Mol go'shti donari-go'sht, makkajo'xori bilan guruch, kartoshka fri, qizil karam salati, pomidor sous


Donar kebab  42 000 x {sonDonarkebab['count']} = {summadonarkebab}
Umumiy: {summadonarkebab} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/donarkebab.jpg', 'rb'), chat_id=call.message.chat.id,
                                    message_id=call.message.message_id, caption=new_caption
                                    ), reply_markup=Donar_kebab,
    )


@dp.callback_query_handler(text='minusdonarkebab')
async def minusDonarkebab(call: types.CallbackQuery):
    print(sonDonarkebab)

    if sonDonarkebab['count'] > 1:
        sonDonarkebab['count'] -= 1

        Donar_kebab = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="minusdonarkebab"),
                    InlineKeyboardButton(text=str(sonDonarkebab['count']), callback_data='0'),
                    InlineKeyboardButton(text='+', callback_data="plusdonarkebab")
                ],

                [
                    InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
                ]
            ]
        )

        summadonarkebab = 42000 * sonDonarkebab['count']
        new_caption = f"""
Donar kebab  
Mol go'shti donari-go'sht, makkajo'xori bilan guruch, kartoshka fri, qizil karam salati, pomidor sous


Donar kebab  42 000 x {sonDonarkebab['count']} = {summadonarkebab}
Umumiy: {summadonarkebab} UZS"""

        await call.message.edit_media(
            media=types.InputMediaPhoto(open('images/donarkebab.jpg', 'rb'), caption=new_caption),
            reply_markup=Donar_kebab
        )
    else:
        await call.answer("1dan kam mahsulot tanlash mumkin emas")


#-----------------------------------------------------------------------------------------------------------------------


sonDonarbox = {
    'count': 1,
}


@dp.message_handler(text="Donar Box")
async def donarbox(message: types.Message):
    await message.answer("Mahsulot miqdorini tanlang")
    await message.answer_photo(photo=open('images/donarbox.jpg', 'rb'), caption="""
Donar Box 
Mol go'shti donari-go'sht, kartoshka fri, guruch, ranch sous va pamidor

 
Donar Box 37 000 x 1 = 37 000
Umumiy: 37 000 UZS""", reply_markup=Donar_box)


@dp.callback_query_handler(text='plusdonarbox')
async def plusDonarbox(call: types.CallbackQuery):
    print(sonDonarbox)
    sonDonarbox['count'] += 1

    Donar_box = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minusdonarbox"),
                InlineKeyboardButton(text=str(sonDonarbox['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plusdonarbox")
            ],
            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ]
        ]
    )

    summadonarbox = 37000 * sonDonarbox['count']
    new_caption = f"""
Donar Box 
Mol go'shti donari-go'sht, kartoshka fri, guruch, ranch sous va pamidor


Donar Box 37 000 x {sonDonarbox['count']} = {summadonarbox}
Umumiy: {summadonarbox} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/donarbox.jpg', 'rb'), chat_id=call.message.chat.id,
                                    message_id=call.message.message_id, caption=new_caption
                                    ), reply_markup=Donar_box,
    )


@dp.callback_query_handler(text='minusdonarbox')
async def minusDonarbox(call: types.CallbackQuery):
    print(sonDonarbox)

    if sonDonarbox['count'] > 1:
        sonDonarbox['count'] -= 1

        Donar_box = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="minusdonarbox"),
                    InlineKeyboardButton(text=str(sonDonarbox['count']), callback_data='0'),
                    InlineKeyboardButton(text='+', callback_data="plusdonarbox")
                ],

                [
                    InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
                ]
            ]
        )

        summadonarbox = 37000 * sonDonarbox['count']
        new_caption = f"""
Donar Box 
Mol go'shti donari-go'sht, kartoshka fri, guruch, ranch sous va pamidor


Donar Box 37 000 x {sonDonarbox['count']} = {summadonarbox}
Umumiy: {summadonarbox} UZS"""

        await call.message.edit_media(
            media=types.InputMediaPhoto(open('images/donarbox.jpg', 'rb'), caption=new_caption),
            reply_markup=Donar_box
        )
    else:
        await call.answer("1dan kam mahsulot tanlash mumkin emas")


#-----------------------------------------------------------------------------------------------------------------------

sonNon = {
    'count': 1,
}


@dp.message_handler(text="Non")
async def non(message: types.Message):
    await message.answer("Mahsulot miqdorini tanlang")
    await message.answer_photo(photo=open('images/non.jpg', 'rb'), caption="""
Non 
Yumshoq bulochka
 

Non 3 000 x 1 = 3 000
Umumiy: 3 000 UZS""", reply_markup=NON)


@dp.callback_query_handler(text='plusnon')
async def plusNon(call: types.CallbackQuery):
    print(sonNon)
    sonNon['count'] += 1

    NON = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minusnon"),
                InlineKeyboardButton(text=str(sonNon['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plusnon")
            ],
            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ]
        ]
    )

    summanon= 3000 * sonNon['count']
    new_caption = f"""
Non 
Yumshoq bulochka


Non 3 000 x {sonNon['count']} = {summanon}
Umumiy: {summanon} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/non.jpg', 'rb'), chat_id=call.message.chat.id,
                                    message_id=call.message.message_id, caption=new_caption
                                    ), reply_markup=NON,
    )


@dp.callback_query_handler(text='minusnon')
async def minusNon(call: types.CallbackQuery):
    print(sonNon)

    if sonNon['count'] > 1:
        sonNon['count'] -= 1

        NON = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="minusnon"),
                    InlineKeyboardButton(text=str(sonNon['count']), callback_data='0'),
                    InlineKeyboardButton(text='+', callback_data="plusnon")
                ],

                [
                    InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
                ]
            ]
        )

        summanon = 3000 * sonNon['count']
        new_caption = f"""
Non 
Yumshoq bulochka


Non 3 000 x {sonNon['count']} = {summanon}
Umumiy: {summanon} UZS"""

        await call.message.edit_media(
            media=types.InputMediaPhoto(open('images/non.jpg', 'rb'), caption=new_caption),
            reply_markup=NON
        )
    else:
        await call.answer("1dan kam mahsulot tanlash mumkin emas")
