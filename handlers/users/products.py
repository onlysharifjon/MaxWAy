from keyboards.default.menubuttons import sous
from keyboards.inline.inline_buttons import Maxi_BOX_Traditsiya
from loader import dp
from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

son = {
    'count': 1,
    'kichik_kartorshka_fri': "kichik kartoshka-fri",
    'fri_caption': """
kartoshka-fri :
  - kichik kartoshka-fri      0 x 1 = 0  
""",
    'sarimsoq_caption': """""",
}
fri_narx = {}

ketchup = {'user_id': True}
pishloqli_sous = {'user_id': True}
sarimsoqli_sous = {'user_id': True}


def sous_checker(user_id):
    if user_id in sarimsoqli_sous.keys():
        if '✅' in sarimsoqli_sous[user_id]:
            return """
siz tanlagan sous :
- sarimsoqli sous      0 x 1 = 0  
    """
        else:
            return ''
    if user_id in pishloqli_sous.keys():
        if '✅' in pishloqli_sous[user_id]:
            return """
siz tanlagan sous :
- pishloqli sous      0 x 1 = 0  
    """
        else:
            return ''
    if user_id in ketchup.keys():
        if '✅' in ketchup[user_id]:
            return """
siz tanlagan sous :
- ketchup       0 x 1 = 0
    """
        else:
            return ''


@dp.message_handler(text="Maxi BOX Traditsiya")
async def maxi_box_traditsiya(message: types.Message):
    ketchup[message.from_user.id] = ''
    sarimsoqli_sous[message.from_user.id] = ''
    pishloqli_sous[message.from_user.id] = ''

    await message.answer("Mahsulot miqdorini tanlang")
    await message.answer_photo(photo=open('images/MaxiBOXTraditsiya.png', 'rb'), caption="""Maxi BOX Traditsiya
Original sendvich, kartoshka fri, 0,4 l coca cola, tanlash uchun sous

Maxi BOX Traditsiya 45 000 x 1 = 45 000

Umumiy: 45 000 UZS""", reply_markup=Maxi_BOX_Traditsiya)


@dp.callback_query_handler(text='plus')
async def plusmaxibox(call: types.CallbackQuery):
    if call.message.chat.id not in son.keys():
        son[call.message.chat.id] = "kichik kartoshka-fri"
    else:
        if '✅' in son[call.message.chat.id]:
            son[call.message.chat.id] = "✅kichik kartoshka-fri"
        else:
            son[call.message.chat.id] = "kichik kartoshka-fri"

    print(son)
    son['count'] += 1

    if call.message.chat.id in sarimsoqli_sous:
        if 'sarimsoqli sous' in sarimsoqli_sous[call.message.chat.id]:
            button_text = sarimsoqli_sous[call.message.chat.id]
        else:
            button_text = "sarimsoqli_sous"
    else:
        button_text = "sarimsoqli_sous"

    Maxi_BOX_Traditsiya = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minus"),
                InlineKeyboardButton(text=str(son['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plus")
            ],
            [
                InlineKeyboardButton(text="⬇️ kartoshka-fri ⬇️", callback_data="0")
            ],
            {
                InlineKeyboardButton(text=son[call.message.chat.id], callback_data="kichik_kartoshka_fri")
            },
            [
                InlineKeyboardButton(text="⬇️ Siz tanlagan sous ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=f'{button_text}', callback_data="sarimsoqli_sous"),
                InlineKeyboardButton(text="Pishloqli sous", callback_data="pishloqli_sous"),
                InlineKeyboardButton(text="Ketchup", callback_data="ketchup")
            ],
            [
                InlineKeyboardButton(text="⬇️ Ichimlik ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text="Quyma cola", callback_data="quyma_cola"),
                InlineKeyboardButton(text="Limonli choy", callback_data="limonli_choy")
            ],
            [
                InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save")
            ]
        ]
    )
    if call.message.chat.id not in fri_narx.keys():
        a = ''
    else:
        a = fri_narx[call.message.chat.id]

    summa = 45000 * son['count']
    new_caption = f"""Maxi BOX Traditsiya
Original sendvich, kartoshka fri, 0.4L coca cola, tanlash uchun sous

Maxi BOX Traditsiya 45 000 x {son['count']} = {summa}
{a}
{sous_checker(call.message.chat.id)}
Umumiy: {summa} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/MaxiBOXTraditsiya.png', 'rb'), chat_id=call.message.chat.id,
                                    message_id=call.message.message_id, caption=new_caption
                                    ), reply_markup=Maxi_BOX_Traditsiya,
    )


@dp.callback_query_handler(text='minus')
async def minusmaxibox(call: types.CallbackQuery):
    print(son)
    try:
        if son['count'] > 1:
            son['count'] -= 1

            if call.message.chat.id in sarimsoqli_sous:
                if 'sarimsoqli sous' in sarimsoqli_sous[call.message.chat.id]:
                    button_text = sarimsoqli_sous[call.message.chat.id]
                else:
                    button_text = "sarimsoqli_sous"
            else:
                button_text = "sarimsoqli_sous"

            Maxi_BOX_Traditsiya = InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        InlineKeyboardButton(text='-', callback_data="minus"),
                        InlineKeyboardButton(text=str(son['count']), callback_data='0'),
                        InlineKeyboardButton(text='+', callback_data="plus")
                    ],
                    [
                        InlineKeyboardButton(text="⬇️ kartoshka-fri ⬇️", callback_data="0")
                    ],
                    [
                        InlineKeyboardButton(text=son[call.message.chat.id], callback_data="kichik_kartoshka_fri")
                    ],
                    [
                        InlineKeyboardButton(text="⬇️ Siz tanlagan sous ⬇️", callback_data="0")
                    ],
                    [
                        InlineKeyboardButton(text=f"""{button_text}""", callback_data="sarimsoqli_sous"),
                        InlineKeyboardButton(text="Pishloqli sous", callback_data="pishloqli_sous"),
                        InlineKeyboardButton(text="Ketchup", callback_data="ketchup")
                    ],
                    [
                        InlineKeyboardButton(text="⬇️ Ichimlik ⬇️", callback_data="0")
                    ],
                    [
                        InlineKeyboardButton(text="Quyma cola", callback_data="quyma_cola"),
                        InlineKeyboardButton(text="Limonli choy", callback_data="limonli_choy")
                    ],
                    [
                        InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save")
                    ]
                ]
            )

            if call.message.chat.id not in fri_narx.keys():
                a = ''
            else:
                a = fri_narx[call.message.chat.id]

            summa = 45000 * son['count']
            new_caption = f"""
Maxi BOX Traditsiya
Original sendvich, kartoshka fri, 0.4L coca cola, tanlash uchun sous

Maxi BOX Traditsiya 45 000 x {son['count']} = {summa}
{a}
{sous_checker(call.message.chat.id)}
Umumiy: {summa} UZS"""

            await call.message.edit_media(
                media=types.InputMediaPhoto(open('images/MaxiBOXTraditsiya.png', 'rb'), caption=new_caption),
                reply_markup=Maxi_BOX_Traditsiya
            )
        else:
            await call.answer("1dan kam mahsulot tanlash mumkin emas")
    except:
        await call.answer("Nimadir xato ketdi. Iltimos, qaytadan urinib ko'ring.")


@dp.callback_query_handler(text='kichik_kartoshka_fri')
async def kichikfri(call: types.CallbackQuery):
    if call.message.chat.id not in fri_narx.keys():
        fri_narx[call.message.chat.id] = '''
kartoshka-fri :
  - kichik kartoshka-fri      0 x 1 = 0  
        '''
    else:
        del fri_narx[call.message.chat.id]
    # try:
    #     print(son[call.message.chat.id])
    # except:
    #     son[call.message.chat.id] = "✅kichik kartoshka-fri"

    if call.message.chat.id in son.keys():

        if '✅' not in son[call.message.chat.id]:
            son[call.message.chat.id] = "✅kichik kartoshka-fri"
        else:
            son[call.message.chat.id] = "kichik kartoshka-fri"

    else:
        son[call.message.chat.id] = "✅kichik kartoshka-fri"

    if call.message.chat.id in sarimsoqli_sous:
        if 'sarimsoqli sous' in sarimsoqli_sous[call.message.chat.id]:
            button_text = sarimsoqli_sous[call.message.chat.id]
        else:
            button_text = "sarimsoqli_sous"
    else:
        button_text = "sarimsoqli_sous"

    update_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minus"),
                InlineKeyboardButton(text=str(son['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plus")
            ],
            [
                InlineKeyboardButton(text="⬇️ kartoshka-fri ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=son[call.message.chat.id], callback_data="kichik_kartoshka_fri")
            ],
            [
                InlineKeyboardButton(text="⬇️siz tanlagan sous⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=f"""{button_text}""", callback_data="sarimsoqli_sous"),
                InlineKeyboardButton(text="pishloqli sous", callback_data="pishloqli_sous"),
                InlineKeyboardButton(text="ketchup", callback_data="ketchup")
            ],

            [
                InlineKeyboardButton(text="⬇️ichimlik⬇️", callback_data="0")
            ],

            [
                InlineKeyboardButton(text="quyma cola", callback_data="quyma_cola"),
                InlineKeyboardButton(text="limonli choy", callback_data="limonli_choy")
            ],

            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ],

        ]
    )
    summa = 45000 * son['count']
    global check
    print(son[call.message.chat.id])
    if '✅' in son[call.message.chat.id]:
        check = son['fri_caption']
    else:
        check = ''

    new_caption = f"""
Maxi BOX Traditsiya
Original sendvich, kartoshka fri, 0.4L coca cola, tanlash uchun sous

Maxi BOX Traditsiya 45 000 x {son['count']} = {summa}
{check}
{sous_checker(call.message.chat.id)}
Umumiy: {summa} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/MaxiBOXTraditsiya.png', 'rb'), caption=new_caption),
        reply_markup=update_button
    )
    print(son)


@dp.callback_query_handler(text='sarimsoqli_sous')
async def sous1(call: types.CallbackQuery):
    global check
    if call.message.chat.id in son.keys():

        if '✅' not in sarimsoqli_sous[call.message.chat.id]:
            sarimsoqli_sous[call.message.chat.id] = "✅sarimsoqli sous"
        else:
            sarimsoqli_sous[call.message.chat.id] = "sarimsoqli sous"

    else:
        sarimsoqli_sous[call.message.chat.id] = "✅sarimsoqli sous"

    update_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minus"),
                InlineKeyboardButton(text=str(son['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plus")
            ],
            [
                InlineKeyboardButton(text="⬇️ kartoshka-fri ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=son[call.message.chat.id], callback_data="kichik_kartoshka_fri")
            ],
            [
                InlineKeyboardButton(text="⬇️siz tanlagan sous⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=f"{sarimsoqli_sous[call.message.chat.id]}", callback_data="sarimsoqli_sous"),
                InlineKeyboardButton(text=f"pishloqli sous", callback_data="pishloqli_sous"),
                InlineKeyboardButton(text=f"ketchup", callback_data="ketchup")
            ],

            [
                InlineKeyboardButton(text="⬇️ichimlik⬇️", callback_data="0")
            ],

            [
                InlineKeyboardButton(text="quyma cola", callback_data="quyma_cola"),
                InlineKeyboardButton(text="limonli choy", callback_data="limonli_choy")
            ],

            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ],

        ]
    )

    summa = 45000 * son['count']

    new_caption = f"""Maxi BOX Traditsiya
        Original sendvich, kartoshka fri, 0.4L coca cola, tanlash uchun sous

        Maxi BOX Traditsiya 45 000 x {son['count']} = {summa}
        {check}

        {sous_checker(call.message.chat.id)}
        Umumiy: {summa} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/MaxiBOXTraditsiya.png', 'rb'), caption=new_caption),
        reply_markup=update_button,
        # message_id=call.message.message_id,
        # chat_id=call.message.chat.id
    )


@dp.callback_query_handler(text='pishloqli_sous')
async def sous1(call: types.CallbackQuery):
    global check

    sarimsoqli_sous[call.message.chat.id] = "sarimsoqli sous"
    ketchup[call.message.chat.id] = 'ketchup'



    if call.message.chat.id in son.keys():

        if '✅' not in pishloqli_sous[call.message.chat.id]:
            pishloqli_sous[call.message.chat.id] = "✅pishloqli sous"
        else:
            pishloqli_sous[call.message.chat.id] = "pishloqli sous"

    else:
        pishloqli_sous[call.message.chat.id] = "✅pishloqli sous"




    update_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minus"),
                InlineKeyboardButton(text=str(son['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plus")
            ],
            [
                InlineKeyboardButton(text="⬇️ kartoshka-fri ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=son[call.message.chat.id], callback_data="kichik_kartoshka_fri")
            ],
            [
                InlineKeyboardButton(text="⬇️siz tanlagan sous⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=f"{sarimsoqli_sous[call.message.chat.id]}", callback_data="sarimsoqli_sous"),
                InlineKeyboardButton(text=f"{pishloqli_sous[call.message.chat.id]}", callback_data="pishloqli_sous"),
                InlineKeyboardButton(text=f"ketchup", callback_data="ketchup")
            ],

            [
                InlineKeyboardButton(text="⬇️ichimlik⬇️", callback_data="0")
            ],

            [
                InlineKeyboardButton(text="quyma cola", callback_data="quyma_cola"),
                InlineKeyboardButton(text="limonli choy", callback_data="limonli_choy")
            ],

            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ],

        ]
    )

    summa = 45000 * son['count']

    new_caption = f"""Maxi BOX Traditsiya
        Original sendvich, kartoshka fri, 0.4L coca cola, tanlash uchun sous

        Maxi BOX Traditsiya 45 000 x {son['count']} = {summa}
        {check}

        {sous_checker(call.message.chat.id)}
        Umumiy: {summa} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/MaxiBOXTraditsiya.png', 'rb'), caption=new_caption),
        reply_markup=update_button,
        # message_id=call.message.message_id,
        # chat_id=call.message.chat.id
    )
