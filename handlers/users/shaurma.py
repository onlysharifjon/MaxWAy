from loader import dp
from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.inline_buttons import German_donar,Shaurma,ShaurmaP



sonGermandonar = {
    'count': 1,
}


@dp.message_handler(text="German Donar")
async def germandonar(message: types.Message):
    await message.answer("Mahsulot miqdorini tanlang")
    await message.answer_photo(photo=open('images/germandonar.jpg', 'rb'), caption="""
German Donar 
Non, ranch sousi, qizil karam salati, Doner go'shti, aysberg salati, yangi pomidor 

German Donar 30 000 x 1 = 30 000
Umumiy: 30 000 UZS""", reply_markup=German_donar)


@dp.callback_query_handler(text='plusgermandonar')
async def plusGermandonar(call: types.CallbackQuery):
    print(sonGermandonar)
    sonGermandonar['count'] += 1

    German_donar = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minusgermandonar"),
                InlineKeyboardButton(text=str(sonGermandonar['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plusgermandonar")
            ],
            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ]
        ]
    )

    summagermandonar = 30000 * sonGermandonar['count']
    new_caption = f"""
German Donar 
Non, ranch sousi, qizil karam salati, Doner go'shti, aysberg salati, yangi pomidor

German Donar 30 000 x  {sonGermandonar['count']} = {summagermandonar}
Umumiy: {summagermandonar} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/germandonar.jpg', 'rb'), chat_id=call.message.chat.id,
                                    message_id=call.message.message_id, caption=new_caption
                                    ), reply_markup=German_donar,
    )


@dp.callback_query_handler(text='minusgermandonar')
async def minusGermandonar(call: types.CallbackQuery):
    print(sonGermandonar)

    if sonGermandonar['count'] > 1:
        sonGermandonar['count'] -= 1

        German_donar = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="minusgermandonar"),
                    InlineKeyboardButton(text=str(sonGermandonar['count']), callback_data='0'),
                    InlineKeyboardButton(text='+', callback_data="plusgermandonar")
                ],

                [
                    InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
                ]
            ]
        )

        summagermandonar = 30000 * sonGermandonar['count']
        new_caption = f"""
German Donar 
Non, ranch sousi, qizil karam salati, Doner go'shti, aysberg salati, yangi pomidor

German Donar 30 000 x  {sonGermandonar['count']} = {summagermandonar}
Umumiy: {summagermandonar} UZS"""

        await call.message.edit_media(
            media=types.InputMediaPhoto(open('images/germandonar.jpg', 'rb'), caption=new_caption),
            reply_markup=German_donar
        )
    else:
        await call.answer("1dan kam mahsulot tanlash mumkin emas")


#-----------------------------------------------------------------------------------------------------------------------

sonShaurma = {
    'count': 1,
}


@dp.message_handler(text="Shaurma")
async def shaurma(message: types.Message):
    await message.answer("Mahsulot miqdorini tanlang")
    await message.answer_photo(photo=open('images/shaurma.jpg', 'rb'), caption="""
Shaurma 
Donor bulochka, mol go'shti-donar, yangi bodring, pomidor, pomidor sousi 

Shaurma 28 000 x 1 = 28 000
Umumiy: 28 000 UZS""", reply_markup=Shaurma)


@dp.callback_query_handler(text='plusshaurma')
async def plusShaurma(call: types.CallbackQuery):
    print(sonShaurma)
    sonShaurma['count'] += 1

    Shaurma = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minusshaurma"),
                InlineKeyboardButton(text=str(sonShaurma['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plusshaurma")
            ],
            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ]
        ]
    )

    summashaurma = 28000 * sonShaurma['count']
    new_caption = f"""
Shaurma 
Donor bulochka, mol go'shti-donar, yangi bodring, pomidor, pomidor sousi 

Shaurma 28 000 x  {sonShaurma['count']} = {summashaurma}
Umumiy: {summashaurma} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/shaurma.jpg', 'rb'), chat_id=call.message.chat.id,
                                    message_id=call.message.message_id, caption=new_caption
                                    ), reply_markup=Shaurma,
    )


@dp.callback_query_handler(text='minusshaurma')
async def minusShaurma(call: types.CallbackQuery):
    print(sonShaurma)

    if sonShaurma['count'] > 1:
        sonShaurma['count'] -= 1

        Shaurma = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="minusshaurma"),
                    InlineKeyboardButton(text=str(sonShaurma['count']), callback_data='0'),
                    InlineKeyboardButton(text='+', callback_data="plusshaurma")
                ],

                [
                    InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
                ]
            ]
        )

        summashaurma = 28000 * sonShaurma['count']
        new_caption = f"""
Shaurma 
Donor bulochka, mol go'shti-donar, yangi bodring, pomidor, pomidor sousi 

Shaurma 28 000 x  {sonShaurma['count']} = {summashaurma}
Umumiy: {summashaurma} UZS"""

        await call.message.edit_media(
            media=types.InputMediaPhoto(open('images/shaurma.jpg', 'rb'), caption=new_caption),
            reply_markup=Shaurma
        )
    else:
        await call.answer("1dan kam mahsulot tanlash mumkin emas")


#-----------------------------------------------------------------------------------------------------------------------

sonShaurmap = {
    'count': 1,
}


@dp.message_handler(text="Shaurma pishloqli")
async def shaurmap(message: types.Message):
    await message.answer("Mahsulot miqdorini tanlang")
    await message.answer_photo(photo=open('images/shaurmaP.jpg', 'rb'), caption="""
Shaurma pishloqli 
Donor bulochka, mol go'shti-donar, yangi bodring, pomidor, pomidor sousi, Xoxland pishloq 

Shaurma pishloqli 30 000 x 1 = 30 000
Umumiy: 30 000 UZS""", reply_markup=ShaurmaP)


@dp.callback_query_handler(text='plusshaurmap')
async def plusShaurmap(call: types.CallbackQuery):
    print(sonShaurmap)
    sonShaurmap['count'] += 1

    ShaurmaP = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minusshaurmap"),
                InlineKeyboardButton(text=str(sonShaurmap['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plusshaurmap")
            ],
            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ]
        ]
    )

    summashaurmap = 30000 * sonShaurmap['count']
    new_caption = f"""
Shaurma pishloqli 
Donor bulochka, mol go'shti-donar, yangi bodring, pomidor, pomidor sousi, Xoxland pishloq  

Shaurma pishloqli 30 000 x  {sonShaurmap['count']} = {summashaurmap}
Umumiy: {summashaurmap} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/shaurmaP.jpg', 'rb'), chat_id=call.message.chat.id,
                                    message_id=call.message.message_id, caption=new_caption
                                    ), reply_markup=ShaurmaP,
    )


@dp.callback_query_handler(text='minusshaurmap')
async def minusShaurmap(call: types.CallbackQuery):
    print(sonShaurmap)

    if sonShaurmap['count'] > 1:
        sonShaurmap['count'] -= 1

        ShaurmaP = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="minusshaurmap"),
                    InlineKeyboardButton(text=str(sonShaurmap['count']), callback_data='0'),
                    InlineKeyboardButton(text='+', callback_data="plusshaurmap")
                ],

                [
                    InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
                ]
            ]
        )

        summashaurmap = 30000 * sonShaurmap['count']
        new_caption = f"""
Shaurma pishloqli 
Donor bulochka, mol go'shti-donar, yangi bodring, pomidor, pomidor sousi, Xoxland pishloq 

Shaurma pishloqli 30 000 x  {sonShaurmap['count']} = {summashaurmap}
Umumiy: {summashaurmap} UZS"""

        await call.message.edit_media(
            media=types.InputMediaPhoto(open('images/shaurmaP.jpg', 'rb'), caption=new_caption),
            reply_markup=ShaurmaP
        )
    else:
        await call.answer("1dan kam mahsulot tanlash mumkin emas")
