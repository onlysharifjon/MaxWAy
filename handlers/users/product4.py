from keyboards.default.menubuttons import sous
from keyboards.inline.inline_buttons import MaxiBoxGerman
from loader import dp
from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

checkgerman = None
songerman = {
    'count': 1,
    'kichik_kartorshka_fri': "kichik kartoshka-fri",
    'fri_caption': """
kartoshka-fri :
  - kichik kartoshka-fri      0 x 1 = 0  
""",
    'sarimsoq_caption': """""",
}
fri_narxgerman = {}

ketchupgerman = {'user_id': True}
pishloqli_sousgerman = {'user_id': True}
sarimsoqli_sousgerman = {'user_id': True}
quyma_colagerman = {'user_id':True}
limonli_choygerman = {'user_id':True}
def ssous_checkergerman(user_id):
    if user_id in sarimsoqli_sousgerman.keys():
        if '✅' in sarimsoqli_sousgerman[user_id]:
            return """
siz tanlagan sous :
- sarimsoqli sous      0 x 1 = 0  
    """
        else:
            return ''


def psous_checkergerman(user_id):
    if user_id in pishloqli_sousgerman.keys():
        if '✅' in pishloqli_sousgerman[user_id]:
            return """
siz tanlagan sous :
- pishloqli sous      0 x 1 = 0  
        """
        else:
            return ''


def ketchup_checkergerman(user_id):
    if user_id in ketchupgerman.keys():
        if '✅' in ketchupgerman[user_id]:
            return """
siz tanlagan sous :
- ketchup       0 x 1 = 0
        """
        else:
            return ''

def quyma_cola_checkergerman(user_id):
    if user_id in quyma_colagerman.keys():
        if '✅' in quyma_colagerman[user_id]:
            return """
ichimlik :
  - quyma cola       0 x 1 = 0
    """
        else:
            return ''

def limonli_choy_checkergerman(user_id):
    if user_id in limonli_choygerman.keys():
        if '✅' in limonli_choygerman[user_id]:
            return """
ichimlik :
  - limonli choy      0 x 1 = 0
    """
        else:
            return ''


@dp.message_handler(text="Max BOX German")
async def maxi_box_german(message: types.Message):
    ketchupgerman[message.from_user.id] = ''
    sarimsoqli_sousgerman[message.from_user.id] = ''
    pishloqli_sousgerman[message.from_user.id] = ''
    quyma_colagerman[message.from_user.id] = ''
    limonli_choygerman[message.from_user.id]=''

    await message.answer("Mahsulot miqdorini tanlang")
    await message.answer_photo(photo=open('images/MaxiBoxGerman.jpg', 'rb'), caption="""
Max BOX German 
German Donar , kartoshka fri, 0,4 l coca cola, tanlash uchun sous 

Maxi BOX German 45 000 x 1 = 45 000

Umumiy: 45 000 UZS""", reply_markup=MaxiBoxGerman)


@dp.callback_query_handler(text='plusgerman')
async def plusmaxiboxgerman(call: types.CallbackQuery):
    if call.message.chat.id not in songerman.keys():
        songerman[call.message.chat.id] = "kichik kartoshka-fri"
    else:
        if '✅' in songerman[call.message.chat.id]:
            songerman[call.message.chat.id] = "✅kichik kartoshka-fri"
        else:
            songerman[call.message.chat.id] = "kichik kartoshka-fri"

    print(songerman)
    songerman['count'] += 1

    if call.message.chat.id in sarimsoqli_sousgerman:
        if 'sarimsoqli sous' in sarimsoqli_sousgerman[call.message.chat.id]:
            button_text = sarimsoqli_sousgerman[call.message.chat.id]
        else:
            button_text = "sarimsoqli sous"
    else:
        button_text = "sarimsoqli sous"

    if call.message.chat.id in pishloqli_sousgerman:
        if 'pishloqli sous' in pishloqli_sousgerman[call.message.chat.id]:
            p_text = pishloqli_sousgerman[call.message.chat.id]
        else:
            p_text = "pishloqli sous"
    else:
        p_text = "pishloqli sous"

    if call.message.chat.id in ketchupgerman:
        if 'ketchup' in ketchupgerman[call.message.chat.id]:
            k_text = ketchupgerman[call.message.chat.id]
        else:
            k_text = "ketchup"
    else:
        k_text = "ketchup"

    if call.message.chat.id in quyma_colagerman:
        if 'quyma cola' in quyma_colagerman[call.message.chat.id]:
            cola_text = quyma_colagerman[call.message.chat.id]
        else:
            cola_text = "quyma cola"
    else:
        cola_text = "quyma cola"

    if call.message.chat.id in limonli_choygerman:
        if 'limonli choy' in limonli_choygerman[call.message.chat.id]:
            limonli_text = limonli_choygerman[call.message.chat.id]
        else:
            limonli_text = "limonli choy"
    else:
        limonli_text = "limonli choy"

    MaxiBoxGerman = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minusgerman"),
                InlineKeyboardButton(text=str(songerman['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plusgerman")
            ],
            [
                InlineKeyboardButton(text="⬇️ kartoshka-fri ⬇️", callback_data="0")
            ],
            {
                InlineKeyboardButton(text=songerman[call.message.chat.id], callback_data="kichik_kartoshka_frigerman")
            },
            [
                InlineKeyboardButton(text="⬇️ siz tanlagan sous ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=f'{button_text}', callback_data="sarimsoqli_sousgerman"),
                InlineKeyboardButton(text=f'{p_text}', callback_data="pishloqli_sousgerman"),
                InlineKeyboardButton(text=f'{k_text}', callback_data="ketchupgerman")
            ],
            [
                InlineKeyboardButton(text="⬇️ ichimlik ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=f'{cola_text}', callback_data="quyma_colagerman"),
                InlineKeyboardButton(text=f'{limonli_text}', callback_data="limonli_choygerman")
            ],
            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ]
        ]
    )
    if call.message.chat.id not in fri_narxgerman.keys():
        a = ''
    else:
        a = fri_narxgerman[call.message.chat.id]

    summa = 45000 * songerman['count']
    new_caption = f"""
Max BOX German 
German Donar , kartoshka fri, 0,4 l coca cola, tanlash uchun sous 

Maxi BOX German 45 000 x {songerman['count']} = {summa}
{a}
{ssous_checkergerman(call.message.chat.id)}
{psous_checkergerman(call.message.chat.id)}
{ketchup_checkergerman(call.message.chat.id)}
{quyma_cola_checkergerman(call.message.chat.id)}
{limonli_choy_checkergerman(call.message.chat.id)}
Umumiy: {summa} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/MaxiBoxGerman.jpg', 'rb'), chat_id=call.message.chat.id,
                                    message_id=call.message.message_id, caption=new_caption
                                    ), reply_markup=MaxiBoxGerman,
    )


@dp.callback_query_handler(text='minusgerman')
async def minusmaxiboxgerman(call: types.CallbackQuery):
    print(songerman)

    if songerman['count'] > 1:
        songerman['count'] -= 1

        if call.message.chat.id in sarimsoqli_sousgerman:
            if 'sarimsoqli sous' in sarimsoqli_sousgerman[call.message.chat.id]:
                button_text = sarimsoqli_sousgerman[call.message.chat.id]
            else:
                button_text = "sarimsoqli sous"
        else:
            button_text = "sarimsoqli sous"

        if call.message.chat.id in pishloqli_sousgerman:
            if 'pishloqli sous' in pishloqli_sousgerman[call.message.chat.id]:
                p_text = pishloqli_sousgerman[call.message.chat.id]
            else:
                p_text = "pishloqli sous"
        else:
            p_text = "pishloqli sous"

        if call.message.chat.id in ketchupgerman:
            if 'ketchup' in ketchupgerman[call.message.chat.id]:
                k_text = ketchupgerman[call.message.chat.id]
            else:
                k_text = "ketchup"
        else:
            k_text = "ketchup"

        if call.message.chat.id in quyma_colagerman:
            if 'quyma cola' in quyma_colagerman[call.message.chat.id]:
                cola_text = quyma_colagerman[call.message.chat.id]
            else:
                cola_text = "quyma cola"
        else:
            cola_text = "quyma cola"

        if call.message.chat.id in limonli_choygerman:
            if 'limonli choy' in limonli_choygerman[call.message.chat.id]:
                limonli_text = limonli_choygerman[call.message.chat.id]
            else:
                limonli_text = "limonli choy"
        else:
            limonli_text = "limonli choy"

        MaxiBoxGerman = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="minusgerman"),
                    InlineKeyboardButton(text=str(songerman['count']), callback_data='0'),
                    InlineKeyboardButton(text='+', callback_data="plusgerman")
                ],
                [
                    InlineKeyboardButton(text="⬇️ kartoshka-fri ⬇️", callback_data="0")
                ],
                [
                    InlineKeyboardButton(text=songerman[call.message.chat.id], callback_data="kichik_kartoshka_frigerman")
                ],
                [
                    InlineKeyboardButton(text="⬇️ siz tanlagan sous ⬇️", callback_data="0")
                ],
                [
                    InlineKeyboardButton(text=f"""{button_text}""", callback_data="sarimsoqli_sousgerman"),
                    InlineKeyboardButton(text=f'{p_text}', callback_data="pishloqli_sousgerman"),
                    InlineKeyboardButton(text=f'{k_text}', callback_data="ketchupgerman")
                ],
                [
                    InlineKeyboardButton(text="⬇️ ichimlik ⬇️", callback_data="0")
                ],
                [
                    InlineKeyboardButton(text=f'{cola_text}', callback_data="quyma_colagerman"),
                    InlineKeyboardButton(text=f'{limonli_text}', callback_data="limonli_choygerman")
                ],
                [
                    InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
                ]
            ]
        )

        if call.message.chat.id not in fri_narxgerman.keys():
            a = ''
        else:
            a = fri_narxgerman[call.message.chat.id]

        summa = 45000 * songerman['count']
        new_caption = f"""
Max BOX German 
German Donar , kartoshka fri, 0,4 l coca cola, tanlash uchun sous 

Maxi BOX German 45 000 x {songerman['count']} = {summa}
{a}
{ssous_checkergerman(call.message.chat.id)}
{psous_checkergerman(call.message.chat.id)}
{ketchup_checkergerman(call.message.chat.id)}
{quyma_cola_checkergerman(call.message.chat.id)}
{limonli_choy_checkergerman(call.message.chat.id)}
Umumiy: {summa} UZS"""

        await call.message.edit_media(
            media=types.InputMediaPhoto(open('images/MaxiBoxGerman.jpg', 'rb'), caption=new_caption),
            reply_markup=MaxiBoxGerman
        )
    else:
        await call.answer("1dan kam mahsulot tanlash mumkin emas")



@dp.callback_query_handler(text='kichik_kartoshka_frigerman')
async def kichikfrigerman(call: types.CallbackQuery):
    if call.message.chat.id not in fri_narxgerman.keys():
        fri_narxgerman[call.message.chat.id] = '''
kartoshka-fri :
  - kichik kartoshka-fri      0 x 1 = 0  
        '''
    else:
        del fri_narxgerman[call.message.chat.id]
    # try:
    #     print(son[call.message.chat.id])
    # except:
    #     son[call.message.chat.id] = "✅kichik kartoshka-fri"

    if call.message.chat.id in songerman.keys():

        if '✅' not in songerman[call.message.chat.id]:
            songerman[call.message.chat.id] = "✅kichik kartoshka-fri"
        else:
            songerman[call.message.chat.id] = "kichik kartoshka-fri"

    else:
        songerman[call.message.chat.id] = "✅kichik kartoshka-fri"

    if call.message.chat.id in sarimsoqli_sousgerman:
        if 'sarimsoqli sous' in sarimsoqli_sousgerman[call.message.chat.id]:
            button_text = sarimsoqli_sousgerman[call.message.chat.id]

        else:
            button_text = "sarimsoqli sous"
    else:
        button_text = "sarimsoqli sous"

    if call.message.chat.id in pishloqli_sousgerman:
        if 'pishloqli sous' in pishloqli_sousgerman[call.message.chat.id]:
            p_text = pishloqli_sousgerman[call.message.chat.id]
        else:
            p_text = "pishloqli sous"
    else:
        p_text = "pishloqli sous"

    if call.message.chat.id in ketchupgerman:
        if 'ketchup' in ketchupgerman[call.message.chat.id]:
            k_text = ketchupgerman[call.message.chat.id]
        else:
            k_text = "ketchup"
    else:
        k_text = "ketchup"

    if call.message.chat.id in quyma_colagerman:
        if 'quyma cola' in quyma_colagerman[call.message.chat.id]:
            cola_text = quyma_colagerman[call.message.chat.id]
        else:
            cola_text = "quyma cola"
    else:
        cola_text = "quyma cola"

    if call.message.chat.id in limonli_choygerman:
        if 'limonli choy' in limonli_choygerman[call.message.chat.id]:
            limonli_text = limonli_choygerman[call.message.chat.id]
        else:
            limonli_text = "limonli choy"
    else:
        limonli_text = "limonli choy"

    update_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minusgerman"),
                InlineKeyboardButton(text=str(songerman['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plusgerman")
            ],
            [
                InlineKeyboardButton(text="⬇️ kartoshka-fri ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=songerman[call.message.chat.id], callback_data="kichik_kartoshka_frigerman")
            ],
            [
                InlineKeyboardButton(text="⬇️ siz tanlagan sous ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=f'{button_text}', callback_data="sarimsoqli_sousgerman"),
                InlineKeyboardButton(text=f'{p_text}', callback_data="pishloqli_sousgerman"),
                InlineKeyboardButton(text=f'{k_text}', callback_data="ketchupgerman")
            ],

            [
                InlineKeyboardButton(text="⬇️ ichimlik ⬇️", callback_data="0")
            ],

            [
                InlineKeyboardButton(text=f'{cola_text}', callback_data="quyma_colagerman"),
                InlineKeyboardButton(text=f'{limonli_text}', callback_data="limonli_choygerman")
            ],

            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ],

        ]
    )
    summa = 45000 * songerman['count']
    global checkgerman
    print(songerman[call.message.chat.id])
    if '✅' in songerman[call.message.chat.id]:
        checkgerman = songerman['fri_caption']
    else:
        checkgerman = ''

    new_caption = f"""
Max BOX German 
German Donar , kartoshka fri, 0,4 l coca cola, tanlash uchun sous 

Maxi BOX German 45 000 x {songerman['count']} = {summa}
{checkgerman}
{ssous_checkergerman(call.message.chat.id)}
{psous_checkergerman(call.message.chat.id)}
{ketchup_checkergerman(call.message.chat.id)}
{quyma_cola_checkergerman(call.message.chat.id)}
{limonli_choy_checkergerman(call.message.chat.id)}
Umumiy: {summa} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/MaxiBoxGerman.jpg', 'rb'), caption=new_caption),
        reply_markup=update_button
    )
    print(songerman)


@dp.callback_query_handler(text='sarimsoqli_sousgerman')
async def sous1german(call: types.CallbackQuery):
    pishloqli_sousgerman[call.message.chat.id] = "pishloqli sous"
    ketchupgerman[call.message.chat.id] = 'ketchup'

    if call.message.chat.id in songerman.keys():

        if '✅' not in sarimsoqli_sousgerman[call.message.chat.id]:
            sarimsoqli_sousgerman[call.message.chat.id] = "✅sarimsoqli sous"
        else:
            sarimsoqli_sousgerman[call.message.chat.id] = "sarimsoqli sous"

    else:
        sarimsoqli_sousgerman[call.message.chat.id] = "✅sarimsoqli sous"
    if call.message.chat.id not in songerman.keys():
        songerman[call.message.chat.id] = "kichik kartoshka-fri"

    if call.message.chat.id in quyma_colagerman:
        if 'quyma cola' in quyma_colagerman[call.message.chat.id]:
            cola_text = quyma_colagerman[call.message.chat.id]
        else:
            cola_text = "quyma cola"
    else:
        cola_text = "quyma cola"

    if call.message.chat.id in limonli_choygerman:
        if 'limonli choy' in limonli_choygerman[call.message.chat.id]:
            limonli_text = limonli_choygerman[call.message.chat.id]
        else:
            limonli_text = "limonli choy"
    else:
        limonli_text = "limonli choy"

    update_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minusgerman"),
                InlineKeyboardButton(text=str(songerman['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plusgerman")
            ],
            [
                InlineKeyboardButton(text="⬇️ kartoshka-fri ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=songerman[call.message.chat.id], callback_data="kichik_kartoshka_frigerman")
            ],
            [
                InlineKeyboardButton(text="⬇️ siz tanlagan sous ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=f"{sarimsoqli_sousgerman[call.message.chat.id]}", callback_data="sarimsoqli_sousgerman"),
                InlineKeyboardButton(text=f"pishloqli sous", callback_data="pishloqli_sousgerman"),
                InlineKeyboardButton(text=f"ketchup", callback_data="ketchupgerman")
            ],

            [
                InlineKeyboardButton(text="⬇️ ichimlik ⬇️", callback_data="0")
            ],

            [
                InlineKeyboardButton(text=f'{cola_text}', callback_data="quyma_colagerman"),
                InlineKeyboardButton(text=f'{limonli_text}', callback_data="limonli_choygerman")
            ],

            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ],

        ]
    )
    global checkgerman
    summa = 45000 * songerman['count']
    new_caption = f"""
Max BOX German 
German Donar , kartoshka fri, 0,4 l coca cola, tanlash uchun sous 

Maxi BOX German 45 000 x {songerman['count']} = {summa}
{checkgerman}
{ssous_checkergerman(call.message.chat.id)}
{psous_checkergerman(call.message.chat.id)}
{ketchup_checkergerman(call.message.chat.id)}
{quyma_cola_checkergerman(call.message.chat.id)}
{limonli_choy_checkergerman(call.message.chat.id)}
Umumiy: {summa} UZS"""

    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/MaxiBoxGerman.jpg', 'rb'), caption=new_caption),
        reply_markup=update_button,
        # message_id=call.message.message_id,
        # chat_id=call.message.chat.id
    )


@dp.callback_query_handler(text='pishloqli_sousgerman')
async def sous2german(call: types.CallbackQuery):
    sarimsoqli_sousgerman[call.message.chat.id] = "sarimsoqli sous"
    ketchupgerman[call.message.chat.id] = 'ketchup'

    if call.message.chat.id in songerman.keys():

        if '✅' not in pishloqli_sousgerman[call.message.chat.id]:
            pishloqli_sousgerman[call.message.chat.id] = "✅pishloqli sous"
        else:
            pishloqli_sousgerman[call.message.chat.id] = "pishloqli sous"

    else:
        pishloqli_sousgerman[call.message.chat.id] = "✅pishloqli sous"

    if call.message.chat.id not in songerman.keys():
        songerman[call.message.chat.id] = "kichik kartoshka-fri"

    if call.message.chat.id in quyma_colagerman:
        if 'quyma cola' in quyma_colagerman[call.message.chat.id]:
            cola_text = quyma_colagerman[call.message.chat.id]
        else:
            cola_text = "quyma cola"
    else:
        cola_text = "quyma cola"

    if call.message.chat.id in limonli_choygerman:
        if 'limonli choy' in limonli_choygerman[call.message.chat.id]:
            limonli_text = limonli_choygerman[call.message.chat.id]
        else:
            limonli_text = "limonli choy"
    else:
        limonli_text = "limonli choy"

    update_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minusgerman"),
                InlineKeyboardButton(text=str(songerman['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plusgerman")
            ],
            [
                InlineKeyboardButton(text="⬇️ kartoshka-fri ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=songerman[call.message.chat.id], callback_data="kichik_kartoshka_frigerman")
            ],
            [
                InlineKeyboardButton(text="⬇️ siz tanlagan sous ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=f"{sarimsoqli_sousgerman[call.message.chat.id]}", callback_data="sarimsoqli_sousgermano"),
                InlineKeyboardButton(text=f"{pishloqli_sousgerman[call.message.chat.id]}", callback_data="pishloqli_sousgerman"),
                InlineKeyboardButton(text=f"ketchup", callback_data="ketchupgerman")
            ],

            [
                InlineKeyboardButton(text="⬇️ ichimlik ⬇️", callback_data="0")
            ],

            [
                InlineKeyboardButton(text=f'{cola_text}', callback_data="quyma_colagerman"),
                InlineKeyboardButton(text=f'{limonli_text}', callback_data="limonli_choygerman")
            ],

            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ],

        ]
    )
    global checkgerman
    summa = 45000 * songerman['count']

    new_caption = f"""
Max BOX German 
German Donar , kartoshka fri, 0,4 l coca cola, tanlash uchun sous 

Maxi BOX German 45 000 x {songerman['count']} = {summa}
{checkgerman}
{ssous_checkergerman(call.message.chat.id)}
{psous_checkergerman(call.message.chat.id)}
{ketchup_checkergerman(call.message.chat.id)}
{quyma_cola_checkergerman(call.message.chat.id)}
{limonli_choy_checkergerman(call.message.chat.id)}
Umumiy: {summa} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/MaxiBoxGerman.jpg', 'rb'), caption=new_caption),
        reply_markup=update_button,
        # message_id=call.message.message_id,
        # chat_id=call.message.chat.id
    )


@dp.callback_query_handler(text='ketchupgerman')
async def sous3german(call: types.CallbackQuery):
    sarimsoqli_sousgerman[call.message.chat.id] = "sarimsoqli sous"
    pishloqli_sousgerman[call.message.chat.id] = 'pishloqli sous'

    if call.message.chat.id in songerman.keys():

        if '✅' not in ketchupgerman[call.message.chat.id]:
            ketchupgerman[call.message.chat.id] = "✅ketchup"
        else:
            ketchupgerman[call.message.chat.id] = "ketchup"

    else:
        ketchupgerman[call.message.chat.id] = "✅ketchup"

    if call.message.chat.id not in songerman.keys():
        songerman[call.message.chat.id] = "kichik kartoshka-fri"

    if call.message.chat.id in quyma_colagerman:
        if 'quyma cola' in quyma_colagerman[call.message.chat.id]:
            cola_text = quyma_colagerman[call.message.chat.id]
        else:
            cola_text = "quyma cola"
    else:
        cola_text = "quyma cola"

    if call.message.chat.id in limonli_choygerman:
        if 'limonli choy' in limonli_choygerman[call.message.chat.id]:
            limonli_text = limonli_choygerman[call.message.chat.id]
        else:
            limonli_text = "limonli choy"
    else:
        limonli_text = "limonli choy"

    update_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minusgerman"),
                InlineKeyboardButton(text=str(songerman['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plusgerman")
            ],
            [
                InlineKeyboardButton(text="⬇️ kartoshka-fri ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=songerman[call.message.chat.id], callback_data="kichik_kartoshka_frigerman")
            ],
            [
                InlineKeyboardButton(text="⬇️ siz tanlagan sous ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=f"{sarimsoqli_sousgerman[call.message.chat.id]}", callback_data="sarimsoqli_sousgerman"),
                InlineKeyboardButton(text=f"{pishloqli_sousgerman[call.message.chat.id]}", callback_data="pishloqli_sousgerman"),
                InlineKeyboardButton(text=f"{ketchupgerman[call.message.chat.id]}", callback_data="ketchupgerman")
            ],

            [
                InlineKeyboardButton(text="⬇️ ichimlik ⬇️", callback_data="0")
            ],

            [
                InlineKeyboardButton(text=f'{cola_text}', callback_data="quyma_colagerman"),
                InlineKeyboardButton(text=f'{limonli_text}', callback_data="limonli_choygerman")
            ],

            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ],

        ]
    )
    global checkgerman
    summa = 45000 * songerman['count']

    new_caption = f"""
Max BOX German 
German Donar , kartoshka fri, 0,4 l coca cola, tanlash uchun sous 

Maxi BOX German 45 000 x {songerman['count']} = {summa}
{checkgerman}
{ssous_checkergerman(call.message.chat.id)}
{psous_checkergerman(call.message.chat.id)}
{ketchup_checkergerman(call.message.chat.id)}
{quyma_cola_checkergerman(call.message.chat.id)}
{limonli_choy_checkergerman(call.message.chat.id)}
Umumiy: {summa} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/MaxiBoxGerman.jpg', 'rb'), caption=new_caption),
        reply_markup=update_button,
        # message_id=call.message.message_id,
        # chat_id=call.message.chat.id
    )


@dp.callback_query_handler(text='quyma_colagerman')
async def colagerman(call: types.CallbackQuery):
    limonli_choygerman[call.message.chat.id] = 'limonli choy'


    if call.message.chat.id in songerman.keys():

        if '✅' not in quyma_colagerman[call.message.chat.id]:
            quyma_colagerman[call.message.chat.id] = "✅quyma cola"
        else:
            quyma_colagerman[call.message.chat.id] = "quyma cola"

    else:
        quyma_colagerman[call.message.chat.id] = "✅quyma cola"

    if call.message.chat.id in sarimsoqli_sousgerman:
        if 'sarimsoqli sous' in sarimsoqli_sousgerman[call.message.chat.id]:
            button_text = sarimsoqli_sousgerman[call.message.chat.id]
        else:
            button_text = "sarimsoqli sous"
    else:
        button_text = "sarimsoqli sous"

    if call.message.chat.id in pishloqli_sousgerman:
        if 'pishloqli sous' in pishloqli_sousgerman[call.message.chat.id]:
            p_text = pishloqli_sousgerman[call.message.chat.id]
        else:
            p_text = "pishloqli sous"
    else:
        p_text = "pishloqli sous"

    if call.message.chat.id in ketchupgerman:
        if 'ketchup' in ketchupgerman[call.message.chat.id]:
            k_text = ketchupgerman[call.message.chat.id]
        else:
            k_text = "ketchup"
    else:
        k_text = "ketchup"

    if call.message.chat.id not in songerman.keys():
        songerman[call.message.chat.id] = "kichik kartoshka-fri"

    update_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minusgerman"),
                InlineKeyboardButton(text=str(songerman['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plusgerman")
            ],
            [
                InlineKeyboardButton(text="⬇️ kartoshka-fri ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=songerman[call.message.chat.id], callback_data="kichik_kartoshka_frigerman")
            ],
            [
                InlineKeyboardButton(text="⬇️ siz tanlagan sous ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=f'{button_text}', callback_data="sarimsoqli_sousgerman"),
                InlineKeyboardButton(text=f'{p_text}', callback_data="pishloqli_sousgerman"),
                InlineKeyboardButton(text=f'{k_text}', callback_data="ketchupgerman")
            ],

            [
                InlineKeyboardButton(text="⬇️ ichimlik ⬇️", callback_data="0")
            ],

            [
                InlineKeyboardButton(text=f"{quyma_colagerman[call.message.chat.id]}", callback_data="quyma_colagerman"),
                InlineKeyboardButton(text="limonli choy", callback_data="limonli_choygerman")
            ],

            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ],

        ]
    )
    global checkgerman
    summa = 45000 * songerman['count']

    new_caption = f"""
Max BOX German 
German Donar , kartoshka fri, 0,4 l coca cola, tanlash uchun sous 

Maxi BOX German 45 000 x {songerman['count']} = {summa}
{checkgerman}
{ssous_checkergerman(call.message.chat.id)}
{psous_checkergerman(call.message.chat.id)}
{ketchup_checkergerman(call.message.chat.id)}
{quyma_cola_checkergerman(call.message.chat.id)}
{limonli_choy_checkergerman(call.message.chat.id)}
Umumiy: {summa} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/MaxiBoxGerman.jpg', 'rb'), caption=new_caption),
        reply_markup=update_button,
        # message_id=call.message.message_id,
        # chat_id=call.message.chat.id
    )



@dp.callback_query_handler(text='limonli_choygerman')
async def limonligerman(call: types.CallbackQuery):
    quyma_colagerman[call.message.chat.id] = 'quyma cola'


    if call.message.chat.id in songerman.keys():

        if '✅' not in limonli_choygerman[call.message.chat.id]:
            limonli_choygerman[call.message.chat.id] = "✅limonli choy"
        else:
            limonli_choygerman[call.message.chat.id] = "limonli choy"

    else:
        limonli_choygerman[call.message.chat.id] = "✅limonli choy"

    if call.message.chat.id in sarimsoqli_sousgerman:
        if 'sarimsoqli sous' in sarimsoqli_sousgerman[call.message.chat.id]:
            button_text = sarimsoqli_sousgerman[call.message.chat.id]
        else:
            button_text = "sarimsoqli sous"
    else:
        button_text = "sarimsoqli sous"

    if call.message.chat.id in pishloqli_sousgerman:
        if 'pishloqli sous' in pishloqli_sousgerman[call.message.chat.id]:
            p_text = pishloqli_sousgerman[call.message.chat.id]
        else:
            p_text = "pishloqli sous"
    else:
        p_text = "pishloqli sous"

    if call.message.chat.id in ketchupgerman:
        if 'ketchup' in ketchupgerman[call.message.chat.id]:
            k_text = ketchupgerman[call.message.chat.id]
        else:
            k_text = "ketchup"
    else:
        k_text = "ketchup"

    if call.message.chat.id not in songerman.keys():
        songerman[call.message.chat.id] = "kichik kartoshka-fri"

    update_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minusgerman"),
                InlineKeyboardButton(text=str(songerman['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plusgerman")
            ],
            [
                InlineKeyboardButton(text="⬇️ kartoshka-fri ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=songerman[call.message.chat.id], callback_data="kichik_kartoshka_frigerman")
            ],
            [
                InlineKeyboardButton(text="⬇️ siz tanlagan sous ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=f'{button_text}', callback_data="sarimsoqli_sousgerman"),
                InlineKeyboardButton(text=f'{p_text}', callback_data="pishloqli_sousgerman"),
                InlineKeyboardButton(text=f'{k_text}', callback_data="ketchupgerman")
            ],

            [
                InlineKeyboardButton(text="⬇️ ichimlik ⬇️", callback_data="0")
            ],

            [
                InlineKeyboardButton(text=f"{quyma_colagerman[call.message.chat.id]}", callback_data="quyma_colagerman"),
                InlineKeyboardButton(text=f"{limonli_choygerman[call.message.chat.id]}", callback_data="limonli_choygerman")
            ],

            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ],

        ]
    )
    global checkgerman
    summa = 45000 * songerman['count']

    new_caption = f"""
Max BOX German 
German Donar , kartoshka fri, 0,4 l coca cola, tanlash uchun sous 

Maxi BOX Geraman 45 000 x {songerman['count']} = {summa}
{checkgerman}
{ssous_checkergerman(call.message.chat.id)}
{psous_checkergerman(call.message.chat.id)}
{ketchup_checkergerman(call.message.chat.id)}
{quyma_cola_checkergerman(call.message.chat.id)}
{limonli_choy_checkergerman(call.message.chat.id)}
Umumiy: {summa} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/MaxiBoxGerman.jpg', 'rb'), caption=new_caption),
        reply_markup=update_button,
        # message_id=call.message.message_id,
        # chat_id=call.message.chat.id
    )