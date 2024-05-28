from keyboards.default.menubuttons import sous
from keyboards.inline.inline_buttons import MaxiBoxPopular
from loader import dp
from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

check = None
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
quyma_cola = {'user_id':True}
limonli_choy = {'user_id':True}
def ssous_checker(user_id):
    if user_id in sarimsoqli_sous.keys():
        if '✅' in sarimsoqli_sous[user_id]:
            return """
siz tanlagan sous :
- sarimsoqli sous      0 x 1 = 0  
    """
        else:
            return ''


def psous_checker(user_id):
    if user_id in pishloqli_sous.keys():
        if '✅' in pishloqli_sous[user_id]:
            return """
siz tanlagan sous :
- pishloqli sous      0 x 1 = 0  
        """
        else:
            return ''


def ketchup_checker(user_id):
    if user_id in ketchup.keys():
        if '✅' in ketchup[user_id]:
            return """
siz tanlagan sous :
- ketchup       0 x 1 = 0
        """
        else:
            return ''

def quyma_cola_checker(user_id):
    if user_id in quyma_cola.keys():
        if '✅' in quyma_cola[user_id]:
            return """
ichimlik :
  - quyma cola       0 x 1 = 0
    """
        else:
            return ''

def limonli_choy_checker(user_id):
    if user_id in limonli_choy.keys():
        if '✅' in limonli_choy[user_id]:
            return """
ichimlik :
  - limonli choy      0 x 1 = 0
    """
        else:
            return ''


@dp.message_handler(text="Maxi BOX Popular")
async def maxi_box_popular(message: types.Message):
    ketchup[message.from_user.id] = ''
    sarimsoqli_sous[message.from_user.id] = ''
    pishloqli_sous[message.from_user.id] = ''
    quyma_cola[message.from_user.id] = ''
    limonli_choy[message.from_user.id]=''

    await message.answer("Mahsulot miqdorini tanlang")
    await message.answer_photo(photo=open('images/MaxiBOXTraditsiya.png', 'rb'), caption="""Maxi BOX Popular 
Original lavash, kartoshka fri, 0,4 l coca cola, tanlash uchun sous
 

Maxi BOX Popular 45 000 x 1 = 45 000

Umumiy: 45 000 UZS""", reply_markup=MaxiBoxPopular)


@dp.callback_query_handler(text='plus')
async def plusmaxiboxpopular(call: types.CallbackQuery):
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
            button_text = "sarimsoqli sous"
    else:
        button_text = "sarimsoqli sous"

    if call.message.chat.id in pishloqli_sous:
        if 'pishloqli sous' in pishloqli_sous[call.message.chat.id]:
            p_text = pishloqli_sous[call.message.chat.id]
        else:
            p_text = "pishloqli sous"
    else:
        p_text = "pishloqli sous"

    if call.message.chat.id in ketchup:
        if 'ketchup' in ketchup[call.message.chat.id]:
            k_text = ketchup[call.message.chat.id]
        else:
            k_text = "ketchup"
    else:
        k_text = "ketchup"

    if call.message.chat.id in quyma_cola:
        if 'quyma cola' in quyma_cola[call.message.chat.id]:
            cola_text = quyma_cola[call.message.chat.id]
        else:
            cola_text = "quyma cola"
    else:
        cola_text = "quyma cola"

    if call.message.chat.id in limonli_choy:
        if 'limonli choy' in limonli_choy[call.message.chat.id]:
            limonli_text = limonli_choy[call.message.chat.id]
        else:
            limonli_text = "limonli choy"
    else:
        limonli_text = "limonli choy"

    MaxiBoxPopular = InlineKeyboardMarkup(
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
                InlineKeyboardButton(text="⬇️ siz tanlagan sous ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=f'{button_text}', callback_data="sarimsoqli_sous"),
                InlineKeyboardButton(text=f'{p_text}', callback_data="pishloqli_sous"),
                InlineKeyboardButton(text=f'{k_text}', callback_data="ketchup")
            ],
            [
                InlineKeyboardButton(text="⬇️ ichimlik ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=f'{cola_text}', callback_data="quyma_cola"),
                InlineKeyboardButton(text=f'{limonli_text}', callback_data="limonli_choy")
            ],
            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ]
        ]
    )
    if call.message.chat.id not in fri_narx.keys():
        a = ''
    else:
        a = fri_narx[call.message.chat.id]

    summa = 45000 * son['count']
    new_caption = f"""Maxi BOX Popular 
Original lavash, kartoshka fri, 0,4 l coca cola, tanlash uchun sous

Maxi BOX Popular 45 000 x {son['count']} = {summa}
{a}
{ssous_checker(call.message.chat.id)}
{psous_checker(call.message.chat.id)}
{ketchup_checker(call.message.chat.id)}
{quyma_cola_checker(call.message.chat.id)}
{limonli_choy_checker(call.message.chat.id)}
Umumiy: {summa} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/MaxiBoxPopular.jpg', 'rb'), chat_id=call.message.chat.id,
                                    message_id=call.message.message_id, caption=new_caption
                                    ), reply_markup=MaxiBoxPopular,
    )


@dp.callback_query_handler(text='minus')
async def minusmaxiboxpopular(call: types.CallbackQuery):
    print(son)
    try:
        if son['count'] > 1:
            son['count'] -= 1

            if call.message.chat.id in sarimsoqli_sous:
                if 'sarimsoqli sous' in sarimsoqli_sous[call.message.chat.id]:
                    button_text = sarimsoqli_sous[call.message.chat.id]
                else:
                    button_text = "sarimsoqli sous"
            else:
                button_text = "sarimsoqli sous"

            if call.message.chat.id in pishloqli_sous:
                if 'pishloqli sous' in pishloqli_sous[call.message.chat.id]:
                    p_text = pishloqli_sous[call.message.chat.id]
                else:
                    p_text = "pishloqli sous"
            else:
                p_text = "pishloqli sous"

            if call.message.chat.id in ketchup:
                if 'ketchup' in ketchup[call.message.chat.id]:
                    k_text = ketchup[call.message.chat.id]
                else:
                    k_text = "ketchup"
            else:
                k_text = "ketchup"

            if call.message.chat.id in quyma_cola:
                if 'quyma cola' in quyma_cola[call.message.chat.id]:
                    cola_text = quyma_cola[call.message.chat.id]
                else:
                    cola_text = "quyma cola"
            else:
                cola_text = "quyma cola"

            if call.message.chat.id in limonli_choy:
                if 'limonli choy' in limonli_choy[call.message.chat.id]:
                    limonli_text = limonli_choy[call.message.chat.id]
                else:
                    limonli_text = "limonli choy"
            else:
                limonli_text = "limonli choy"

            MaxiBoxPopular = InlineKeyboardMarkup(
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
                        InlineKeyboardButton(text="⬇️ siz tanlagan sous ⬇️", callback_data="0")
                    ],
                    [
                        InlineKeyboardButton(text=f"""{button_text}""", callback_data="sarimsoqli_sous"),
                        InlineKeyboardButton(text=f'{p_text}', callback_data="pishloqli_sous"),
                        InlineKeyboardButton(text=f'{k_text}', callback_data="ketchup")
                    ],
                    [
                        InlineKeyboardButton(text="⬇️ ichimlik ⬇️", callback_data="0")
                    ],
                    [
                        InlineKeyboardButton(text=f'{cola_text}', callback_data="quyma_cola"),
                        InlineKeyboardButton(text=f'{limonli_text}', callback_data="limonli_choy")
                    ],
                    [
                        InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
                    ]
                ]
            )

            if call.message.chat.id not in fri_narx.keys():
                a = ''
            else:
                a = fri_narx[call.message.chat.id]

            summa = 45000 * son['count']
            new_caption = f"""
Maxi BOX Popular 
Original lavash, kartoshka fri, 0,4 l coca cola, tanlash uchun sous

Maxi BOX Popular 45 000 x {son['count']} = {summa}
{a}
{ssous_checker(call.message.chat.id)}
{psous_checker(call.message.chat.id)}
{ketchup_checker(call.message.chat.id)}
{quyma_cola_checker(call.message.chat.id)}
{limonli_choy_checker(call.message.chat.id)}
Umumiy: {summa} UZS"""

            await call.message.edit_media(
                media=types.InputMediaPhoto(open('imagesMaxiBoxPopular.jpg', 'rb'), caption=new_caption),
                reply_markup=MaxiBoxPopular
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
            button_text = "sarimsoqli sous"
    else:
        button_text = "sarimsoqli sous"

    if call.message.chat.id in pishloqli_sous:
        if 'pishloqli sous' in pishloqli_sous[call.message.chat.id]:
            p_text = pishloqli_sous[call.message.chat.id]
        else:
            p_text = "pishloqli sous"
    else:
        p_text = "pishloqli sous"

    if call.message.chat.id in ketchup:
        if 'ketchup' in ketchup[call.message.chat.id]:
            k_text = ketchup[call.message.chat.id]
        else:
            k_text = "ketchup"
    else:
        k_text = "ketchup"

    if call.message.chat.id in quyma_cola:
        if 'quyma cola' in quyma_cola[call.message.chat.id]:
            cola_text = quyma_cola[call.message.chat.id]
        else:
            cola_text = "quyma cola"
    else:
        cola_text = "quyma cola"

    if call.message.chat.id in limonli_choy:
        if 'limonli choy' in limonli_choy[call.message.chat.id]:
            limonli_text = limonli_choy[call.message.chat.id]
        else:
            limonli_text = "limonli choy"
    else:
        limonli_text = "limonli choy"

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
                InlineKeyboardButton(text="⬇️ siz tanlagan sous ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=f'{button_text}', callback_data="sarimsoqli_sous"),
                InlineKeyboardButton(text=f'{p_text}', callback_data="pishloqli_sous"),
                InlineKeyboardButton(text=f'{k_text}', callback_data="ketchup")
            ],

            [
                InlineKeyboardButton(text="⬇️ ichimlik ⬇️", callback_data="0")
            ],

            [
                InlineKeyboardButton(text=f'{cola_text}', callback_data="quyma_cola"),
                InlineKeyboardButton(text=f'{limonli_text}', callback_data="limonli_choy")
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
Maxi BOX Popular 
Original lavash, kartoshka fri, 0,4 l coca cola, tanlash uchun sous

Maxi BOX Popular 45 000 x {son['count']} = {summa}
{check}
{ssous_checker(call.message.chat.id)}
{psous_checker(call.message.chat.id)}
{ketchup_checker(call.message.chat.id)}
{quyma_cola_checker(call.message.chat.id)}
{limonli_choy_checker(call.message.chat.id)}
Umumiy: {summa} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/MaxiBoxPopular.jpg', 'rb'), caption=new_caption),
        reply_markup=update_button
    )
    print(son)


@dp.callback_query_handler(text='sarimsoqli_sous')
async def sous1(call: types.CallbackQuery):
    pishloqli_sous[call.message.chat.id] = "pishloqli sous"
    ketchup[call.message.chat.id] = 'ketchup'

    if call.message.chat.id in son.keys():

        if '✅' not in sarimsoqli_sous[call.message.chat.id]:
            sarimsoqli_sous[call.message.chat.id] = "✅sarimsoqli sous"
        else:
            sarimsoqli_sous[call.message.chat.id] = "sarimsoqli sous"

    else:
        sarimsoqli_sous[call.message.chat.id] = "✅sarimsoqli sous"
    if call.message.chat.id not in son.keys():
        son[call.message.chat.id] = "kichik kartoshka-fri"

    if call.message.chat.id in quyma_cola:
        if 'quyma cola' in quyma_cola[call.message.chat.id]:
            cola_text = quyma_cola[call.message.chat.id]
        else:
            cola_text = "quyma cola"
    else:
        cola_text = "quyma cola"

    if call.message.chat.id in limonli_choy:
        if 'limonli choy' in limonli_choy[call.message.chat.id]:
            limonli_text = limonli_choy[call.message.chat.id]
        else:
            limonli_text = "limonli choy"
    else:
        limonli_text = "limonli choy"

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
                InlineKeyboardButton(text="⬇️ siz tanlagan sous ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=f"{sarimsoqli_sous[call.message.chat.id]}", callback_data="sarimsoqli_sous"),
                InlineKeyboardButton(text=f"pishloqli sous", callback_data="pishloqli_sous"),
                InlineKeyboardButton(text=f"ketchup", callback_data="ketchup")
            ],

            [
                InlineKeyboardButton(text="⬇️ ichimlik ⬇️", callback_data="0")
            ],

            [
                InlineKeyboardButton(text=f'{cola_text}', callback_data="quyma_cola"),
                InlineKeyboardButton(text=f'{limonli_text}', callback_data="limonli_choy")
            ],

            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ],

        ]
    )
    global check
    summa = 45000 * son['count']
    new_caption = f"""
Maxi BOX Popular 
Original lavash, kartoshka fri, 0,4 l coca cola, tanlash uchun sous

Maxi BOX Popular 45 000 x {son['count']} = {summa}
{check}
{ssous_checker(call.message.chat.id)}
{psous_checker(call.message.chat.id)}
{ketchup_checker(call.message.chat.id)}
{quyma_cola_checker(call.message.chat.id)}
{limonli_choy_checker(call.message.chat.id)}
Umumiy: {summa} UZS"""

    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/MaxiBoxPopular.jpg', 'rb'), caption=new_caption),
        reply_markup=update_button,
        # message_id=call.message.message_id,
        # chat_id=call.message.chat.id
    )


@dp.callback_query_handler(text='pishloqli_sous')
async def sous2(call: types.CallbackQuery):
    sarimsoqli_sous[call.message.chat.id] = "sarimsoqli sous"
    ketchup[call.message.chat.id] = 'ketchup'

    if call.message.chat.id in son.keys():

        if '✅' not in pishloqli_sous[call.message.chat.id]:
            pishloqli_sous[call.message.chat.id] = "✅pishloqli sous"
        else:
            pishloqli_sous[call.message.chat.id] = "pishloqli sous"

    else:
        pishloqli_sous[call.message.chat.id] = "✅pishloqli sous"

    if call.message.chat.id in quyma_cola:
        if 'quyma cola' in quyma_cola[call.message.chat.id]:
            cola_text = quyma_cola[call.message.chat.id]
        else:
            cola_text = "quyma cola"
    else:
        cola_text = "quyma cola"

    if call.message.chat.id in limonli_choy:
        if 'limonli choy' in limonli_choy[call.message.chat.id]:
            limonli_text = limonli_choy[call.message.chat.id]
        else:
            limonli_text = "limonli choy"
    else:
        limonli_text = "limonli choy"

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
                InlineKeyboardButton(text="⬇️ siz tanlagan sous ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=f"{sarimsoqli_sous[call.message.chat.id]}", callback_data="sarimsoqli_sous"),
                InlineKeyboardButton(text=f"{pishloqli_sous[call.message.chat.id]}", callback_data="pishloqli_sous"),
                InlineKeyboardButton(text=f"ketchup", callback_data="ketchup")
            ],

            [
                InlineKeyboardButton(text="⬇️ ichimlik ⬇️", callback_data="0")
            ],

            [
                InlineKeyboardButton(text=f'{cola_text}', callback_data="quyma_cola"),
                InlineKeyboardButton(text=f'{limonli_text}', callback_data="limonli_choy")
            ],

            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ],

        ]
    )
    global check
    summa = 45000 * son['count']

    new_caption = f"""
Maxi BOX Popular 
Original lavash, kartoshka fri, 0,4 l coca cola, tanlash uchun sous

Maxi BOX Popular 45 000 x {son['count']} = {summa}
{check}
{ssous_checker(call.message.chat.id)}
{psous_checker(call.message.chat.id)}
{ketchup_checker(call.message.chat.id)}
{quyma_cola_checker(call.message.chat.id)}
{limonli_choy_checker(call.message.chat.id)}
Umumiy: {summa} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/MaxiBoxPopular.jpg', 'rb'), caption=new_caption),
        reply_markup=update_button,
        # message_id=call.message.message_id,
        # chat_id=call.message.chat.id
    )


@dp.callback_query_handler(text='ketchup')
async def sous3(call: types.CallbackQuery):
    sarimsoqli_sous[call.message.chat.id] = "sarimsoqli sous"
    pishloqli_sous[call.message.chat.id] = 'pishloqli sous'

    if call.message.chat.id in son.keys():

        if '✅' not in ketchup[call.message.chat.id]:
            ketchup[call.message.chat.id] = "✅ketchup"
        else:
            ketchup[call.message.chat.id] = "ketchup"

    else:
        ketchup[call.message.chat.id] = "✅ketchup"

    if call.message.chat.id in quyma_cola:
        if 'quyma cola' in quyma_cola[call.message.chat.id]:
            cola_text = quyma_cola[call.message.chat.id]
        else:
            cola_text = "quyma cola"
    else:
        cola_text = "quyma cola"

    if call.message.chat.id in limonli_choy:
        if 'limonli choy' in limonli_choy[call.message.chat.id]:
            limonli_text = limonli_choy[call.message.chat.id]
        else:
            limonli_text = "limonli choy"
    else:
        limonli_text = "limonli choy"

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
                InlineKeyboardButton(text="⬇️ siz tanlagan sous ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=f"{sarimsoqli_sous[call.message.chat.id]}", callback_data="sarimsoqli_sous"),
                InlineKeyboardButton(text=f"{pishloqli_sous[call.message.chat.id]}", callback_data="pishloqli_sous"),
                InlineKeyboardButton(text=f"{ketchup[call.message.chat.id]}", callback_data="ketchup")
            ],

            [
                InlineKeyboardButton(text="⬇️ ichimlik ⬇️", callback_data="0")
            ],

            [
                InlineKeyboardButton(text=f'{cola_text}', callback_data="quyma_cola"),
                InlineKeyboardButton(text=f'{limonli_text}', callback_data="limonli_choy")
            ],

            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ],

        ]
    )
    global check
    summa = 45000 * son['count']

    new_caption = f"""
Maxi BOX Popular 
Original lavash, kartoshka fri, 0,4 l coca cola, tanlash uchun sous

Maxi BOX Popular 45 000 x {son['count']} = {summa}
{check}
{ssous_checker(call.message.chat.id)}
{psous_checker(call.message.chat.id)}
{ketchup_checker(call.message.chat.id)}
{quyma_cola_checker(call.message.chat.id)}
{limonli_choy_checker(call.message.chat.id)}
Umumiy: {summa} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/MaxiBoxPopular.jpg', 'rb'), caption=new_caption),
        reply_markup=update_button,
        # message_id=call.message.message_id,
        # chat_id=call.message.chat.id
    )


@dp.callback_query_handler(text='quyma_cola')
async def cola(call: types.CallbackQuery):
    limonli_choy[call.message.chat.id] = 'limonli choy'


    if call.message.chat.id in son.keys():

        if '✅' not in quyma_cola[call.message.chat.id]:
            quyma_cola[call.message.chat.id] = "✅quyma cola"
        else:
            quyma_cola[call.message.chat.id] = "quyma cola"

    else:
        quyma_cola[call.message.chat.id] = "✅quyma cola"

    if call.message.chat.id in sarimsoqli_sous:
        if 'sarimsoqli sous' in sarimsoqli_sous[call.message.chat.id]:
            button_text = sarimsoqli_sous[call.message.chat.id]
        else:
            button_text = "sarimsoqli sous"
    else:
        button_text = "sarimsoqli sous"

    if call.message.chat.id in pishloqli_sous:
        if 'pishloqli sous' in pishloqli_sous[call.message.chat.id]:
            p_text = pishloqli_sous[call.message.chat.id]
        else:
            p_text = "pishloqli sous"
    else:
        p_text = "pishloqli sous"

    if call.message.chat.id in ketchup:
        if 'ketchup' in ketchup[call.message.chat.id]:
            k_text = ketchup[call.message.chat.id]
        else:
            k_text = "ketchup"
    else:
        k_text = "ketchup"

    if call.message.chat.id not in son.keys():
        son[call.message.chat.id] = "kichik kartoshka-fri"

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
                InlineKeyboardButton(text="⬇️ siz tanlagan sous ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=f'{button_text}', callback_data="sarimsoqli_sous"),
                InlineKeyboardButton(text=f'{p_text}', callback_data="pishloqli_sous"),
                InlineKeyboardButton(text=f'{k_text}', callback_data="ketchup")
            ],

            [
                InlineKeyboardButton(text="⬇️ ichimlik ⬇️", callback_data="0")
            ],

            [
                InlineKeyboardButton(text=f"{quyma_cola[call.message.chat.id]}", callback_data="quyma_cola"),
                InlineKeyboardButton(text="limonli choy", callback_data="limonli_choy")
            ],

            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ],

        ]
    )
    global check
    summa = 45000 * son['count']

    new_caption = f"""
Maxi BOX Popular 
Original lavash, kartoshka fri, 0,4 l coca cola, tanlash uchun sous

Maxi BOX Popular 45 000 x {son['count']} = {summa}
{check}
{ssous_checker(call.message.chat.id)}
{psous_checker(call.message.chat.id)}
{ketchup_checker(call.message.chat.id)}
{quyma_cola_checker(call.message.chat.id)}
{limonli_choy_checker(call.message.chat.id)}
Umumiy: {summa} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/MaxiBoxPopular.jpg', 'rb'), caption=new_caption),
        reply_markup=update_button,
        # message_id=call.message.message_id,
        # chat_id=call.message.chat.id
    )



@dp.callback_query_handler(text='limonli_choy')
async def limonli(call: types.CallbackQuery):
    quyma_cola[call.message.chat.id] = 'quyma cola'


    if call.message.chat.id in son.keys():

        if '✅' not in limonli_choy[call.message.chat.id]:
            limonli_choy[call.message.chat.id] = "✅limonli choy"
        else:
            limonli_choy[call.message.chat.id] = "limonli choy"

    else:
        limonli_choy[call.message.chat.id] = "✅limonli choy"

    if call.message.chat.id in sarimsoqli_sous:
        if 'sarimsoqli sous' in sarimsoqli_sous[call.message.chat.id]:
            button_text = sarimsoqli_sous[call.message.chat.id]
        else:
            button_text = "sarimsoqli sous"
    else:
        button_text = "sarimsoqli sous"

    if call.message.chat.id in pishloqli_sous:
        if 'pishloqli sous' in pishloqli_sous[call.message.chat.id]:
            p_text = pishloqli_sous[call.message.chat.id]
        else:
            p_text = "pishloqli sous"
    else:
        p_text = "pishloqli sous"

    if call.message.chat.id in ketchup:
        if 'ketchup' in ketchup[call.message.chat.id]:
            k_text = ketchup[call.message.chat.id]
        else:
            k_text = "ketchup"
    else:
        k_text = "ketchup"

    if call.message.chat.id not in son.keys():
        son[call.message.chat.id] = "kichik kartoshka-fri"

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
                InlineKeyboardButton(text="⬇️ siz tanlagan sous ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=f'{button_text}', callback_data="sarimsoqli_sous"),
                InlineKeyboardButton(text=f'{p_text}', callback_data="pishloqli_sous"),
                InlineKeyboardButton(text=f'{k_text}', callback_data="ketchup")
            ],

            [
                InlineKeyboardButton(text="⬇️ ichimlik ⬇️", callback_data="0")
            ],

            [
                InlineKeyboardButton(text=f"{quyma_cola[call.message.chat.id]}", callback_data="quyma_cola"),
                InlineKeyboardButton(text=f"{limonli_choy[call.message.chat.id]}", callback_data="limonli_choy")
            ],

            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ],

        ]
    )
    global check
    summa = 45000 * son['count']

    new_caption = f"""
Maxi BOX Popular 
Original lavash, kartoshka fri, 0,4 l coca cola, tanlash uchun sous

Maxi BOX Popular 45 000 x {son['count']} = {summa}
{check}
{ssous_checker(call.message.chat.id)}
{psous_checker(call.message.chat.id)}
{ketchup_checker(call.message.chat.id)}
{quyma_cola_checker(call.message.chat.id)}
{limonli_choy_checker(call.message.chat.id)}
Umumiy: {summa} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/MaxiBoxPopular.jpg', 'rb'), caption=new_caption),
        reply_markup=update_button,
        # message_id=call.message.message_id,
        # chat_id=call.message.chat.id
    )