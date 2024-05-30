from keyboards.default.menubuttons import sous
from keyboards.inline.inline_buttons import MaxiBoxPopular
from loader import dp
from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

checkpopular = None
son2 = {
    'count': 1,
    'kichik_kartorshka_fri': "kichik kartoshka-fri",
    'fri_caption': """
kartoshka-fri :
  - kichik kartoshka-fri      0 x 1 = 0  
""",
    'sarimsoq_caption': """""",
}
fri_narx2 = {}

ketchup2 = {'user_id': True}
pishloqli_sous2 = {'user_id': True}
sarimsoqli_sous2 = {'user_id': True}
quyma_cola2 = {'user_id': True}
limonli_choy2 = {'user_id': True}


def ssous_checker2(user_id):
    if user_id in sarimsoqli_sous2.keys():
        if '✅' in sarimsoqli_sous2[user_id]:
            return """
siz tanlagan sous :
- sarimsoqli sous      0 x 1 = 0  
    """
        else:
            return ''


def psous_checker2(user_id):
    if user_id in pishloqli_sous2.keys():
        if '✅' in pishloqli_sous2[user_id]:
            return """
siz tanlagan sous :
- pishloqli sous      0 x 1 = 0  
        """
        else:
            return ''


def ketchup_checker2(user_id):
    if user_id in ketchup2.keys():
        if '✅' in ketchup2[user_id]:
            return """
siz tanlagan sous :
- ketchup       0 x 1 = 0
        """
        else:
            return ''


def quyma_cola_checker2(user_id):
    if user_id in quyma_cola2.keys():
        if '✅' in quyma_cola2[user_id]:
            return """
ichimlik :
  - quyma cola       0 x 1 = 0
    """
        else:
            return ''


def limonli_choy_checker2(user_id):
    if user_id in limonli_choy2.keys():
        if '✅' in limonli_choy2[user_id]:
            return """
ichimlik :
  - limonli choy      0 x 1 = 0
    """
        else:
            return ''


@dp.message_handler(text="Maxi BOX Popular")
async def maxi_box_popular(message: types.Message):
    ketchup2[message.from_user.id] = ''
    sarimsoqli_sous2[message.from_user.id] = ''
    pishloqli_sous2[message.from_user.id] = ''
    quyma_cola2[message.from_user.id] = ''
    limonli_choy2[message.from_user.id] = ''

    await message.answer("Mahsulot miqdorini tanlang")
    await message.answer_photo(photo=open('images/MaxiBoxPopular.jpg', 'rb'), caption="""Maxi BOX Popular 
Original lavash, kartoshka fri, 0,4 l coca cola, tanlash uchun sous


Maxi BOX Popular 45 000 x 1 = 45 000

Umumiy: 45 000 UZS""", reply_markup=MaxiBoxPopular)


@dp.callback_query_handler(text='pluspopular')
async def plusmaxiboxpopular2(call: types.CallbackQuery):
    if call.message.chat.id not in son2.keys():
        son2[call.message.chat.id] = "kichik kartoshka-fri"
    else:
        if '✅' in son2[call.message.chat.id]:
            son2[call.message.chat.id] = "✅kichik kartoshka-fri"
        else:
            son2[call.message.chat.id] = "kichik kartoshka-fri"

    print(son2)
    son2['count'] += 1

    if call.message.chat.id in sarimsoqli_sous2:
        if 'sarimsoqli sous' in sarimsoqli_sous2[call.message.chat.id]:
            button_text = sarimsoqli_sous2[call.message.chat.id]
        else:
            button_text = "sarimsoqli sous"
    else:
        button_text = "sarimsoqli sous"

    if call.message.chat.id in pishloqli_sous2:
        if 'pishloqli sous' in pishloqli_sous2[call.message.chat.id]:
            p_text = pishloqli_sous2[call.message.chat.id]
        else:
            p_text = "pishloqli sous"
    else:
        p_text = "pishloqli sous"

    if call.message.chat.id in ketchup2:
        if 'ketchup' in ketchup2[call.message.chat.id]:
            k_text = ketchup2[call.message.chat.id]
        else:
            k_text = "ketchup"
    else:
        k_text = "ketchup"

    if call.message.chat.id in quyma_cola2:
        if 'quyma cola' in quyma_cola2[call.message.chat.id]:
            cola_text = quyma_cola2[call.message.chat.id]
        else:
            cola_text = "quyma cola"
    else:
        cola_text = "quyma cola"

    if call.message.chat.id in limonli_choy2:
        if 'limonli choy' in limonli_choy2[call.message.chat.id]:
            limonli_text = limonli_choy2[call.message.chat.id]
        else:
            limonli_text = "limonli choy"
    else:
        limonli_text = "limonli choy"

    MaxiBoxPopular = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minuspopular"),
                InlineKeyboardButton(text=str(son2['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="pluspopular")
            ],
            [
                InlineKeyboardButton(text="⬇️ kartoshka-fri ⬇️", callback_data="0")
            ],
            {
                InlineKeyboardButton(text=son2[call.message.chat.id], callback_data="kichik_kartoshka_fripopular")
            },
            [
                InlineKeyboardButton(text="⬇️ siz tanlagan sous ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=f'{button_text}', callback_data="sarimsoqli_souspopular"),
                InlineKeyboardButton(text=f'{p_text}', callback_data="pishloqli_souspopular"),
                InlineKeyboardButton(text=f'{k_text}', callback_data="ketchuppopular")
            ],
            [
                InlineKeyboardButton(text="⬇️ ichimlik ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=f'{cola_text}', callback_data="quyma_colapopular"),
                InlineKeyboardButton(text=f'{limonli_text}', callback_data="limonli_choypopular")
            ],
            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ]
        ]
    )
    if call.message.chat.id not in fri_narx2.keys():
        a = ''
    else:
        a = fri_narx2[call.message.chat.id]

    summa = 45000 * son2['count']
    new_caption = f"""Maxi BOX Popular 
Original lavash, kartoshka fri, 0,4 l coca cola, tanlash uchun sous

Maxi BOX Popular 45 000 x {son2['count']} = {summa}
{a}
{ssous_checker2(call.message.chat.id)}
{psous_checker2(call.message.chat.id)}
{ketchup_checker2(call.message.chat.id)}
{quyma_cola_checker2(call.message.chat.id)}
{limonli_choy_checker2(call.message.chat.id)}
Umumiy: {summa} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/MaxiBoxPopular.jpg', 'rb'), chat_id=call.message.chat.id,
                                    message_id=call.message.message_id, caption=new_caption
                                    ), reply_markup=MaxiBoxPopular,
    )


@dp.callback_query_handler(text='minuspopular')
async def minusmaxiboxpopular(call: types.CallbackQuery):
    print(son2)

    if son2['count'] > 1:
        son2['count'] -= 1

        if call.message.chat.id in sarimsoqli_sous2:
            if 'sarimsoqli sous' in sarimsoqli_sous2[call.message.chat.id]:
                button_text = sarimsoqli_sous2[call.message.chat.id]
            else:
                button_text = "sarimsoqli sous"
        else:
            button_text = "sarimsoqli sous"

        if call.message.chat.id in pishloqli_sous2:
            if 'pishloqli sous' in pishloqli_sous2[call.message.chat.id]:
                p_text = pishloqli_sous2[call.message.chat.id]
            else:
                p_text = "pishloqli sous"
        else:
            p_text = "pishloqli sous"

        if call.message.chat.id in ketchup2:
            if 'ketchup' in ketchup2[call.message.chat.id]:
                k_text = ketchup2[call.message.chat.id]
            else:
                k_text = "ketchup"
        else:
            k_text = "ketchup"

        if call.message.chat.id in quyma_cola2:
            if 'quyma cola' in quyma_cola2[call.message.chat.id]:
                cola_text = quyma_cola2[call.message.chat.id]
            else:
                cola_text = "quyma cola"
        else:
            cola_text = "quyma cola"

        if call.message.chat.id in limonli_choy2:
            if 'limonli choy' in limonli_choy2[call.message.chat.id]:
                limonli_text = limonli_choy2[call.message.chat.id]
            else:
                limonli_text = "limonli choy"
        else:
            limonli_text = "limonli choy"

        MaxiBoxPopular = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="minuspopular"),
                    InlineKeyboardButton(text=str(son2['count']), callback_data='0'),
                    InlineKeyboardButton(text='+', callback_data="pluspopular")
                ],
                [
                    InlineKeyboardButton(text="⬇️ kartoshka-fri ⬇️", callback_data="0")
                ],
                [
                    InlineKeyboardButton(text=son2[call.message.chat.id], callback_data="kichik_kartoshka_fripopular")
                ],
                [
                    InlineKeyboardButton(text="⬇️ siz tanlagan sous ⬇️", callback_data="0")
                ],
                [
                    InlineKeyboardButton(text=f"""{button_text}""", callback_data="sarimsoqli_souspopular"),
                    InlineKeyboardButton(text=f'{p_text}', callback_data="pishloqli_souspopular"),
                    InlineKeyboardButton(text=f'{k_text}', callback_data="ketchuppopular")
                ],
                [
                    InlineKeyboardButton(text="⬇️ ichimlik ⬇️", callback_data="0")
                ],
                [
                    InlineKeyboardButton(text=f'{cola_text}', callback_data="quyma_colapopular"),
                    InlineKeyboardButton(text=f'{limonli_text}', callback_data="limonli_choypopular")
                ],
                [
                    InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
                ]
            ]
        )

        if call.message.chat.id not in fri_narx2.keys():
            a = ''
        else:
            a = fri_narx2[call.message.chat.id]

        summa = 45000 * son2['count']
        new_caption = f"""
Maxi BOX Popular 
Original lavash, kartoshka fri, 0,4 l coca cola, tanlash uchun sous

Maxi BOX Popular 45 000 x {son2['count']} = {summa}
{a}
{ssous_checker2(call.message.chat.id)}
{psous_checker2(call.message.chat.id)}
{ketchup_checker2(call.message.chat.id)}
{quyma_cola_checker2(call.message.chat.id)}
{limonli_choy_checker2(call.message.chat.id)}
Umumiy: {summa} UZS"""

        await call.message.edit_media(
            media=types.InputMediaPhoto(open('images/MaxiBoxPopular.jpg', 'rb'), caption=new_caption),
            reply_markup=MaxiBoxPopular
        )
    else:
        await call.answer("1dan kam mahsulot tanlash mumkin emas")


@dp.callback_query_handler(text="kichik_kartoshka_fripopular")
async def kichikfripopular(call: types.CallbackQuery):
    if call.message.chat.id not in fri_narx2.keys():
        fri_narx2[call.message.chat.id] = '''
kartoshka-fri :
  - kichik kartoshka-fri      0 x 1 = 0  
        '''
    else:
        del fri_narx2[call.message.chat.id]
    # try:
    #     print(son[call.message.chat.id])
    # except:
    #     son[call.message.chat.id] = "✅kichik kartoshka-fri"

    if call.message.chat.id in son2.keys():

        if '✅' not in son2[call.message.chat.id]:
            son2[call.message.chat.id] = "✅kichik kartoshka-fri"
        else:
            son2[call.message.chat.id] = "kichik kartoshka-fri"

    else:
        son2[call.message.chat.id] = "✅kichik kartoshka-fri"

    if call.message.chat.id in sarimsoqli_sous2:
        if 'sarimsoqli sous' in sarimsoqli_sous2[call.message.chat.id]:
            button_text = sarimsoqli_sous2[call.message.chat.id]
        else:
            button_text = "sarimsoqli sous"
    else:
        button_text = "sarimsoqli sous"

    if call.message.chat.id in pishloqli_sous2:
        if 'pishloqli sous' in pishloqli_sous2[call.message.chat.id]:
            p_text = pishloqli_sous2[call.message.chat.id]
        else:
            p_text = "pishloqli sous"
    else:
        p_text = "pishloqli sous"

    if call.message.chat.id in ketchup2:
        if 'ketchup' in ketchup2[call.message.chat.id]:
            k_text = ketchup2[call.message.chat.id]
        else:
            k_text = "ketchup"
    else:
        k_text = "ketchup"

    if call.message.chat.id in quyma_cola2:
        if 'quyma cola' in quyma_cola2[call.message.chat.id]:
            cola_text = quyma_cola2[call.message.chat.id]
        else:
            cola_text = "quyma cola"
    else:
        cola_text = "quyma cola"

    if call.message.chat.id in limonli_choy2:
        if 'limonli choy' in limonli_choy2[call.message.chat.id]:
            limonli_text = limonli_choy2[call.message.chat.id]
        else:
            limonli_text = "limonli choy"
    else:
        limonli_text = "limonli choy"

    update_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minuspopular"),
                InlineKeyboardButton(text=str(son2['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="pluspopular")
            ],
            [
                InlineKeyboardButton(text="⬇️ kartoshka-fri ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=son2[call.message.chat.id], callback_data="kichik_kartoshka_fripopular")
            ],
            [
                InlineKeyboardButton(text="⬇️ siz tanlagan sous ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=f'{button_text}', callback_data="sarimsoqli_souspopular"),
                InlineKeyboardButton(text=f'{p_text}', callback_data="pishloqli_souspopular"),
                InlineKeyboardButton(text=f'{k_text}', callback_data="ketchuppopular")
            ],

            [
                InlineKeyboardButton(text="⬇️ ichimlik ⬇️", callback_data="0")
            ],

            [
                InlineKeyboardButton(text=f'{cola_text}', callback_data="quyma_colapopular"),
                InlineKeyboardButton(text=f'{limonli_text}', callback_data="limonli_choypopular")
            ],

            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ],

        ]
    )
    summa = 45000 * son2['count']
    global checkpopular
    print(son2[call.message.chat.id])
    if '✅' in son2[call.message.chat.id]:
        checkpopular = son2['fri_caption']
    else:
        checkpopular = ''

    new_caption = f"""
Maxi BOX Popular 
Original lavash, kartoshka fri, 0,4 l coca cola, tanlash uchun sous

Maxi BOX Popular 45 000 x {son2['count']} = {summa}
{checkpopular}
{ssous_checker2(call.message.chat.id)}
{psous_checker2(call.message.chat.id)}
{ketchup_checker2(call.message.chat.id)}
{quyma_cola_checker2(call.message.chat.id)}
{limonli_choy_checker2(call.message.chat.id)}
Umumiy: {summa} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/MaxiBoxPopular.jpg', 'rb'), caption=new_caption),
        reply_markup=update_button
    )
    print(son2)


@dp.callback_query_handler(text='sarimsoqli_souspopular')
async def popularsous1(call: types.CallbackQuery):
    pishloqli_sous2[call.message.chat.id] = "pishloqli sous"
    ketchup2[call.message.chat.id] = 'ketchup'

    if call.message.chat.id in son2.keys():

        if '✅' not in sarimsoqli_sous2[call.message.chat.id]:
            sarimsoqli_sous2[call.message.chat.id] = "✅sarimsoqli sous"
        else:
            sarimsoqli_sous2[call.message.chat.id] = "sarimsoqli sous"

    else:
        sarimsoqli_sous2[call.message.chat.id] = "✅sarimsoqli sous"
    if call.message.chat.id not in son2.keys():
        son2[call.message.chat.id] = "kichik kartoshka-fri"

    if call.message.chat.id in quyma_cola2:
        if 'quyma cola' in quyma_cola2[call.message.chat.id]:
            cola_text = quyma_cola2[call.message.chat.id]
        else:
            cola_text = "quyma cola"
    else:
        cola_text = "quyma cola"

    if call.message.chat.id in limonli_choy2:
        if 'limonli choy' in limonli_choy2[call.message.chat.id]:
            limonli_text = limonli_choy2[call.message.chat.id]
        else:
            limonli_text = "limonli choy"
    else:
        limonli_text = "limonli choy"

    update_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minuspopular"),
                InlineKeyboardButton(text=str(son2['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="pluspopular")
            ],
            [
                InlineKeyboardButton(text="⬇️ kartoshka-fri ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=son2[call.message.chat.id], callback_data="kichik_kartoshka_fripopular")
            ],
            [
                InlineKeyboardButton(text="⬇️ siz tanlagan sous ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=f"{sarimsoqli_sous2[call.message.chat.id]}",callback_data="sarimsoqli_souspopular"),
                InlineKeyboardButton(text=f"pishloqli sous", callback_data="pishloqli_souspopular"),
                InlineKeyboardButton(text=f"ketchup", callback_data="ketchuppopular")
            ],

            [
                InlineKeyboardButton(text="⬇️ ichimlik ⬇️", callback_data="0")
            ],

            [
                InlineKeyboardButton(text=f'{cola_text}', callback_data="quyma_colapopular"),
                InlineKeyboardButton(text=f'{limonli_text}', callback_data="limonli_choypopular")
            ],

            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ],

        ]
    )
    global checkpopular
    summa = 45000 * son2['count']
    new_caption = f"""
Maxi BOX Popular 
Original lavash, kartoshka fri, 0,4 l coca cola, tanlash uchun sous

Maxi BOX Popular 45 000 x {son2['count']} = {summa}
{checkpopular}
{ssous_checker2(call.message.chat.id)}
{psous_checker2(call.message.chat.id)}
{ketchup_checker2(call.message.chat.id)}
{quyma_cola_checker2(call.message.chat.id)}
{limonli_choy_checker2(call.message.chat.id)}
Umumiy: {summa} UZS"""

    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/MaxiBoxPopular.jpg', 'rb'), caption=new_caption),
        reply_markup=update_button,
        # message_id=call.message.message_id,
        # chat_id=call.message.chat.id
    )


@dp.callback_query_handler(text='pishloqli_souspopular')
async def popularsous2(call: types.CallbackQuery):
    sarimsoqli_sous2[call.message.chat.id] = "sarimsoqli sous"
    ketchup2[call.message.chat.id] = 'ketchup'

    if call.message.chat.id in son2.keys():

        if '✅' not in pishloqli_sous2[call.message.chat.id]:
            pishloqli_sous2[call.message.chat.id] = "✅pishloqli sous"
        else:
            pishloqli_sous2[call.message.chat.id] = "pishloqli sous"

    else:
        pishloqli_sous2[call.message.chat.id] = "✅pishloqli sous"

    if call.message.chat.id in quyma_cola2:
        if 'quyma cola' in quyma_cola2[call.message.chat.id]:
            cola_text = quyma_cola2[call.message.chat.id]
        else:
            cola_text = "quyma cola"
    else:
        cola_text = "quyma cola"

    if call.message.chat.id in limonli_choy2:
        if 'limonli choy' in limonli_choy2[call.message.chat.id]:
            limonli_text = limonli_choy2[call.message.chat.id]
        else:
            limonli_text = "limonli choy"
    else:
        limonli_text = "limonli choy"

    update_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minuspopular"),
                InlineKeyboardButton(text=str(son2['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="pluspopular")
            ],
            [
                InlineKeyboardButton(text="⬇️ kartoshka-fri ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=son2[call.message.chat.id], callback_data="kichik_kartoshka_fripopular")
            ],
            [
                InlineKeyboardButton(text="⬇️ siz tanlagan sous ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=f"{sarimsoqli_sous2[call.message.chat.id]}", callback_data="sarimsoqli_souspopular"),
                InlineKeyboardButton(text=f"{pishloqli_sous2[call.message.chat.id]}", callback_data="pishloqli_souspopular"),
                InlineKeyboardButton(text=f"ketchup", callback_data="ketchuppopular")
            ],

            [
                InlineKeyboardButton(text="⬇️ ichimlik ⬇️", callback_data="0")
            ],

            [
                InlineKeyboardButton(text=f'{cola_text}', callback_data="quyma_colapopular"),
                InlineKeyboardButton(text=f'{limonli_text}', callback_data="limonli_choypopular")
            ],

            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ],

        ]
    )
    global checkpopular
    summa = 45000 * son2['count']

    new_caption = f"""
Maxi BOX Popular 
Original lavash, kartoshka fri, 0,4 l coca cola, tanlash uchun sous

Maxi BOX Popular 45 000 x {son2['count']} = {summa}
{checkpopular}
{ssous_checker2(call.message.chat.id)}
{psous_checker2(call.message.chat.id)}
{ketchup_checker2(call.message.chat.id)}
{quyma_cola_checker2(call.message.chat.id)}
{limonli_choy_checker2(call.message.chat.id)}
Umumiy: {summa} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/MaxiBoxPopular.jpg', 'rb'), caption=new_caption),
        reply_markup=update_button,
        # message_id=call.message.message_id,
        # chat_id=call.message.chat.id
    )


@dp.callback_query_handler(text='ketchuppopular')
async def popularsous3(call: types.CallbackQuery):
    sarimsoqli_sous2[call.message.chat.id] = "sarimsoqli sous"
    pishloqli_sous2[call.message.chat.id] = 'pishloqli sous'

    if call.message.chat.id in son2.keys():

        if '✅' not in ketchup2[call.message.chat.id]:
            ketchup2[call.message.chat.id] = "✅ketchup"
        else:
            ketchup2[call.message.chat.id] = "ketchup"

    else:
        ketchup2[call.message.chat.id] = "✅ketchup"

    if call.message.chat.id in quyma_cola2:
        if 'quyma cola' in quyma_cola2[call.message.chat.id]:
            cola_text = quyma_cola2[call.message.chat.id]
        else:
            cola_text = "quyma cola"
    else:
        cola_text = "quyma cola"

    if call.message.chat.id in limonli_choy2:
        if 'limonli choy' in limonli_choy2[call.message.chat.id]:
            limonli_text = limonli_choy2[call.message.chat.id]
        else:
            limonli_text = "limonli choy"
    else:
        limonli_text = "limonli choy"

    update_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minuspopular"),
                InlineKeyboardButton(text=str(son2['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="pluspopular")
            ],
            [
                InlineKeyboardButton(text="⬇️ kartoshka-fri ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=son2[call.message.chat.id], callback_data="kichik_kartoshka_fripopular")
            ],
            [
                InlineKeyboardButton(text="⬇️ siz tanlagan sous ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=f"{sarimsoqli_sous2[call.message.chat.id]}", callback_data="sarimsoqli_souspopular"),
                InlineKeyboardButton(text=f"{pishloqli_sous2[call.message.chat.id]}", callback_data="pishloqli_souspopular"),
                InlineKeyboardButton(text=f"{ketchup2[call.message.chat.id]}", callback_data="ketchuppopular")
            ],

            [
                InlineKeyboardButton(text="⬇️ ichimlik ⬇️", callback_data="0")
            ],

            [
                InlineKeyboardButton(text=f'{cola_text}', callback_data="quyma_colapopular"),
                InlineKeyboardButton(text=f'{limonli_text}', callback_data="limonli_choypopular")
            ],

            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ],

        ]
    )
    global checkpopular
    summa = 45000 * son2['count']

    new_caption = f"""
Maxi BOX Popular 
Original lavash, kartoshka fri, 0,4 l coca cola, tanlash uchun sous

Maxi BOX Popular 45 000 x {son2['count']} = {summa}
{checkpopular}
{ssous_checker2(call.message.chat.id)}
{psous_checker2(call.message.chat.id)}
{ketchup_checker2(call.message.chat.id)}
{quyma_cola_checker2(call.message.chat.id)}
{limonli_choy_checker2(call.message.chat.id)}
Umumiy: {summa} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/MaxiBoxPopular.jpg', 'rb'), caption=new_caption),
        reply_markup=update_button,
        # message_id=call.message.message_id,
        # chat_id=call.message.chat.id
    )


@dp.callback_query_handler(text='quyma_colapopular')
async def cola(call: types.CallbackQuery):
    limonli_choy2[call.message.chat.id] = 'limonli choy'

    if call.message.chat.id in son2.keys():

        if '✅' not in quyma_cola2[call.message.chat.id]:
            quyma_cola2[call.message.chat.id] = "✅quyma cola"
        else:
            quyma_cola2[call.message.chat.id] = "quyma cola"

    else:
        quyma_cola2[call.message.chat.id] = "✅quyma cola"

    if call.message.chat.id in sarimsoqli_sous2:
        if 'sarimsoqli sous' in sarimsoqli_sous2[call.message.chat.id]:
            button_text = sarimsoqli_sous2[call.message.chat.id]
        else:
            button_text = "sarimsoqli sous"
    else:
        button_text = "sarimsoqli sous"

    if call.message.chat.id in pishloqli_sous2:
        if 'pishloqli sous' in pishloqli_sous2[call.message.chat.id]:
            p_text = pishloqli_sous2[call.message.chat.id]
        else:
            p_text = "pishloqli sous"
    else:
        p_text = "pishloqli sous"

    if call.message.chat.id in ketchup2:
        if 'ketchup' in ketchup2[call.message.chat.id]:
            k_text = ketchup2[call.message.chat.id]
        else:
            k_text = "ketchup"
    else:
        k_text = "ketchup"

    if call.message.chat.id not in son2.keys():
        son2[call.message.chat.id] = "kichik kartoshka-fri"

    update_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minuspopular"),
                InlineKeyboardButton(text=str(son2['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="pluspopular")
            ],
            [
                InlineKeyboardButton(text="⬇️ kartoshka-fri ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=son2[call.message.chat.id], callback_data="kichik_kartoshka_fripopular")
            ],
            [
                InlineKeyboardButton(text="⬇️ siz tanlagan sous ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=f'{button_text}', callback_data="sarimsoqli_souspopular"),
                InlineKeyboardButton(text=f'{p_text}', callback_data="pishloqli_souspopular"),
                InlineKeyboardButton(text=f'{k_text}', callback_data="ketchuppopular")
            ],

            [
                InlineKeyboardButton(text="⬇️ ichimlik ⬇️", callback_data="0")
            ],

            [
                InlineKeyboardButton(text=f"{quyma_cola2[call.message.chat.id]}", callback_data="quyma_colapopular"),
                InlineKeyboardButton(text="limonli choy", callback_data="limonli_choypopular")
            ],

            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ],

        ]
    )
    global checkpopular
    summa = 45000 * son2['count']

    new_caption = f"""
Maxi BOX Popular 
Original lavash, kartoshka fri, 0,4 l coca cola, tanlash uchun sous

Maxi BOX Popular 45 000 x {son2['count']} = {summa}
{checkpopular}
{ssous_checker2(call.message.chat.id)}
{psous_checker2(call.message.chat.id)}
{ketchup_checker2(call.message.chat.id)}
{quyma_cola_checker2(call.message.chat.id)}
{limonli_choy_checker2(call.message.chat.id)}
Umumiy: {summa} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/MaxiBoxPopular.jpg', 'rb'), caption=new_caption),
        reply_markup=update_button,
        # message_id=call.message.message_id,
        # chat_id=call.message.chat.id
    )


@dp.callback_query_handler(text='limonli_choypopular')
async def limonli(call: types.CallbackQuery):
    quyma_cola2[call.message.chat.id] = 'quyma cola'

    if call.message.chat.id in son2.keys():

        if '✅' not in limonli_choy2[call.message.chat.id]:
            limonli_choy2[call.message.chat.id] = "✅limonli choy"
        else:
            limonli_choy2[call.message.chat.id] = "limonli choy"

    else:
        limonli_choy2[call.message.chat.id] = "✅limonli choy"

    if call.message.chat.id in sarimsoqli_sous2:
        if 'sarimsoqli sous' in sarimsoqli_sous2[call.message.chat.id]:
            button_text = sarimsoqli_sous2[call.message.chat.id]
        else:
            button_text = "sarimsoqli sous"
    else:
        button_text = "sarimsoqli sous"

    if call.message.chat.id in pishloqli_sous2:
        if 'pishloqli sous' in pishloqli_sous2[call.message.chat.id]:
            p_text = pishloqli_sous2[call.message.chat.id]
        else:
            p_text = "pishloqli sous"
    else:
        p_text = "pishloqli sous"

    if call.message.chat.id in ketchup2:
        if 'ketchup' in ketchup2[call.message.chat.id]:
            k_text = ketchup2[call.message.chat.id]
        else:
            k_text = "ketchup"
    else:
        k_text = "ketchup"

    if call.message.chat.id not in son2.keys():
        son2[call.message.chat.id] = "kichik kartoshka-fri"

    update_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minuspopular"),
                InlineKeyboardButton(text=str(son2['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="pluspopular")
            ],
            [
                InlineKeyboardButton(text="⬇️ kartoshka-fri ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=son2[call.message.chat.id], callback_data="kichik_kartoshka_fripopular")
            ],
            [
                InlineKeyboardButton(text="⬇️ siz tanlagan sous ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=f'{button_text}', callback_data="sarimsoqli_souspopular"),
                InlineKeyboardButton(text=f'{p_text}', callback_data="pishloqli_souspopular"),
                InlineKeyboardButton(text=f'{k_text}', callback_data="ketchuppopular")
            ],

            [
                InlineKeyboardButton(text="⬇️ ichimlik ⬇️", callback_data="0")
            ],

            [
                InlineKeyboardButton(text=f"{quyma_cola2[call.message.chat.id]}", callback_data="quyma_colapopular"),
                InlineKeyboardButton(text=f"{limonli_choy2[call.message.chat.id]}", callback_data="limonli_choypopular")
            ],

            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ],

        ]
    )
    global checkpopular
    summa = 45000 * son2['count']

    new_caption = f"""
Maxi BOX Popular 
Original lavash, kartoshka fri, 0,4 l coca cola, tanlash uchun sous

Maxi BOX Popular 45 000 x {son2['count']} = {summa}
{checkpopular}
{ssous_checker2(call.message.chat.id)}
{psous_checker2(call.message.chat.id)}
{ketchup_checker2(call.message.chat.id)}
{quyma_cola_checker2(call.message.chat.id)}
{limonli_choy_checker2(call.message.chat.id)}
Umumiy: {summa} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/MaxiBoxPopular.jpg', 'rb'), caption=new_caption),
        reply_markup=update_button,
        # message_id=call.message.message_id,
        # chat_id=call.message.chat.id
    )
