from loader import dp
from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.inline_buttons import Hot_dog,Chiz_dog,Longer

sonHotdog = {
    'count': 1,
}


@dp.message_handler(text="Hot Dog")
async def hotdog(message: types.Message):
    await message.answer("Mahsulot miqdorini tanlang")
    await message.answer_photo(photo=open('images/hotdog.jpg', 'rb'), caption="""
Hot Dog 
Hot-dog bulochkasi, Kanada sosiskasi, tuzlangan bodring, pomidor, Hot-dog sousi
 

Hot Dog 12 000 x 1 = 12 000
Umumiy: 12 000 UZS""", reply_markup=Hot_dog)


@dp.callback_query_handler(text='plushotdog')
async def plusHotdog(call: types.CallbackQuery):
    print(sonHotdog)
    sonHotdog['count'] += 1

    Hot_dog = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minushotdog"),
                InlineKeyboardButton(text=str(sonHotdog['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plushotdog")
            ],
            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ]
        ]
    )

    summahotdog = 12000 * sonHotdog['count']
    new_caption = f"""
Hot Dog 
Hot-dog bulochkasi, Kanada sosiskasi, tuzlangan bodring, pomidor, Hot-dog sousi


Hot Dog 12 000 x {sonHotdog['count']} = {summahotdog}
Umumiy: {summahotdog} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/hotdog.jpg', 'rb'), chat_id=call.message.chat.id,
                                    message_id=call.message.message_id, caption=new_caption
                                    ), reply_markup=Hot_dog,
    )


@dp.callback_query_handler(text='minushotdog')
async def minusHotdog(call: types.CallbackQuery):
    print(sonHotdog)

    if sonHotdog['count'] > 1:
        sonHotdog['count'] -= 1

        Hot_dog = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="minushotdog"),
                    InlineKeyboardButton(text=str(sonHotdog['count']), callback_data='0'),
                    InlineKeyboardButton(text='+', callback_data="plushotdog")
                ],

                [
                    InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
                ]
            ]
        )

        summahotdog = 12000 * sonHotdog['count']
        new_caption = f"""
Hot Dog 
Hot-dog bulochkasi, Kanada sosiskasi, tuzlangan bodring, pomidor, Hot-dog sousi


Hot Dog 12 000 x {sonHotdog['count']} = {summahotdog}
Umumiy: {summahotdog} UZS"""

        await call.message.edit_media(
            media=types.InputMediaPhoto(open('images/hotdog.jpg', 'rb'), caption=new_caption),
            reply_markup=Hot_dog
        )
    else:
        await call.answer("1dan kam mahsulot tanlash mumkin emas")



#-----------------------------------------------------------------------------------------------------------------------

sonChizdog = {
    'count': 1,
}


@dp.message_handler(text="Chiz dog")
async def chizdog(message: types.Message):
    await message.answer("Mahsulot miqdorini tanlang")
    await message.answer_photo(photo=open('images/chizdog.jpg', 'rb'), caption="""
Chiz dog 
Hot-dog bulochkasi, kanada sosiskasi, tuzlangan bodring, pomidor, Xoxland pishloq, Hot-dog sousi
 

Chiz dog 15 000 x 1 = 15 000
Umumiy: 15 000 UZS""", reply_markup=Chiz_dog)


@dp.callback_query_handler(text='pluschizdog')
async def plusChizdog(call: types.CallbackQuery):
    print(sonChizdog)
    sonChizdog['count'] += 1

    Chiz_dog = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minuschizdog"),
                InlineKeyboardButton(text=str(sonChizdog['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="pluschizdog")
            ],
            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ]
        ]
    )

    summachizdog = 15000 * sonChizdog['count']
    new_caption = f"""
Chiz dog 
Hot-dog bulochkasi, kanada sosiskasi, tuzlangan bodring, pomidor, Xoxland pishloq, Hot-dog sousi


Chiz dog 15 000 x {sonChizdog['count']} = {summachizdog}
Umumiy: {summachizdog} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/chizdog.jpg', 'rb'), chat_id=call.message.chat.id,
                                    message_id=call.message.message_id, caption=new_caption
                                    ), reply_markup=Chiz_dog,
    )


@dp.callback_query_handler(text='minuschizdog')
async def minusChizdog(call: types.CallbackQuery):
    print(sonChizdog)

    if sonChizdog['count'] > 1:
        sonChizdog['count'] -= 1

        Chiz_dog = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="minuschizdog"),
                    InlineKeyboardButton(text=str(sonChizdog['count']), callback_data='0'),
                    InlineKeyboardButton(text='+', callback_data="pluschizdog")
                ],

                [
                    InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
                ]
            ]
        )

        summachizdog = 15000 * sonChizdog['count']
        new_caption = f"""
Chiz dog 
Hot-dog bulochkasi, kanada sosiskasi, tuzlangan bodring, pomidor, Xoxland pishloq, Hot-dog sousi


Chiz dog 15 000 x {sonChizdog['count']} = {summachizdog}
Umumiy: {summachizdog} UZS"""

        await call.message.edit_media(
            media=types.InputMediaPhoto(open('images/chizdog.jpg', 'rb'), caption=new_caption),
            reply_markup=Chiz_dog
        )
    else:
        await call.answer("1dan kam mahsulot tanlash mumkin emas")


#-----------------------------------------------------------------------------------------------------------------------


sonLonger= {
    'count': 1,
}


@dp.message_handler(text="Longer")
async def longer(message: types.Message):
    await message.answer("Mahsulot miqdorini tanlang")
    await message.answer_photo(photo=open('images/longer.jpg', 'rb'), caption="""
Longer  
Hot-dog bulochka,ketchup, mayonez, strips  1 dona, tuzlangan bodring 3 dona va aysberg salat bargi 

Longer  15 000 x 1 = 15 000
Umumiy: 15 000 UZS""", reply_markup=Longer)


@dp.callback_query_handler(text='pluslonger')
async def plusLonger(call: types.CallbackQuery):
    print(sonLonger)
    sonLonger['count'] += 1

    Longer = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minuslonger"),
                InlineKeyboardButton(text=str(sonLonger['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="pluslonger")
            ],
            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ]
        ]
    )

    summalonger = 15000 * sonLonger['count']
    new_caption = f"""
Longer  
Hot-dog bulochka,ketchup, mayonez, strips  1 dona, tuzlangan bodring 3 dona va aysberg salat bargi

Longer  15 000 x {sonLonger['count']} = {summalonger}
Umumiy: {summalonger} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/longer.jpg', 'rb'), chat_id=call.message.chat.id,
                                    message_id=call.message.message_id, caption=new_caption
                                    ), reply_markup=Longer,
    )


@dp.callback_query_handler(text='minuslonger')
async def minusLonger(call: types.CallbackQuery):
    print(sonLonger)

    if sonLonger['count'] > 1:
        sonLonger['count'] -= 1

        Longer = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="minuslonger"),
                    InlineKeyboardButton(text=str(sonLonger['count']), callback_data='0'),
                    InlineKeyboardButton(text='+', callback_data="pluslonger")
                ],

                [
                    InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
                ]
            ]
        )

        summalonger = 15000 * sonLonger['count']
        new_caption = f"""
Longer  
Hot-dog bulochka,ketchup, mayonez, strips  1 dona, tuzlangan bodring 3 dona va aysberg salat bargi

Longer  15 000 x {sonLonger['count']} = {summalonger}
Umumiy: {summalonger} UZS"""

        await call.message.edit_media(
            media=types.InputMediaPhoto(open('images/longer.jpg', 'rb'), caption=new_caption),
            reply_markup=Longer
        )
    else:
        await call.answer("1dan kam mahsulot tanlash mumkin emas")