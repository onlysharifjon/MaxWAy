from loader import dp
from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.inline_buttons import Lavash_klassik,Lavash_pishloqli,Lavash_achchiq,Lavash_mini,Lavash_minip



sonLavashklassik = {
    'count': 1,
}


@dp.message_handler(text="Lavash standart klassik")
async def lavashklassik(message: types.Message):
    await message.answer("Mahsulot miqdorini tanlang")
    await message.answer_photo(photo=open('images/lavashKlassik.jpg', 'rb'), caption="""
Lavash standart klassik 
Lavash xamiri, mol go'shti-donar, pomidor, chipslar, pomidor sousi, mayonez 

Lavash standart klassik 30 000 x 1 = 30 000
Umumiy: 30 000 UZS""", reply_markup=Lavash_klassik)


@dp.callback_query_handler(text='pluslavashklassik')
async def pluslavashklassik(call: types.CallbackQuery):
    print(sonLavashklassik)
    sonLavashklassik['count'] += 1

    Lavash_klassik = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minuslavashklassik"),
                InlineKeyboardButton(text=str(sonLavashklassik['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="pluslavashklassik")
            ],
            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ]
        ]
    )

    summalavashklassik = 30000 * sonLavashklassik['count']
    new_caption = f"""
Lavash standart klassik 
Lavash xamiri, mol go'shti-donar, pomidor, chipslar, pomidor sousi, mayonez

Lavash standart klassik 30 000 x  {sonLavashklassik['count']} = {summalavashklassik}
Umumiy: {summalavashklassik} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/lavashKlassik.jpg', 'rb'), chat_id=call.message.chat.id,
                                    message_id=call.message.message_id, caption=new_caption
                                    ), reply_markup=Lavash_klassik,
    )


@dp.callback_query_handler(text='minuslavashklassik')
async def minuslavashklassik(call: types.CallbackQuery):
    print(sonLavashklassik)

    if sonLavashklassik['count'] > 1:
        sonLavashklassik['count'] -= 1

        Lavash_klassik = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="minuslavashklassik"),
                    InlineKeyboardButton(text=str(sonLavashklassik['count']), callback_data='0'),
                    InlineKeyboardButton(text='+', callback_data="pluslavashklassik")
                ],

                [
                    InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
                ]
            ]
        )

        summalavashklassik = 30000 * sonLavashklassik['count']
        new_caption = f"""
Lavash standart klassik 
Lavash xamiri, mol go'shti-donar, pomidor, chipslar, pomidor sousi, mayonez

Lavash standart klassik 30 000 x  {sonLavashklassik['count']} = {summalavashklassik}
Umumiy: {summalavashklassik} UZS"""

        await call.message.edit_media(
            media=types.InputMediaPhoto(open('images/lavashKlassik.jpg', 'rb'), caption=new_caption),
            reply_markup=Lavash_klassik
        )
    else:
        await call.answer("1dan kam mahsulot tanlash mumkin emas")


#-----------------------------------------------------------------------------------------------------------------------


sonLavashpishloqli = {
    'count': 1,
}


@dp.message_handler(text="Lavash standart pishloqli")
async def lavashpishloqli(message: types.Message):
    await message.answer("Mahsulot miqdorini tanlang")
    await message.answer_photo(photo=open('images/lavashpishloqli.jpg', 'rb'), caption="""
Lavash standart pishloqli 
Lavash xamiri, mol go'shti-donar, pomidor, chiplar, pomidor sousi, mayonez, Xoxland pishloq
 

Lavash standart pishloqli 33 000 x 1 = 33 000
Umumiy: 33 000 UZS""", reply_markup=Lavash_pishloqli)


@dp.callback_query_handler(text='pluslavashpishloqli')
async def pluslavashpishloq(call: types.CallbackQuery):
    print(sonLavashpishloqli)
    sonLavashpishloqli['count'] += 1

    Lavash_pishloqli = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minuslavashpishloqli"),
                InlineKeyboardButton(text=str(sonLavashpishloqli['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="pluslavashpishloqli")
            ],
            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ]
        ]
    )

    summalavashpishloqli = 33000 * sonLavashpishloqli['count']
    new_caption = f"""
Lavash standart pishloqli 
Lavash xamiri, mol go'shti-donar, pomidor, chiplar, pomidor sousi, mayonez, Xoxland pishloq
 

Lavash standart pishloqli 33 000 x  {sonLavashpishloqli['count']} = {summalavashpishloqli}
Umumiy: {summalavashpishloqli} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/lavashpishloqli.jpg', 'rb'), chat_id=call.message.chat.id,
                                    message_id=call.message.message_id, caption=new_caption
                                    ), reply_markup=Lavash_pishloqli,
    )


@dp.callback_query_handler(text='minuslavashpishloqli')
async def minuslavashpishloq(call: types.CallbackQuery):
    print(sonLavashpishloqli)

    if sonLavashpishloqli['count'] > 1:
        sonLavashpishloqli['count'] -= 1

        Lavash_pishloqli = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="minuslavashpishloqli"),
                    InlineKeyboardButton(text=str(sonLavashpishloqli['count']), callback_data='0'),
                    InlineKeyboardButton(text='+', callback_data="pluslavashpishloqli")
                ],

                [
                    InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
                ]
            ]
        )

        summalavashpishloqli = 33000 * sonLavashpishloqli['count']
        new_caption = f"""
Lavash standart pishloqli 
Lavash xamiri, mol go'shti-donar, pomidor, chiplar, pomidor sousi, mayonez, Xoxland pishloq
 

Lavash standart pishloqli 33 000 x  {sonLavashpishloqli['count']} = {summalavashpishloqli}
Umumiy: {summalavashpishloqli} UZS"""

        await call.message.edit_media(
            media=types.InputMediaPhoto(open('images/lavashpishloqli.jpg', 'rb'), caption=new_caption),
            reply_markup=Lavash_pishloqli
        )
    else:
        await call.answer("1dan kam mahsulot tanlash mumkin emas")


#-----------------------------------------------------------------------------------------------------------------------

sonLavashachchiq = {
    'count': 1,
}


@dp.message_handler(text="Lavash standart achchiq")
async def lavashachchiq(message: types.Message):
    await message.answer("Mahsulot miqdorini tanlang")
    await message.answer_photo(photo=open('images/lavashachchiq.jpg', 'rb'), caption="""
Lavash standart achchiq 
Lavash xamiri, mol go'shti donar, pomidor, kartoshkali chipslar, tomat sousi, mayonez, halapeno 

Lavash standart achchiq 30 000 x 1 = 30 000
Umumiy: 30 000 UZS""", reply_markup=Lavash_achchiq)


@dp.callback_query_handler(text='pluslavashachchiq')
async def plusLavashachchiq(call: types.CallbackQuery):
    print(sonLavashpishloqli)
    sonLavashachchiq['count'] += 1

    Lavash_achchiq = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minuslavashachchiq"),
                InlineKeyboardButton(text=str(sonLavashachchiq['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="pluslavashachchiq")
            ],
            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ]
        ]
    )

    summalavashachchiq = 30000 * sonLavashachchiq['count']
    new_caption = f"""
Lavash standart achchiq 
Lavash xamiri, mol go'shti donar, pomidor, kartoshkali chipslar, tomat sousi, mayonez, halapeno

Lavash standart achchiq 30 000 x {sonLavashachchiq['count']} = {summalavashachchiq}
Umumiy: {summalavashachchiq} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/lavashachchiq.jpg', 'rb'), chat_id=call.message.chat.id,
                                    message_id=call.message.message_id, caption=new_caption
                                    ), reply_markup=Lavash_achchiq,
    )


@dp.callback_query_handler(text='minuslavashachchiq')
async def minusLavashachchiq(call: types.CallbackQuery):
    print(sonLavashachchiq)

    if sonLavashachchiq['count'] > 1:
        sonLavashachchiq['count'] -= 1

        Lavash_achchiq = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="minuslavashachchiq"),
                    InlineKeyboardButton(text=str(sonLavashachchiq['count']), callback_data='0'),
                    InlineKeyboardButton(text='+', callback_data="pluslavashachchiq")
                ],

                [
                    InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
                ]
            ]
        )

        summalavashachchiq = 30000 * sonLavashachchiq['count']
        new_caption = f"""
Lavash standart achchiq 
Lavash xamiri, mol go'shti donar, pomidor, kartoshkali chipslar, tomat sousi, mayonez, halapeno

Lavash standart achchiq 30 000 x {sonLavashachchiq['count']} = {summalavashachchiq}
Umumiy: {summalavashachchiq} UZS"""

        await call.message.edit_media(
            media=types.InputMediaPhoto(open('images/lavashachchiq.jpg', 'rb'), caption=new_caption),
            reply_markup=Lavash_achchiq
        )
    else:
        await call.answer("1dan kam mahsulot tanlash mumkin emas")

#-----------------------------------------------------------------------------------------------------------------------


sonLavashmini = {
    'count': 1,
}


@dp.message_handler(text="Lavash mini klassik")
async def lavashmini(message: types.Message):
    await message.answer("Mahsulot miqdorini tanlang")
    await message.answer_photo(photo=open('images/lavashmini.jpg', 'rb'), caption="""
Lavash mini klassik 
Lavash xamiri, mol go'shti-donar, pomidor, chipslar, pomidor sousi, mayonez 

Lavash mini klassik 25 000 x 1 = 25 000
Umumiy: 25 000 UZS""", reply_markup=Lavash_mini)


@dp.callback_query_handler(text='pluslavashmini')
async def plusLavashmini(call: types.CallbackQuery):
    print(sonLavashmini)
    sonLavashmini['count'] += 1

    Lavash_mini = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minuslavashmini"),
                InlineKeyboardButton(text=str(sonLavashmini['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="pluslavashmini")
            ],
            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ]
        ]
    )

    summalavashmini = 25000 * sonLavashmini['count']
    new_caption = f"""
Lavash mini klassik 
Lavash xamiri, mol go'shti-donar, pomidor, chipslar, pomidor sousi, mayonez 

Lavash mini klassik 25 000 x  {sonLavashmini['count']} = {summalavashmini}
Umumiy: {summalavashmini} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/lavashmini.jpg', 'rb'), chat_id=call.message.chat.id,
                                    message_id=call.message.message_id, caption=new_caption
                                    ), reply_markup=Lavash_mini,
    )


@dp.callback_query_handler(text='minuslavashmini')
async def minusLavashmini(call: types.CallbackQuery):
    print(sonLavashmini)

    if sonLavashmini['count'] > 1:
        sonLavashmini['count'] -= 1

        Lavash_mini = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="minuslavashmini"),
                    InlineKeyboardButton(text=str(sonLavashmini['count']), callback_data='0'),
                    InlineKeyboardButton(text='+', callback_data="pluslavashmini")
                ],

                [
                    InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
                ]
            ]
        )

        summalavashmini = 25000 * sonLavashmini['count']
        new_caption = f"""
Lavash mini klassik 
Lavash xamiri, mol go'shti-donar, pomidor, chipslar, pomidor sousi, mayonez 

Lavash mini klassik 25 000 x  {sonLavashmini['count']} = {summalavashmini}
Umumiy: {summalavashmini} UZS"""

        await call.message.edit_media(
            media=types.InputMediaPhoto(open('images/lavashmini.jpg', 'rb'), caption=new_caption),
            reply_markup=Lavash_mini
        )
    else:
        await call.answer("1dan kam mahsulot tanlash mumkin emas")


#-----------------------------------------------------------------------------------------------------------------------



sonLavashminip = {
    'count': 1,
}


@dp.message_handler(text="Lavash mini pishloqli")
async def lavashminip(message: types.Message):
    await message.answer("Mahsulot miqdorini tanlang")
    await message.answer_photo(photo=open('images/lavashminip.jpg', 'rb'), caption="""
Lavash mini pishloqli 
Lavash xamiri, mol go'shti-donar, pomidor, chipslar, pomidor sousi, mayonez, Xoxland pishloq 

Lavash mini pishloqli 28 000 x 1 = 28 000
Umumiy: 28 000 UZS""", reply_markup=Lavash_minip)


@dp.callback_query_handler(text='pluslavashminip')
async def plusLavashminip(call: types.CallbackQuery):
    print(sonLavashminip)
    sonLavashminip['count'] += 1

    Lavash_minip = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minuslavashminip"),
                InlineKeyboardButton(text=str(sonLavashminip['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="pluslavashminip")
            ],
            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ]
        ]
    )

    summalavashminip = 28000 * sonLavashminip['count']
    new_caption = f"""
Lavash mini pishloqli 
Lavash xamiri, mol go'shti-donar, pomidor, chipslar, pomidor sousi, mayonez, Xoxland pishloq 

Lavash mini pishloqli 28 000 x {sonLavashminip['count']} = {summalavashminip}
Umumiy: {summalavashminip} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/lavashminip.jpg', 'rb'), chat_id=call.message.chat.id,
                                    message_id=call.message.message_id, caption=new_caption
                                    ), reply_markup=Lavash_minip,
    )


@dp.callback_query_handler(text='minuslavashminip')
async def minusLavashminip(call: types.CallbackQuery):
    print(sonLavashminip)

    if sonLavashminip['count'] > 1:
        sonLavashminip['count'] -= 1

        Lavash_minip = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="minuslavashminip"),
                    InlineKeyboardButton(text=str(sonLavashminip['count']), callback_data='0'),
                    InlineKeyboardButton(text='+', callback_data="pluslavashminip")
                ],

                [
                    InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
                ]
            ]
        )

        summalavashminip = 28000 * sonLavashminip['count']
        new_caption = f"""
Lavash mini pishloqli 
Lavash xamiri, mol go'shti-donar, pomidor, chipslar, pomidor sousi, mayonez, Xoxland pishloq

Lavash mini pishloqli 28 000 x {sonLavashminip['count']} = {summalavashminip}
Umumiy: {summalavashminip} UZS"""

        await call.message.edit_media(
            media=types.InputMediaPhoto(open('images/lavashminip.jpg', 'rb'), caption=new_caption),
            reply_markup=Lavash_minip
        )
    else:
        await call.answer("1dan kam mahsulot tanlash mumkin emas")
