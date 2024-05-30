from keyboards.default.menubuttons import sous
from keyboards.inline.inline_buttons import MaxiBoxRetro
from loader import dp
from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

checkretro = None
sonretro = {
    'count': 1,
    'kichik_kartorshka_fri': "kichik kartoshka-fri",
    'fri_caption': """
kartoshka-fri :
  - kichik kartoshka-fri      0 x 1 = 0  
""",
    'sarimsoq_caption': """""",
}
fri_narxretro = {}

ketchupretro = {'user_id': True}
pishloqli_sousretro = {'user_id': True}
sarimsoqli_sousretro = {'user_id': True}
quyma_colaretro = {'user_id':True}
limonli_choyretro = {'user_id':True}
def ssous_checkerretro(user_id):
    if user_id in sarimsoqli_sousretro.keys():
        if '✅' in sarimsoqli_sousretro[user_id]:
            return """
siz tanlagan sous :
- sarimsoqli sous      0 x 1 = 0  
    """
        else:
            return ''


def psous_checkerretro(user_id):
    if user_id in pishloqli_sousretro.keys():
        if '✅' in pishloqli_sousretro[user_id]:
            return """
siz tanlagan sous :
- pishloqli sous      0 x 1 = 0  
        """
        else:
            return ''


def ketchup_checkerretro(user_id):
    if user_id in ketchupretro.keys():
        if '✅' in ketchupretro[user_id]:
            return """
siz tanlagan sous :
- ketchup       0 x 1 = 0
        """
        else:
            return ''

def quyma_cola_checkerretro(user_id):
    if user_id in quyma_colaretro.keys():
        if '✅' in quyma_colaretro[user_id]:
            return """
ichimlik :
  - quyma cola       0 x 1 = 0
    """
        else:
            return ''

def limonli_choy_checkerretro(user_id):
    if user_id in limonli_choyretro.keys():
        if '✅' in limonli_choyretro[user_id]:
            return """
ichimlik :
  - limonli choy      0 x 1 = 0
    """
        else:
            return ''


@dp.message_handler(text="Maxi BOX Retro")
async def maxi_box_retro(message: types.Message):
    ketchupretro[message.from_user.id] = ''
    sarimsoqli_sousretro[message.from_user.id] = ''
    pishloqli_sousretro[message.from_user.id] = ''
    quyma_colaretro[message.from_user.id] = ''
    limonli_choyretro[message.from_user.id]=''

    await message.answer("Mahsulot miqdorini tanlang")
    await message.answer_photo(photo=open('images/MaxiBoxRetro.jpg', 'rb'), caption="""
Maxi BOX Retro 
Shaurma Original, kartoshka fri, 0,4 l coca cola , tanlash uchun sous 

Maxi BOX Retro 42 000 x 1 = 42 000

Umumiy: 42 000 UZS""", reply_markup=MaxiBoxRetro)


@dp.callback_query_handler(text='plusretro')
async def plusmaxiboxretro(call: types.CallbackQuery):
    if call.message.chat.id not in sonretro.keys():
        sonretro[call.message.chat.id] = "kichik kartoshka-fri"
    else:
        if '✅' in sonretro[call.message.chat.id]:
            sonretro[call.message.chat.id] = "✅kichik kartoshka-fri"
        else:
            sonretro[call.message.chat.id] = "kichik kartoshka-fri"

    print(sonretro)
    sonretro['count'] += 1

    if call.message.chat.id in sarimsoqli_sousretro:
        if 'sarimsoqli sous' in sarimsoqli_sousretro[call.message.chat.id]:
            button_text = sarimsoqli_sousretro[call.message.chat.id]
        else:
            button_text = "sarimsoqli sous"
    else:
        button_text = "sarimsoqli sous"

    if call.message.chat.id in pishloqli_sousretro:
        if 'pishloqli sous' in pishloqli_sousretro[call.message.chat.id]:
            p_text = pishloqli_sousretro[call.message.chat.id]
        else:
            p_text = "pishloqli sous"
    else:
        p_text = "pishloqli sous"

    if call.message.chat.id in ketchupretro:
        if 'ketchup' in ketchupretro[call.message.chat.id]:
            k_text = ketchupretro[call.message.chat.id]
        else:
            k_text = "ketchup"
    else:
        k_text = "ketchup"

    if call.message.chat.id in quyma_colaretro:
        if 'quyma cola' in quyma_colaretro[call.message.chat.id]:
            cola_text = quyma_colaretro[call.message.chat.id]
        else:
            cola_text = "quyma cola"
    else:
        cola_text = "quyma cola"

    if call.message.chat.id in limonli_choyretro:
        if 'limonli choy' in limonli_choyretro[call.message.chat.id]:
            limonli_text = limonli_choyretro[call.message.chat.id]
        else:
            limonli_text = "limonli choy"
    else:
        limonli_text = "limonli choy"

    MaxiBoxRetro = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minusretro"),
                InlineKeyboardButton(text=str(sonretro['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plusretro")
            ],
            [
                InlineKeyboardButton(text="⬇️ kartoshka-fri ⬇️", callback_data="0")
            ],
            {
                InlineKeyboardButton(text=sonretro[call.message.chat.id], callback_data="kichik_kartoshka_friretro")
            },
            [
                InlineKeyboardButton(text="⬇️ siz tanlagan sous ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=f'{button_text}', callback_data="sarimsoqli_sousretro"),
                InlineKeyboardButton(text=f'{p_text}', callback_data="pishloqli_sousretro"),
                InlineKeyboardButton(text=f'{k_text}', callback_data="ketchupretro")
            ],
            [
                InlineKeyboardButton(text="⬇️ ichimlik ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=f'{cola_text}', callback_data="quyma_colaretro"),
                InlineKeyboardButton(text=f'{limonli_text}', callback_data="limonli_choyretro")
            ],
            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ]
        ]
    )
    if call.message.chat.id not in fri_narxretro.keys():
        a = ''
    else:
        a = fri_narxretro[call.message.chat.id]

    summa = 42000 * sonretro['count']
    new_caption = f"""
Maxi BOX Retro 
Shaurma Original, kartoshka fri, 0,4 l coca cola , tanlash uchun sous

Maxi BOX Retro 42 000 x {sonretro['count']} = {summa}
{a}
{ssous_checkerretro(call.message.chat.id)}
{psous_checkerretro(call.message.chat.id)}
{ketchup_checkerretro(call.message.chat.id)}
{quyma_cola_checkerretro(call.message.chat.id)}
{limonli_choy_checkerretro(call.message.chat.id)}
Umumiy: {summa} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/MaxiBoxRetro.jpg', 'rb'), chat_id=call.message.chat.id,
                                    message_id=call.message.message_id, caption=new_caption
                                    ), reply_markup=MaxiBoxRetro,
    )


@dp.callback_query_handler(text='minusretro')
async def minusmaxiboxretro(call: types.CallbackQuery):
    print(sonretro)

    if sonretro['count'] > 1:
        sonretro['count'] -= 1

        if call.message.chat.id in sarimsoqli_sousretro:
            if 'sarimsoqli sous' in sarimsoqli_sousretro[call.message.chat.id]:
                button_text = sarimsoqli_sousretro[call.message.chat.id]
            else:
                button_text = "sarimsoqli sous"
        else:
            button_text = "sarimsoqli sous"

        if call.message.chat.id in pishloqli_sousretro:
            if 'pishloqli sous' in pishloqli_sousretro[call.message.chat.id]:
                p_text = pishloqli_sousretro[call.message.chat.id]
            else:
                p_text = "pishloqli sous"
        else:
            p_text = "pishloqli sous"

        if call.message.chat.id in ketchupretro:
            if 'ketchup' in ketchupretro[call.message.chat.id]:
                k_text = ketchupretro[call.message.chat.id]
            else:
                k_text = "ketchup"
        else:
            k_text = "ketchup"

        if call.message.chat.id in quyma_colaretro:
            if 'quyma cola' in quyma_colaretro[call.message.chat.id]:
                cola_text = quyma_colaretro[call.message.chat.id]
            else:
                cola_text = "quyma cola"
        else:
            cola_text = "quyma cola"

        if call.message.chat.id in limonli_choyretro:
            if 'limonli choy' in limonli_choyretro[call.message.chat.id]:
                limonli_text = limonli_choyretro[call.message.chat.id]
            else:
                limonli_text = "limonli choy"
        else:
            limonli_text = "limonli choy"

        MaxiBoxRetro = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="minusretro"),
                    InlineKeyboardButton(text=str(sonretro['count']), callback_data='0'),
                    InlineKeyboardButton(text='+', callback_data="plusretro")
                ],
                [
                    InlineKeyboardButton(text="⬇️ kartoshka-fri ⬇️", callback_data="0")
                ],
                [
                    InlineKeyboardButton(text=sonretro[call.message.chat.id], callback_data="kichik_kartoshka_friretro")
                ],
                [
                    InlineKeyboardButton(text="⬇️ siz tanlagan sous ⬇️", callback_data="0")
                ],
                [
                    InlineKeyboardButton(text=f"""{button_text}""", callback_data="sarimsoqli_sousretro"),
                    InlineKeyboardButton(text=f'{p_text}', callback_data="pishloqli_sousretro"),
                    InlineKeyboardButton(text=f'{k_text}', callback_data="ketchupretro")
                ],
                [
                    InlineKeyboardButton(text="⬇️ ichimlik ⬇️", callback_data="0")
                ],
                [
                    InlineKeyboardButton(text=f'{cola_text}', callback_data="quyma_colaretro"),
                    InlineKeyboardButton(text=f'{limonli_text}', callback_data="limonli_choyretro")
                ],
                [
                    InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
                ]
            ]
        )

        if call.message.chat.id not in fri_narxretro.keys():
            a = ''
        else:
            a = fri_narxretro[call.message.chat.id]

        summa = 42000 * sonretro['count']
        new_caption = f"""
Maxi BOX Retro 
Shaurma Original, kartoshka fri, 0,4 l coca cola , tanlash uchun sous

Maxi BOX Retro 42 000 x {sonretro['count']} = {summa}
{a}
{ssous_checkerretro(call.message.chat.id)}
{psous_checkerretro(call.message.chat.id)}
{ketchup_checkerretro(call.message.chat.id)}
{quyma_cola_checkerretro(call.message.chat.id)}
{limonli_choy_checkerretro(call.message.chat.id)}
Umumiy: {summa} UZS"""

        await call.message.edit_media(
            media=types.InputMediaPhoto(open('images/MaxiBoxRetro.jpg', 'rb'), caption=new_caption),
            reply_markup=MaxiBoxRetro
        )
    else:
        await call.answer("1dan kam mahsulot tanlash mumkin emas")



@dp.callback_query_handler(text='kichik_kartoshka_friretro')
async def kichikfriretro(call: types.CallbackQuery):
    if call.message.chat.id not in fri_narxretro.keys():
        fri_narxretro[call.message.chat.id] = '''
kartoshka-fri :
  - kichik kartoshka-fri      0 x 1 = 0  
        '''
    else:
        del fri_narxretro[call.message.chat.id]
    # try:
    #     print(son[call.message.chat.id])
    # except:
    #     son[call.message.chat.id] = "✅kichik kartoshka-fri"

    if call.message.chat.id in sonretro.keys():

        if '✅' not in sonretro[call.message.chat.id]:
            sonretro[call.message.chat.id] = "✅kichik kartoshka-fri"
        else:
            sonretro[call.message.chat.id] = "kichik kartoshka-fri"

    else:
        sonretro[call.message.chat.id] = "✅kichik kartoshka-fri"

    if call.message.chat.id in sarimsoqli_sousretro:
        if 'sarimsoqli sous' in sarimsoqli_sousretro[call.message.chat.id]:
            button_text = sarimsoqli_sousretro[call.message.chat.id]
        else:
            button_text = "sarimsoqli sous"
    else:
        button_text = "sarimsoqli sous"

    if call.message.chat.id in pishloqli_sousretro:
        if 'pishloqli sous' in pishloqli_sousretro[call.message.chat.id]:
            p_text = pishloqli_sousretro[call.message.chat.id]
        else:
            p_text = "pishloqli sous"
    else:
        p_text = "pishloqli sous"

    if call.message.chat.id in ketchupretro:
        if 'ketchup' in ketchupretro[call.message.chat.id]:
            k_text = ketchupretro[call.message.chat.id]
        else:
            k_text = "ketchup"
    else:
        k_text = "ketchup"

    if call.message.chat.id in quyma_colaretro:
        if 'quyma cola' in quyma_colaretro[call.message.chat.id]:
            cola_text = quyma_colaretro[call.message.chat.id]
        else:
            cola_text = "quyma cola"
    else:
        cola_text = "quyma cola"

    if call.message.chat.id in limonli_choyretro:
        if 'limonli choy' in limonli_choyretro[call.message.chat.id]:
            limonli_text = limonli_choyretro[call.message.chat.id]
        else:
            limonli_text = "limonli choy"
    else:
        limonli_text = "limonli choy"

    update_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minusretro"),
                InlineKeyboardButton(text=str(sonretro['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plusretro")
            ],
            [
                InlineKeyboardButton(text="⬇️ kartoshka-fri ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=sonretro[call.message.chat.id], callback_data="kichik_kartoshka_friretro")
            ],
            [
                InlineKeyboardButton(text="⬇️ siz tanlagan sous ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=f'{button_text}', callback_data="sarimsoqli_sousretro"),
                InlineKeyboardButton(text=f'{p_text}', callback_data="pishloqli_sousretro"),
                InlineKeyboardButton(text=f'{k_text}', callback_data="ketchupretro")
            ],

            [
                InlineKeyboardButton(text="⬇️ ichimlik ⬇️", callback_data="0")
            ],

            [
                InlineKeyboardButton(text=f'{cola_text}', callback_data="quyma_colaretro"),
                InlineKeyboardButton(text=f'{limonli_text}', callback_data="limonli_choyretro")
            ],

            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ],

        ]
    )
    summa = 42000 * sonretro['count']
    global checkretro
    print(sonretro[call.message.chat.id])
    if '✅' in sonretro[call.message.chat.id]:
        checkretro = sonretro['fri_caption']
    else:
        checkretro = ''

    new_caption = f"""
Maxi BOX Retro 
Shaurma Original, kartoshka fri, 0,4 l coca cola , tanlash uchun sous

Maxi BOX Retro 42 000 x {sonretro['count']} = {summa}
{checkretro}
{ssous_checkerretro(call.message.chat.id)}
{psous_checkerretro(call.message.chat.id)}
{ketchup_checkerretro(call.message.chat.id)}
{quyma_cola_checkerretro(call.message.chat.id)}
{limonli_choy_checkerretro(call.message.chat.id)}
Umumiy: {summa} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/MaxiBoxRetro.jpg', 'rb'), caption=new_caption),
        reply_markup=update_button
    )
    print(sonretro)


@dp.callback_query_handler(text='sarimsoqli_sousretro')
async def sous1retro(call: types.CallbackQuery):
    pishloqli_sousretro[call.message.chat.id] = "pishloqli sous"
    ketchupretro[call.message.chat.id] = 'ketchup'

    if call.message.chat.id in sonretro.keys():

        if '✅' not in sarimsoqli_sousretro[call.message.chat.id]:
            sarimsoqli_sousretro[call.message.chat.id] = "✅sarimsoqli sous"
        else:
            sarimsoqli_sousretro[call.message.chat.id] = "sarimsoqli sous"

    else:
        sarimsoqli_sousretro[call.message.chat.id] = "✅sarimsoqli sous"
    if call.message.chat.id not in sonretro.keys():
        sonretro[call.message.chat.id] = "kichik kartoshka-fri"

    if call.message.chat.id in quyma_colaretro:
        if 'quyma cola' in quyma_colaretro[call.message.chat.id]:
            cola_text = quyma_colaretro[call.message.chat.id]
        else:
            cola_text = "quyma cola"
    else:
        cola_text = "quyma cola"

    if call.message.chat.id in limonli_choyretro:
        if 'limonli choy' in limonli_choyretro[call.message.chat.id]:
            limonli_text = limonli_choyretro[call.message.chat.id]
        else:
            limonli_text = "limonli choy"
    else:
        limonli_text = "limonli choy"

    update_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minusretro"),
                InlineKeyboardButton(text=str(sonretro['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plusretro")
            ],
            [
                InlineKeyboardButton(text="⬇️ kartoshka-fri ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=sonretro[call.message.chat.id], callback_data="kichik_kartoshka_friretro")
            ],
            [
                InlineKeyboardButton(text="⬇️ siz tanlagan sous ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=f"{sarimsoqli_sousretro[call.message.chat.id]}", callback_data="sarimsoqli_sousretro"),
                InlineKeyboardButton(text=f"pishloqli sous", callback_data="pishloqli_sousretro"),
                InlineKeyboardButton(text=f"ketchup", callback_data="ketchupretro")
            ],

            [
                InlineKeyboardButton(text="⬇️ ichimlik ⬇️", callback_data="0")
            ],

            [
                InlineKeyboardButton(text=f'{cola_text}', callback_data="quyma_colaretro"),
                InlineKeyboardButton(text=f'{limonli_text}', callback_data="limonli_choyretro")
            ],

            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ],

        ]
    )
    global checkretro
    summa = 42000 * sonretro['count']
    new_caption = f"""
Maxi BOX Retro 
Shaurma Original, kartoshka fri, 0,4 l coca cola , tanlash uchun sous

Maxi BOX Retro 42 000 x {sonretro['count']} = {summa}
{checkretro}
{ssous_checkerretro(call.message.chat.id)}
{psous_checkerretro(call.message.chat.id)}
{ketchup_checkerretro(call.message.chat.id)}
{quyma_cola_checkerretro(call.message.chat.id)}
{limonli_choy_checkerretro(call.message.chat.id)}
Umumiy: {summa} UZS"""

    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/MaxiBoxRetro.jpg', 'rb'), caption=new_caption),
        reply_markup=update_button,
        # message_id=call.message.message_id,
        # chat_id=call.message.chat.id
    )


@dp.callback_query_handler(text='pishloqli_sousretro')
async def sous2retro(call: types.CallbackQuery):
    sarimsoqli_sousretro[call.message.chat.id] = "sarimsoqli sous"
    ketchupretro[call.message.chat.id] = 'ketchup'

    if call.message.chat.id in sonretro.keys():

        if '✅' not in pishloqli_sousretro[call.message.chat.id]:
            pishloqli_sousretro[call.message.chat.id] = "✅pishloqli sous"
        else:
            pishloqli_sousretro[call.message.chat.id] = "pishloqli sous"

    else:
        pishloqli_sousretro[call.message.chat.id] = "✅pishloqli sous"

    if call.message.chat.id not in sonretro.keys():
        sonretro[call.message.chat.id] = "kichik kartoshka-fri"

    if call.message.chat.id in quyma_colaretro:
        if 'quyma cola' in quyma_colaretro[call.message.chat.id]:
            cola_text = quyma_colaretro[call.message.chat.id]
        else:
            cola_text = "quyma cola"
    else:
        cola_text = "quyma cola"

    if call.message.chat.id in limonli_choyretro:
        if 'limonli choy' in limonli_choyretro[call.message.chat.id]:
            limonli_text = limonli_choyretro[call.message.chat.id]
        else:
            limonli_text = "limonli choy"
    else:
        limonli_text = "limonli choy"

    update_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minusretro"),
                InlineKeyboardButton(text=str(sonretro['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plusretro")
            ],
            [
                InlineKeyboardButton(text="⬇️ kartoshka-fri ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=sonretro[call.message.chat.id], callback_data="kichik_kartoshka_friretro")
            ],
            [
                InlineKeyboardButton(text="⬇️ siz tanlagan sous ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=f"{sarimsoqli_sousretro[call.message.chat.id]}", callback_data="sarimsoqli_sousretro"),
                InlineKeyboardButton(text=f"{pishloqli_sousretro[call.message.chat.id]}", callback_data="pishloqli_sousretro"),
                InlineKeyboardButton(text=f"ketchup", callback_data="ketchupretro")
            ],

            [
                InlineKeyboardButton(text="⬇️ ichimlik ⬇️", callback_data="0")
            ],

            [
                InlineKeyboardButton(text=f'{cola_text}', callback_data="quyma_colaretro"),
                InlineKeyboardButton(text=f'{limonli_text}', callback_data="limonli_choyretro")
            ],

            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ],

        ]
    )
    global checkretro
    summa = 42000 * sonretro['count']

    new_caption = f"""
Maxi BOX Retro 
Shaurma Original, kartoshka fri, 0,4 l coca cola , tanlash uchun sous

Maxi BOX Retro 42 000 x {sonretro['count']} = {summa}
{checkretro}
{ssous_checkerretro(call.message.chat.id)}
{psous_checkerretro(call.message.chat.id)}
{ketchup_checkerretro(call.message.chat.id)}
{quyma_cola_checkerretro(call.message.chat.id)}
{limonli_choy_checkerretro(call.message.chat.id)}
Umumiy: {summa} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/MaxiBoxRetro.jpg', 'rb'), caption=new_caption),
        reply_markup=update_button,
        # message_id=call.message.message_id,
        # chat_id=call.message.chat.id
    )


@dp.callback_query_handler(text='ketchupretro')
async def sous3retro(call: types.CallbackQuery):
    sarimsoqli_sousretro[call.message.chat.id] = "sarimsoqli sous"
    pishloqli_sousretro[call.message.chat.id] = 'pishloqli sous'

    if call.message.chat.id in sonretro.keys():

        if '✅' not in ketchupretro[call.message.chat.id]:
            ketchupretro[call.message.chat.id] = "✅ketchup"
        else:
            ketchupretro[call.message.chat.id] = "ketchup"

    else:
        ketchupretro[call.message.chat.id] = "✅ketchup"

    if call.message.chat.id not in sonretro.keys():
        sonretro[call.message.chat.id] = "kichik kartoshka-fri"

    if call.message.chat.id in quyma_colaretro:
        if 'quyma cola' in quyma_colaretro[call.message.chat.id]:
            cola_text = quyma_colaretro[call.message.chat.id]
        else:
            cola_text = "quyma cola"
    else:
        cola_text = "quyma cola"

    if call.message.chat.id in limonli_choyretro:
        if 'limonli choy' in limonli_choyretro[call.message.chat.id]:
            limonli_text = limonli_choyretro[call.message.chat.id]
        else:
            limonli_text = "limonli choy"
    else:
        limonli_text = "limonli choy"

    update_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minusretro"),
                InlineKeyboardButton(text=str(sonretro['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plusretro")
            ],
            [
                InlineKeyboardButton(text="⬇️ kartoshka-fri ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=sonretro[call.message.chat.id], callback_data="kichik_kartoshka_friretro")
            ],
            [
                InlineKeyboardButton(text="⬇️ siz tanlagan sous ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=f"{sarimsoqli_sousretro[call.message.chat.id]}", callback_data="sarimsoqli_sousretro"),
                InlineKeyboardButton(text=f"{pishloqli_sousretro[call.message.chat.id]}", callback_data="pishloqli_sousretro"),
                InlineKeyboardButton(text=f"{ketchupretro[call.message.chat.id]}", callback_data="ketchupretro")
            ],

            [
                InlineKeyboardButton(text="⬇️ ichimlik ⬇️", callback_data="0")
            ],

            [
                InlineKeyboardButton(text=f'{cola_text}', callback_data="quyma_colaretro"),
                InlineKeyboardButton(text=f'{limonli_text}', callback_data="limonli_choyretro")
            ],

            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ],

        ]
    )
    global checkretro
    summa = 42000 * sonretro['count']

    new_caption = f"""
Maxi BOX Retro 
Shaurma Original, kartoshka fri, 0,4 l coca cola , tanlash uchun sous

Maxi BOX Retro 42 000 x {sonretro['count']} = {summa}
{checkretro}
{ssous_checkerretro(call.message.chat.id)}
{psous_checkerretro(call.message.chat.id)}
{ketchup_checkerretro(call.message.chat.id)}
{quyma_cola_checkerretro(call.message.chat.id)}
{limonli_choy_checkerretro(call.message.chat.id)}
Umumiy: {summa} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/MaxiBoxRetro.jpg', 'rb'), caption=new_caption),
        reply_markup=update_button,
        # message_id=call.message.message_id,
        # chat_id=call.message.chat.id
    )


@dp.callback_query_handler(text='quyma_colaretro')
async def colaretro(call: types.CallbackQuery):
    limonli_choyretro[call.message.chat.id] = 'limonli choy'


    if call.message.chat.id in sonretro.keys():

        if '✅' not in quyma_colaretro[call.message.chat.id]:
            quyma_colaretro[call.message.chat.id] = "✅quyma cola"
        else:
            quyma_colaretro[call.message.chat.id] = "quyma cola"

    else:
        quyma_colaretro[call.message.chat.id] = "✅quyma cola"

    if call.message.chat.id in sarimsoqli_sousretro:
        if 'sarimsoqli sous' in sarimsoqli_sousretro[call.message.chat.id]:
            button_text = sarimsoqli_sousretro[call.message.chat.id]
        else:
            button_text = "sarimsoqli sous"
    else:
        button_text = "sarimsoqli sous"

    if call.message.chat.id in pishloqli_sousretro:
        if 'pishloqli sous' in pishloqli_sousretro[call.message.chat.id]:
            p_text = pishloqli_sousretro[call.message.chat.id]
        else:
            p_text = "pishloqli sous"
    else:
        p_text = "pishloqli sous"

    if call.message.chat.id in ketchupretro:
        if 'ketchup' in ketchupretro[call.message.chat.id]:
            k_text = ketchupretro[call.message.chat.id]
        else:
            k_text = "ketchup"
    else:
        k_text = "ketchup"

    if call.message.chat.id not in sonretro.keys():
        sonretro[call.message.chat.id] = "kichik kartoshka-fri"

    update_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minusretro"),
                InlineKeyboardButton(text=str(sonretro['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plusretro")
            ],
            [
                InlineKeyboardButton(text="⬇️ kartoshka-fri ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=sonretro[call.message.chat.id], callback_data="kichik_kartoshka_friretro")
            ],
            [
                InlineKeyboardButton(text="⬇️ siz tanlagan sous ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=f'{button_text}', callback_data="sarimsoqli_sousretro"),
                InlineKeyboardButton(text=f'{p_text}', callback_data="pishloqli_sousretro"),
                InlineKeyboardButton(text=f'{k_text}', callback_data="ketchupretro")
            ],

            [
                InlineKeyboardButton(text="⬇️ ichimlik ⬇️", callback_data="0")
            ],

            [
                InlineKeyboardButton(text=f"{quyma_colaretro[call.message.chat.id]}", callback_data="quyma_colaretro"),
                InlineKeyboardButton(text="limonli choy", callback_data="limonli_choyretro")
            ],

            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ],

        ]
    )
    global checkretro
    summa = 42000 * sonretro['count']

    new_caption = f"""
Maxi BOX Retro 
Shaurma Original, kartoshka fri, 0,4 l coca cola , tanlash uchun sous

Maxi BOX Retro 42 000 x {sonretro['count']} = {summa}
{checkretro}
{ssous_checkerretro(call.message.chat.id)}
{psous_checkerretro(call.message.chat.id)}
{ketchup_checkerretro(call.message.chat.id)}
{quyma_cola_checkerretro(call.message.chat.id)}
{limonli_choy_checkerretro(call.message.chat.id)}
Umumiy: {summa} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/MaxiBoxRetro.jpg', 'rb'), caption=new_caption),
        reply_markup=update_button,
        # message_id=call.message.message_id,
        # chat_id=call.message.chat.id
    )



@dp.callback_query_handler(text='limonli_choyretro')
async def limonliretro(call: types.CallbackQuery):
    quyma_colaretro[call.message.chat.id] = 'quyma cola'


    if call.message.chat.id in sonretro.keys():

        if '✅' not in limonli_choyretro[call.message.chat.id]:
            limonli_choyretro[call.message.chat.id] = "✅limonli choy"
        else:
            limonli_choyretro[call.message.chat.id] = "limonli choy"

    else:
        limonli_choyretro[call.message.chat.id] = "✅limonli choy"

    if call.message.chat.id in sarimsoqli_sousretro:
        if 'sarimsoqli sous' in sarimsoqli_sousretro[call.message.chat.id]:
            button_text = sarimsoqli_sousretro[call.message.chat.id]
        else:
            button_text = "sarimsoqli sous"
    else:
        button_text = "sarimsoqli sous"

    if call.message.chat.id in pishloqli_sousretro:
        if 'pishloqli sous' in pishloqli_sousretro[call.message.chat.id]:
            p_text = pishloqli_sousretro[call.message.chat.id]
        else:
            p_text = "pishloqli sous"
    else:
        p_text = "pishloqli sous"

    if call.message.chat.id in ketchupretro:
        if 'ketchup' in ketchupretro[call.message.chat.id]:
            k_text = ketchupretro[call.message.chat.id]
        else:
            k_text = "ketchup"
    else:
        k_text = "ketchup"

    if call.message.chat.id not in sonretro.keys():
        sonretro[call.message.chat.id] = "kichik kartoshka-fri"

    update_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minusretro"),
                InlineKeyboardButton(text=str(sonretro['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plusretro")
            ],
            [
                InlineKeyboardButton(text="⬇️ kartoshka-fri ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=sonretro[call.message.chat.id], callback_data="kichik_kartoshka_friretro")
            ],
            [
                InlineKeyboardButton(text="⬇️ siz tanlagan sous ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=f'{button_text}', callback_data="sarimsoqli_sousretro"),
                InlineKeyboardButton(text=f'{p_text}', callback_data="pishloqli_sousretro"),
                InlineKeyboardButton(text=f'{k_text}', callback_data="ketchupretro")
            ],

            [
                InlineKeyboardButton(text="⬇️ ichimlik ⬇️", callback_data="0")
            ],

            [
                InlineKeyboardButton(text=f"{quyma_colaretro[call.message.chat.id]}", callback_data="quyma_colaretro"),
                InlineKeyboardButton(text=f"{limonli_choyretro[call.message.chat.id]}", callback_data="limonli_choyretro")
            ],

            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ],

        ]
    )
    global checkretro
    summa = 42000 * sonretro['count']

    new_caption = f"""
Maxi BOX Retro 
Shaurma Original, kartoshka fri, 0,4 l coca cola , tanlash uchun sous

Maxi BOX Retro 42 000 x {sonretro['count']} = {summa}
{checkretro}
{ssous_checkerretro(call.message.chat.id)}
{psous_checkerretro(call.message.chat.id)}
{ketchup_checkerretro(call.message.chat.id)}
{quyma_cola_checkerretro(call.message.chat.id)}
{limonli_choy_checkerretro(call.message.chat.id)}
Umumiy: {summa} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/MaxiBoxRetro.jpg', 'rb'), caption=new_caption),
        reply_markup=update_button,
        # message_id=call.message.message_id,
        # chat_id=call.message.chat.id
    )