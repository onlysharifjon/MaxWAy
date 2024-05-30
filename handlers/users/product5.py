from keyboards.default.menubuttons import sous
from keyboards.inline.inline_buttons import MaxiBoxTrend
from loader import dp
from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

checktrend = None
sontrend = {
    'count': 1,
    'kichik_kartorshka_fri': "kichik kartoshka-fri",
    'fri_caption': """
kartoshka-fri :
  - kichik kartoshka-fri      0 x 1 = 0  
""",
    'sarimsoq_caption': """""",
}
fri_narxtrend = {}

ketchuptrend = {'user_id': True}
pishloqli_soustrend = {'user_id': True}
sarimsoqli_soustrend = {'user_id': True}
quyma_colatrend = {'user_id':True}
limonli_choytrend = {'user_id':True}
def ssous_checkertrend(user_id):
    if user_id in sarimsoqli_soustrend.keys():
        if '✅' in sarimsoqli_soustrend[user_id]:
            return """
siz tanlagan sous :
- sarimsoqli sous      0 x 1 = 0  
    """
        else:
            return ''


def psous_checkertrend(user_id):
    if user_id in pishloqli_soustrend.keys():
        if '✅' in pishloqli_soustrend[user_id]:
            return """
siz tanlagan sous :
- pishloqli sous      0 x 1 = 0  
        """
        else:
            return ''


def ketchup_checkertrend(user_id):
    if user_id in ketchuptrend.keys():
        if '✅' in ketchuptrend[user_id]:
            return """
siz tanlagan sous :
- ketchup       0 x 1 = 0
        """
        else:
            return ''

def quyma_cola_checkertrend(user_id):
    if user_id in quyma_colatrend.keys():
        if '✅' in quyma_colatrend[user_id]:
            return """
ichimlik :
  - quyma cola       0 x 1 = 0
    """
        else:
            return ''

def limonli_choy_checkertrend(user_id):
    if user_id in limonli_choytrend.keys():
        if '✅' in limonli_choytrend[user_id]:
            return """
ichimlik :
  - limonli choy      0 x 1 = 0
    """
        else:
            return ''


@dp.message_handler(text="Maxi BOX Trend")
async def maxi_box_trend(message: types.Message):
    ketchuptrend[message.from_user.id] = ''
    sarimsoqli_soustrend[message.from_user.id] = ''
    pishloqli_soustrend[message.from_user.id] = ''
    quyma_colatrend[message.from_user.id] = ''
    limonli_choytrend[message.from_user.id]=''

    await message.answer("Mahsulot miqdorini tanlang")
    await message.answer_photo(photo=open('images/MaxiBoxTrend.jpg', 'rb'), caption="""
Maxi BOX Trend 
Gamburger,  kartoshka fri, 0,4 l coca cola, tanlash uchun sous

Maxi BOX Trend 40 000 x 1 = 40 000

Umumiy: 40 000 UZS""", reply_markup=MaxiBoxTrend)


@dp.callback_query_handler(text='plustrend')
async def plusmaxiboxtrend(call: types.CallbackQuery):
    if call.message.chat.id not in sontrend.keys():
        sontrend[call.message.chat.id] = "kichik kartoshka-fri"
    else:
        if '✅' in sontrend[call.message.chat.id]:
            sontrend[call.message.chat.id] = "✅kichik kartoshka-fri"
        else:
            sontrend[call.message.chat.id] = "kichik kartoshka-fri"

    print(sontrend)
    sontrend['count'] += 1

    if call.message.chat.id in sarimsoqli_soustrend:
        if 'sarimsoqli sous' in sarimsoqli_soustrend[call.message.chat.id]:
            button_text = sarimsoqli_soustrend[call.message.chat.id]
        else:
            button_text = "sarimsoqli sous"
    else:
        button_text = "sarimsoqli sous"

    if call.message.chat.id in pishloqli_soustrend:
        if 'pishloqli sous' in pishloqli_soustrend[call.message.chat.id]:
            p_text = pishloqli_soustrend[call.message.chat.id]
        else:
            p_text = "pishloqli sous"
    else:
        p_text = "pishloqli sous"

    if call.message.chat.id in ketchuptrend:
        if 'ketchup' in ketchuptrend[call.message.chat.id]:
            k_text = ketchuptrend[call.message.chat.id]
        else:
            k_text = "ketchup"
    else:
        k_text = "ketchup"

    if call.message.chat.id in quyma_colatrend:
        if 'quyma cola' in quyma_colatrend[call.message.chat.id]:
            cola_text = quyma_colatrend[call.message.chat.id]
        else:
            cola_text = "quyma cola"
    else:
        cola_text = "quyma cola"

    if call.message.chat.id in limonli_choytrend:
        if 'limonli choy' in limonli_choytrend[call.message.chat.id]:
            limonli_text = limonli_choytrend[call.message.chat.id]
        else:
            limonli_text = "limonli choy"
    else:
        limonli_text = "limonli choy"

    MaxiBoxTrend = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minustrend"),
                InlineKeyboardButton(text=str(sontrend['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plustrend")
            ],
            [
                InlineKeyboardButton(text="⬇️ kartoshka-fri ⬇️", callback_data="0")
            ],
            {
                InlineKeyboardButton(text=sontrend[call.message.chat.id], callback_data="kichik_kartoshka_fritrend")
            },
            [
                InlineKeyboardButton(text="⬇️ siz tanlagan sous ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=f'{button_text}', callback_data="sarimsoqli_soustrend"),
                InlineKeyboardButton(text=f'{p_text}', callback_data="pishloqli_soustrend"),
                InlineKeyboardButton(text=f'{k_text}', callback_data="ketchuptrend")
            ],
            [
                InlineKeyboardButton(text="⬇️ ichimlik ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=f'{cola_text}', callback_data="quyma_colatrend"),
                InlineKeyboardButton(text=f'{limonli_text}', callback_data="limonli_choytrend")
            ],
            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ]
        ]
    )
    if call.message.chat.id not in fri_narxtrend.keys():
        a = ''
    else:
        a = fri_narxtrend[call.message.chat.id]

    summa = 40000 * sontrend['count']
    new_caption = f"""
Maxi BOX Trend 
Gamburger,  kartoshka fri, 0,4 l coca cola, tanlash uchun sous

Maxi BOX Trend 40 000 x {sontrend['count']} = {summa}
{a}
{ssous_checkertrend(call.message.chat.id)}
{psous_checkertrend(call.message.chat.id)}
{ketchup_checkertrend(call.message.chat.id)}
{quyma_cola_checkertrend(call.message.chat.id)}
{limonli_choy_checkertrend(call.message.chat.id)}
Umumiy: {summa} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/MaxiBoxTrend.jpg', 'rb'), chat_id=call.message.chat.id,
                                    message_id=call.message.message_id, caption=new_caption
                                    ), reply_markup=MaxiBoxTrend,
    )


@dp.callback_query_handler(text='minustrend')
async def minusmaxiboxtrend(call: types.CallbackQuery):
    print(sontrend)

    if sontrend['count'] > 1:
        sontrend['count'] -= 1

        if call.message.chat.id in sarimsoqli_soustrend:
            if 'sarimsoqli sous' in sarimsoqli_soustrend[call.message.chat.id]:
                button_text = sarimsoqli_soustrend[call.message.chat.id]
            else:
                button_text = "sarimsoqli sous"
        else:
            button_text = "sarimsoqli sous"

        if call.message.chat.id in pishloqli_soustrend:
            if 'pishloqli sous' in pishloqli_soustrend[call.message.chat.id]:
                p_text = pishloqli_soustrend[call.message.chat.id]
            else:
                p_text = "pishloqli sous"
        else:
            p_text = "pishloqli sous"

        if call.message.chat.id in ketchuptrend:
            if 'ketchup' in ketchuptrend[call.message.chat.id]:
                k_text = ketchuptrend[call.message.chat.id]
            else:
                k_text = "ketchup"
        else:
            k_text = "ketchup"

        if call.message.chat.id in quyma_colatrend:
            if 'quyma cola' in quyma_colatrend[call.message.chat.id]:
                cola_text = quyma_colatrend[call.message.chat.id]
            else:
                cola_text = "quyma cola"
        else:
            cola_text = "quyma cola"

        if call.message.chat.id in limonli_choytrend:
            if 'limonli choy' in limonli_choytrend[call.message.chat.id]:
                limonli_text = limonli_choytrend[call.message.chat.id]
            else:
                limonli_text = "limonli choy"
        else:
            limonli_text = "limonli choy"

        MaxiBoxTrend = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="minustrend"),
                    InlineKeyboardButton(text=str(sontrend['count']), callback_data='0'),
                    InlineKeyboardButton(text='+', callback_data="plustrend")
                ],
                [
                    InlineKeyboardButton(text="⬇️ kartoshka-fri ⬇️", callback_data="0")
                ],
                [
                    InlineKeyboardButton(text=sontrend[call.message.chat.id], callback_data="kichik_kartoshka_fritrend")
                ],
                [
                    InlineKeyboardButton(text="⬇️ siz tanlagan sous ⬇️", callback_data="0")
                ],
                [
                    InlineKeyboardButton(text=f"""{button_text}""", callback_data="sarimsoqli_soustrend"),
                    InlineKeyboardButton(text=f'{p_text}', callback_data="pishloqli_soustrend"),
                    InlineKeyboardButton(text=f'{k_text}', callback_data="ketchuptrend")
                ],
                [
                    InlineKeyboardButton(text="⬇️ ichimlik ⬇️", callback_data="0")
                ],
                [
                    InlineKeyboardButton(text=f'{cola_text}', callback_data="quyma_colatrend"),
                    InlineKeyboardButton(text=f'{limonli_text}', callback_data="limonli_choytrend")
                ],
                [
                    InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
                ]
            ]
        )

        if call.message.chat.id not in fri_narxtrend.keys():
            a = ''
        else:
            a = fri_narxtrend[call.message.chat.id]

        summa = 40000 * sontrend['count']
        new_caption = f"""
Maxi BOX Trend 
Gamburger,  kartoshka fri, 0,4 l coca cola, tanlash uchun sous

Maxi BOX Trend 40 000 x {sontrend['count']} = {summa}
{a}
{ssous_checkertrend(call.message.chat.id)}
{psous_checkertrend(call.message.chat.id)}
{ketchup_checkertrend(call.message.chat.id)}
{quyma_cola_checkertrend(call.message.chat.id)}
{limonli_choy_checkertrend(call.message.chat.id)}
Umumiy: {summa} UZS"""

        await call.message.edit_media(
            media=types.InputMediaPhoto(open('images/MaxiBoxTrend.jpg', 'rb'), caption=new_caption),
            reply_markup=MaxiBoxTrend
        )
    else:
        await call.answer("1dan kam mahsulot tanlash mumkin emas")



@dp.callback_query_handler(text='kichik_kartoshka_fritrend')
async def kichikfritrend(call: types.CallbackQuery):
    if call.message.chat.id not in fri_narxtrend.keys():
        fri_narxtrend[call.message.chat.id] = '''
kartoshka-fri :
  - kichik kartoshka-fri      0 x 1 = 0  
        '''
    else:
        del fri_narxtrend[call.message.chat.id]
    # try:
    #     print(son[call.message.chat.id])
    # except:
    #     son[call.message.chat.id] = "✅kichik kartoshka-fri"

    if call.message.chat.id in sontrend.keys():

        if '✅' not in sontrend[call.message.chat.id]:
            sontrend[call.message.chat.id] = "✅kichik kartoshka-fri"
        else:
            sontrend[call.message.chat.id] = "kichik kartoshka-fri"

    else:
        sontrend[call.message.chat.id] = "✅kichik kartoshka-fri"

    if call.message.chat.id in sarimsoqli_soustrend:
        if 'sarimsoqli sous' in sarimsoqli_soustrend[call.message.chat.id]:
            button_text = sarimsoqli_soustrend[call.message.chat.id]
        else:
            button_text = "sarimsoqli sous"
    else:
        button_text = "sarimsoqli sous"

    if call.message.chat.id in pishloqli_soustrend:
        if 'pishloqli sous' in pishloqli_soustrend[call.message.chat.id]:
            p_text = pishloqli_soustrend[call.message.chat.id]
        else:
            p_text = "pishloqli sous"
    else:
        p_text = "pishloqli sous"

    if call.message.chat.id in ketchuptrend:
        if 'ketchup' in ketchuptrend[call.message.chat.id]:
            k_text = ketchuptrend[call.message.chat.id]
        else:
            k_text = "ketchup"
    else:
        k_text = "ketchup"

    if call.message.chat.id in quyma_colatrend:
        if 'quyma cola' in quyma_colatrend[call.message.chat.id]:
            cola_text = quyma_colatrend[call.message.chat.id]
        else:
            cola_text = "quyma cola"
    else:
        cola_text = "quyma cola"

    if call.message.chat.id in limonli_choytrend:
        if 'limonli choy' in limonli_choytrend[call.message.chat.id]:
            limonli_text = limonli_choytrend[call.message.chat.id]
        else:
            limonli_text = "limonli choy"
    else:
        limonli_text = "limonli choy"

    update_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minustrend"),
                InlineKeyboardButton(text=str(sontrend['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plustrend")
            ],
            [
                InlineKeyboardButton(text="⬇️ kartoshka-fri ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=sontrend[call.message.chat.id], callback_data="kichik_kartoshka_fritrend")
            ],
            [
                InlineKeyboardButton(text="⬇️ siz tanlagan sous ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=f'{button_text}', callback_data="sarimsoqli_soustrend"),
                InlineKeyboardButton(text=f'{p_text}', callback_data="pishloqli_soustrend"),
                InlineKeyboardButton(text=f'{k_text}', callback_data="ketchuptrend")
            ],

            [
                InlineKeyboardButton(text="⬇️ ichimlik ⬇️", callback_data="0")
            ],

            [
                InlineKeyboardButton(text=f'{cola_text}', callback_data="quyma_colatrend"),
                InlineKeyboardButton(text=f'{limonli_text}', callback_data="limonli_choytrend")
            ],

            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ],

        ]
    )
    summa = 40000 * sontrend['count']
    global checktrend
    print(sontrend[call.message.chat.id])
    if '✅' in sontrend[call.message.chat.id]:
        checktrend = sontrend['fri_caption']
    else:
        checktrend = ''

    new_caption = f"""
Maxi BOX Trend 
Gamburger,  kartoshka fri, 0,4 l coca cola, tanlash uchun sous

Maxi BOX Trend 40 000 x {sontrend['count']} = {summa}
{checktrend}
{ssous_checkertrend(call.message.chat.id)}
{psous_checkertrend(call.message.chat.id)}
{ketchup_checkertrend(call.message.chat.id)}
{quyma_cola_checkertrend(call.message.chat.id)}
{limonli_choy_checkertrend(call.message.chat.id)}
Umumiy: {summa} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/MaxiBoxTrend.jpg', 'rb'), caption=new_caption),
        reply_markup=update_button
    )
    print(sontrend)


@dp.callback_query_handler(text='sarimsoqli_soustrend')
async def sous1trend(call: types.CallbackQuery):
    pishloqli_soustrend[call.message.chat.id] = "pishloqli sous"
    ketchuptrend[call.message.chat.id] = 'ketchup'

    if call.message.chat.id in sontrend.keys():

        if '✅' not in sarimsoqli_soustrend[call.message.chat.id]:
            sarimsoqli_soustrend[call.message.chat.id] = "✅sarimsoqli sous"
        else:
            sarimsoqli_soustrend[call.message.chat.id] = "sarimsoqli sous"

    else:
        sarimsoqli_soustrend[call.message.chat.id] = "✅sarimsoqli sous"
    if call.message.chat.id not in sontrend.keys():
        sontrend[call.message.chat.id] = "kichik kartoshka-fri"

    if call.message.chat.id in quyma_colatrend:
        if 'quyma cola' in quyma_colatrend[call.message.chat.id]:
            cola_text = quyma_colatrend[call.message.chat.id]
        else:
            cola_text = "quyma cola"
    else:
        cola_text = "quyma cola"

    if call.message.chat.id in limonli_choytrend:
        if 'limonli choy' in limonli_choytrend[call.message.chat.id]:
            limonli_text = limonli_choytrend[call.message.chat.id]
        else:
            limonli_text = "limonli choy"
    else:
        limonli_text = "limonli choy"

    update_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minustrend"),
                InlineKeyboardButton(text=str(sontrend['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plustrend")
            ],
            [
                InlineKeyboardButton(text="⬇️ kartoshka-fri ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=sontrend[call.message.chat.id], callback_data="kichik_kartoshka_fritrend")
            ],
            [
                InlineKeyboardButton(text="⬇️ siz tanlagan sous ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=f"{sarimsoqli_soustrend[call.message.chat.id]}", callback_data="sarimsoqli_soustrend"),
                InlineKeyboardButton(text=f"pishloqli sous", callback_data="pishloqli_soustrend"),
                InlineKeyboardButton(text=f"ketchup", callback_data="ketchuptrend")
            ],

            [
                InlineKeyboardButton(text="⬇️ ichimlik ⬇️", callback_data="0")
            ],

            [
                InlineKeyboardButton(text=f'{cola_text}', callback_data="quyma_colatrend"),
                InlineKeyboardButton(text=f'{limonli_text}', callback_data="limonli_choytrend")
            ],

            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ],

        ]
    )
    global checktrend
    summa = 40000 * sontrend['count']
    new_caption = f"""
Maxi BOX Trend 
Gamburger,  kartoshka fri, 0,4 l coca cola, tanlash uchun sous

Maxi BOX Trend 40 000 x {sontrend['count']} = {summa}
{checktrend}
{ssous_checkertrend(call.message.chat.id)}
{psous_checkertrend(call.message.chat.id)}
{ketchup_checkertrend(call.message.chat.id)}
{quyma_cola_checkertrend(call.message.chat.id)}
{limonli_choy_checkertrend(call.message.chat.id)}
Umumiy: {summa} UZS"""

    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/MaxiBoxTrend.jpg', 'rb'), caption=new_caption),
        reply_markup=update_button,
        # message_id=call.message.message_id,
        # chat_id=call.message.chat.id
    )


@dp.callback_query_handler(text='pishloqli_soustrend')
async def sous2trend(call: types.CallbackQuery):
    sarimsoqli_soustrend[call.message.chat.id] = "sarimsoqli sous"
    ketchuptrend[call.message.chat.id] = 'ketchup'

    if call.message.chat.id in sontrend.keys():

        if '✅' not in pishloqli_soustrend[call.message.chat.id]:
            pishloqli_soustrend[call.message.chat.id] = "✅pishloqli sous"
        else:
            pishloqli_soustrend[call.message.chat.id] = "pishloqli sous"

    else:
        pishloqli_soustrend[call.message.chat.id] = "✅pishloqli sous"

    if call.message.chat.id not in sontrend.keys():
        sontrend[call.message.chat.id] = "kichik kartoshka-fri"

    if call.message.chat.id in quyma_colatrend:
        if 'quyma cola' in quyma_colatrend[call.message.chat.id]:
            cola_text = quyma_colatrend[call.message.chat.id]
        else:
            cola_text = "quyma cola"
    else:
        cola_text = "quyma cola"

    if call.message.chat.id in limonli_choytrend:
        if 'limonli choy' in limonli_choytrend[call.message.chat.id]:
            limonli_text = limonli_choytrend[call.message.chat.id]
        else:
            limonli_text = "limonli choy"
    else:
        limonli_text = "limonli choy"

    update_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minustrend"),
                InlineKeyboardButton(text=str(sontrend['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plustrend")
            ],
            [
                InlineKeyboardButton(text="⬇️ kartoshka-fri ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=sontrend[call.message.chat.id], callback_data="kichik_kartoshka_fritrend")
            ],
            [
                InlineKeyboardButton(text="⬇️ siz tanlagan sous ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=f"{sarimsoqli_soustrend[call.message.chat.id]}", callback_data="sarimsoqli_soustrend"),
                InlineKeyboardButton(text=f"{pishloqli_soustrend[call.message.chat.id]}", callback_data="pishloqli_soustrend"),
                InlineKeyboardButton(text=f"ketchup", callback_data="ketchup")
            ],

            [
                InlineKeyboardButton(text="⬇️ ichimlik ⬇️", callback_data="0")
            ],

            [
                InlineKeyboardButton(text=f'{cola_text}', callback_data="quyma_colatrend"),
                InlineKeyboardButton(text=f'{limonli_text}', callback_data="limonli_choytrend")
            ],

            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ],

        ]
    )
    global checktrend
    summa = 40000 * sontrend['count']

    new_caption = f"""
Maxi BOX Trend 
Gamburger,  kartoshka fri, 0,4 l coca cola, tanlash uchun sous

Maxi BOX Trend 40 000 x {sontrend['count']} = {summa}
{checktrend}
{ssous_checkertrend(call.message.chat.id)}
{psous_checkertrend(call.message.chat.id)}
{ketchup_checkertrend(call.message.chat.id)}
{quyma_cola_checkertrend(call.message.chat.id)}
{limonli_choy_checkertrend(call.message.chat.id)}
Umumiy: {summa} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/MaxiBoxTrend.jpg', 'rb'), caption=new_caption),
        reply_markup=update_button,
        # message_id=call.message.message_id,
        # chat_id=call.message.chat.id
    )


@dp.callback_query_handler(text='ketchuptrend')
async def sous3trend(call: types.CallbackQuery):
    sarimsoqli_soustrend[call.message.chat.id] = "sarimsoqli sous"
    pishloqli_soustrend[call.message.chat.id] = 'pishloqli sous'

    if call.message.chat.id in sontrend.keys():

        if '✅' not in ketchuptrend[call.message.chat.id]:
            ketchuptrend[call.message.chat.id] = "✅ketchup"
        else:
            ketchuptrend[call.message.chat.id] = "ketchup"

    else:
        ketchuptrend[call.message.chat.id] = "✅ketchup"

    if call.message.chat.id not in sontrend.keys():
        sontrend[call.message.chat.id] = "kichik kartoshka-fri"

    if call.message.chat.id in quyma_colatrend:
        if 'quyma cola' in quyma_colatrend[call.message.chat.id]:
            cola_text = quyma_colatrend[call.message.chat.id]
        else:
            cola_text = "quyma cola"
    else:
        cola_text = "quyma cola"

    if call.message.chat.id in limonli_choytrend:
        if 'limonli choy' in limonli_choytrend[call.message.chat.id]:
            limonli_text = limonli_choytrend[call.message.chat.id]
        else:
            limonli_text = "limonli choy"
    else:
        limonli_text = "limonli choy"

    update_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minustrend"),
                InlineKeyboardButton(text=str(sontrend['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plustrend")
            ],
            [
                InlineKeyboardButton(text="⬇️ kartoshka-fri ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=sontrend[call.message.chat.id], callback_data="kichik_kartoshka_fritrend")
            ],
            [
                InlineKeyboardButton(text="⬇️ siz tanlagan sous ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=f"{sarimsoqli_soustrend[call.message.chat.id]}", callback_data="sarimsoqli_soustrend"),
                InlineKeyboardButton(text=f"{pishloqli_soustrend[call.message.chat.id]}", callback_data="pishloqli_soustrend"),
                InlineKeyboardButton(text=f"{ketchuptrend[call.message.chat.id]}", callback_data="ketchuptrend")
            ],

            [
                InlineKeyboardButton(text="⬇️ ichimlik ⬇️", callback_data="0")
            ],

            [
                InlineKeyboardButton(text=f'{cola_text}', callback_data="quyma_colatrend"),
                InlineKeyboardButton(text=f'{limonli_text}', callback_data="limonli_choytrend")
            ],

            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ],

        ]
    )
    global checktrend
    summa = 40000 * sontrend['count']

    new_caption = f"""
Maxi BOX Trend 
Gamburger,  kartoshka fri, 0,4 l coca cola, tanlash uchun sous

Maxi BOX Trend 40 000 x {sontrend['count']} = {summa}
{checktrend}
{ssous_checkertrend(call.message.chat.id)}
{psous_checkertrend(call.message.chat.id)}
{ketchup_checkertrend(call.message.chat.id)}
{quyma_cola_checkertrend(call.message.chat.id)}
{limonli_choy_checkertrend(call.message.chat.id)}
Umumiy: {summa} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/MaxiBoxTrend.jpg', 'rb'), caption=new_caption),
        reply_markup=update_button,
        # message_id=call.message.message_id,
        # chat_id=call.message.chat.id
    )


@dp.callback_query_handler(text='quyma_colatrend')
async def colatrend(call: types.CallbackQuery):
    limonli_choytrend[call.message.chat.id] = 'limonli choy'


    if call.message.chat.id in sontrend.keys():

        if '✅' not in quyma_colatrend[call.message.chat.id]:
            quyma_colatrend[call.message.chat.id] = "✅quyma cola"
        else:
            quyma_colatrend[call.message.chat.id] = "quyma cola"

    else:
        quyma_colatrend[call.message.chat.id] = "✅quyma cola"

    if call.message.chat.id in sarimsoqli_soustrend:
        if 'sarimsoqli sous' in sarimsoqli_soustrend[call.message.chat.id]:
            button_text = sarimsoqli_soustrend[call.message.chat.id]
        else:
            button_text = "sarimsoqli sous"
    else:
        button_text = "sarimsoqli sous"

    if call.message.chat.id in pishloqli_soustrend:
        if 'pishloqli sous' in pishloqli_soustrend[call.message.chat.id]:
            p_text = pishloqli_soustrend[call.message.chat.id]
        else:
            p_text = "pishloqli sous"
    else:
        p_text = "pishloqli sous"

    if call.message.chat.id in ketchuptrend:
        if 'ketchup' in ketchuptrend[call.message.chat.id]:
            k_text = ketchuptrend[call.message.chat.id]
        else:
            k_text = "ketchup"
    else:
        k_text = "ketchup"

    if call.message.chat.id not in sontrend.keys():
        sontrend[call.message.chat.id] = "kichik kartoshka-fri"

    update_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minustrend"),
                InlineKeyboardButton(text=str(sontrend['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plustrend")
            ],
            [
                InlineKeyboardButton(text="⬇️ kartoshka-fri ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=sontrend[call.message.chat.id], callback_data="kichik_kartoshka_fritrend")
            ],
            [
                InlineKeyboardButton(text="⬇️ siz tanlagan sous ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=f'{button_text}', callback_data="sarimsoqli_soustrend"),
                InlineKeyboardButton(text=f'{p_text}', callback_data="pishloqli_soustrend"),
                InlineKeyboardButton(text=f'{k_text}', callback_data="ketchuptrend")
            ],

            [
                InlineKeyboardButton(text="⬇️ ichimlik ⬇️", callback_data="0")
            ],

            [
                InlineKeyboardButton(text=f"{quyma_colatrend[call.message.chat.id]}", callback_data="quyma_colatrend"),
                InlineKeyboardButton(text="limonli choy", callback_data="limonli_choytrend")
            ],

            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ],

        ]
    )
    global checktrend
    summa = 40000 * sontrend['count']

    new_caption = f"""
Maxi BOX Trend 
Gamburger,  kartoshka fri, 0,4 l coca cola, tanlash uchun sous

Maxi BOX Trend 40 000 x {sontrend['count']} = {summa}
{checktrend}
{ssous_checkertrend(call.message.chat.id)}
{psous_checkertrend(call.message.chat.id)}
{ketchup_checkertrend(call.message.chat.id)}
{quyma_cola_checkertrend(call.message.chat.id)}
{limonli_choy_checkertrend(call.message.chat.id)}
Umumiy: {summa} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/MaxiBoxTrend.jpg', 'rb'), caption=new_caption),
        reply_markup=update_button,
        # message_id=call.message.message_id,
        # chat_id=call.message.chat.id
    )



@dp.callback_query_handler(text='limonli_choytrend')
async def limonlitrend(call: types.CallbackQuery):
    quyma_colatrend[call.message.chat.id] = 'quyma cola'


    if call.message.chat.id in sontrend.keys():

        if '✅' not in limonli_choytrend[call.message.chat.id]:
            limonli_choytrend[call.message.chat.id] = "✅limonli choy"
        else:
            limonli_choytrend[call.message.chat.id] = "limonli choy"

    else:
        limonli_choytrend[call.message.chat.id] = "✅limonli choy"

    if call.message.chat.id in sarimsoqli_soustrend:
        if 'sarimsoqli sous' in sarimsoqli_soustrend[call.message.chat.id]:
            button_text = sarimsoqli_soustrend[call.message.chat.id]
        else:
            button_text = "sarimsoqli sous"
    else:
        button_text = "sarimsoqli sous"

    if call.message.chat.id in pishloqli_soustrend:
        if 'pishloqli sous' in pishloqli_soustrend[call.message.chat.id]:
            p_text = pishloqli_soustrend[call.message.chat.id]
        else:
            p_text = "pishloqli sous"
    else:
        p_text = "pishloqli sous"

    if call.message.chat.id in ketchuptrend:
        if 'ketchup' in ketchuptrend[call.message.chat.id]:
            k_text = ketchuptrend[call.message.chat.id]
        else:
            k_text = "ketchup"
    else:
        k_text = "ketchup"

    if call.message.chat.id not in sontrend.keys():
        sontrend[call.message.chat.id] = "kichik kartoshka-fri"

    update_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minustrend"),
                InlineKeyboardButton(text=str(sontrend['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plustrend")
            ],
            [
                InlineKeyboardButton(text="⬇️ kartoshka-fri ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=sontrend[call.message.chat.id], callback_data="kichik_kartoshka_fritrend")
            ],
            [
                InlineKeyboardButton(text="⬇️ siz tanlagan sous ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=f'{button_text}', callback_data="sarimsoqli_soustrend"),
                InlineKeyboardButton(text=f'{p_text}', callback_data="pishloqli_soustrend"),
                InlineKeyboardButton(text=f'{k_text}', callback_data="ketchuptrend")
            ],

            [
                InlineKeyboardButton(text="⬇️ ichimlik ⬇️", callback_data="0")
            ],

            [
                InlineKeyboardButton(text=f"{quyma_colatrend[call.message.chat.id]}", callback_data="quyma_colatrend"),
                InlineKeyboardButton(text=f"{limonli_choytrend[call.message.chat.id]}", callback_data="limonli_choytrend")
            ],

            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ],

        ]
    )
    global checktrend
    summa = 40000 * sontrend['count']

    new_caption = f"""
Maxi BOX Trend 
Gamburger,  kartoshka fri, 0,4 l coca cola, tanlash uchun sous

Maxi BOX Trend 40 000 x {sontrend['count']} = {summa}
{checktrend}
{ssous_checkertrend(call.message.chat.id)}
{psous_checkertrend(call.message.chat.id)}
{ketchup_checkertrend(call.message.chat.id)}
{quyma_cola_checkertrend(call.message.chat.id)}
{limonli_choy_checkertrend(call.message.chat.id)}
Umumiy: {summa} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/MaxiBoxTrend.jpg', 'rb'), caption=new_caption),
        reply_markup=update_button,
        # message_id=call.message.message_id,
        # chat_id=call.message.chat.id
    )