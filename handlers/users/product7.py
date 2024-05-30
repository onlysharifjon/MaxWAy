from keyboards.default.menubuttons import sous
from keyboards.inline.inline_buttons import MaxiBoxTrendvich
from loader import dp
from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

checktrendvich = None
sontrendvich = {
    'count': 1,
    'kichik_kartorshka_fri': "kichik kartoshka-fri",
    'fri_caption': """
kartoshka-fri :
  - kichik kartoshka-fri      0 x 1 = 0  
""",
    'sarimsoq_caption': """""",
}
fri_narxtrendvich = {}

ketchuptrendvich = {'user_id': True}
pishloqli_soustrendvich = {'user_id': True}
sarimsoqli_soustrendvich = {'user_id': True}
quyma_colatrendvich = {'user_id':True}
limonli_choytrendvich = {'user_id':True}
def ssous_checkertrendvich(user_id):
    if user_id in sarimsoqli_soustrendvich.keys():
        if '✅' in sarimsoqli_soustrendvich[user_id]:
            return """
siz tanlagan sous :
- sarimsoqli sous      0 x 1 = 0  
    """
        else:
            return ''


def psous_checkertrendvich(user_id):
    if user_id in pishloqli_soustrendvich.keys():
        if '✅' in pishloqli_soustrendvich[user_id]:
            return """
siz tanlagan sous :
- pishloqli sous      0 x 1 = 0  
        """
        else:
            return ''


def ketchup_checkertrendvich(user_id):
    if user_id in ketchuptrendvich.keys():
        if '✅' in ketchuptrendvich[user_id]:
            return """
siz tanlagan sous :
- ketchup       0 x 1 = 0
        """
        else:
            return ''

def quyma_cola_checkertrendvich(user_id):
    if user_id in quyma_colatrendvich.keys():
        if '✅' in quyma_colatrendvich[user_id]:
            return """
ichimlik :
  - quyma cola       0 x 1 = 0
    """
        else:
            return ''

def limonli_choy_checkertrendvich(user_id):
    if user_id in limonli_choytrendvich.keys():
        if '✅' in limonli_choytrendvich[user_id]:
            return """
ichimlik :
  - limonli choy      0 x 1 = 0
    """
        else:
            return ''


@dp.message_handler(text="Maxi BOX Trendvich")
async def maxi_box_trendvich(message: types.Message):
    ketchuptrendvich[message.from_user.id] = ''
    sarimsoqli_soustrendvich[message.from_user.id] = ''
    pishloqli_soustrendvich[message.from_user.id] = ''
    quyma_colatrendvich[message.from_user.id] = ''
    limonli_choytrendvich[message.from_user.id]=''

    await message.answer("Mahsulot miqdorini tanlang")
    await message.answer_photo(photo=open('images/Maxiboxtrendvich.jpg', 'rb'), caption="""
Maxi BOX Trendvich 
Trendvich, kartoshka fri, 0,4 l coca cola, tanlash uchun sous 

Maxi BOX Trendvich 45 000 x 1 = 45 000

Umumiy: 45 000 UZS""", reply_markup=MaxiBoxTrendvich)


@dp.callback_query_handler(text='plustrendvich')
async def plusmaxiboxtrendvich(call: types.CallbackQuery):
    if call.message.chat.id not in sontrendvich.keys():
        sontrendvich[call.message.chat.id] = "kichik kartoshka-fri"
    else:
        if '✅' in sontrendvich[call.message.chat.id]:
            sontrendvich[call.message.chat.id] = "✅kichik kartoshka-fri"
        else:
            sontrendvich[call.message.chat.id] = "kichik kartoshka-fri"

    print(sontrendvich)
    sontrendvich['count'] += 1

    if call.message.chat.id in sarimsoqli_soustrendvich:
        if 'sarimsoqli sous' in sarimsoqli_soustrendvich[call.message.chat.id]:
            button_text = sarimsoqli_soustrendvich[call.message.chat.id]
        else:
            button_text = "sarimsoqli sous"
    else:
        button_text = "sarimsoqli sous"

    if call.message.chat.id in pishloqli_soustrendvich:
        if 'pishloqli sous' in pishloqli_soustrendvich[call.message.chat.id]:
            p_text = pishloqli_soustrendvich[call.message.chat.id]
        else:
            p_text = "pishloqli sous"
    else:
        p_text = "pishloqli sous"

    if call.message.chat.id in ketchuptrendvich:
        if 'ketchup' in ketchuptrendvich[call.message.chat.id]:
            k_text = ketchuptrendvich[call.message.chat.id]
        else:
            k_text = "ketchup"
    else:
        k_text = "ketchup"

    if call.message.chat.id in quyma_colatrendvich:
        if 'quyma cola' in quyma_colatrendvich[call.message.chat.id]:
            cola_text = quyma_colatrendvich[call.message.chat.id]
        else:
            cola_text = "quyma cola"
    else:
        cola_text = "quyma cola"

    if call.message.chat.id in limonli_choytrendvich:
        if 'limonli choy' in limonli_choytrendvich[call.message.chat.id]:
            limonli_text = limonli_choytrendvich[call.message.chat.id]
        else:
            limonli_text = "limonli choy"
    else:
        limonli_text = "limonli choy"

    MaxiBoxTrendvich = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minustrendvich"),
                InlineKeyboardButton(text=str(sontrendvich['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plustrendvich")
            ],
            [
                InlineKeyboardButton(text="⬇️ kartoshka-fri ⬇️", callback_data="0")
            ],
            {
                InlineKeyboardButton(text=sontrendvich[call.message.chat.id], callback_data="kichik_kartoshka_fritrendvich")
            },
            [
                InlineKeyboardButton(text="⬇️ siz tanlagan sous ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=f'{button_text}', callback_data="sarimsoqli_soustrendvich"),
                InlineKeyboardButton(text=f'{p_text}', callback_data="pishloqli_soustrendvich"),
                InlineKeyboardButton(text=f'{k_text}', callback_data="ketchuptrendvich")
            ],
            [
                InlineKeyboardButton(text="⬇️ ichimlik ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=f'{cola_text}', callback_data="quyma_colatrendvich"),
                InlineKeyboardButton(text=f'{limonli_text}', callback_data="limonli_choytrendvich")
            ],
            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ]
        ]
    )
    if call.message.chat.id not in fri_narxtrendvich.keys():
        a = ''
    else:
        a = fri_narxtrendvich[call.message.chat.id]

    summa = 45000 * sontrendvich['count']
    new_caption = f"""
Maxi BOX Trendvich 
Trendvich, kartoshka fri, 0,4 l coca cola, tanlash uchun sous

Maxi BOX Trendvich 45 000 x {sontrendvich['count']} = {summa}
{a}
{ssous_checkertrendvich(call.message.chat.id)}
{psous_checkertrendvich(call.message.chat.id)}
{ketchup_checkertrendvich(call.message.chat.id)}
{quyma_cola_checkertrendvich(call.message.chat.id)}
{limonli_choy_checkertrendvich(call.message.chat.id)}
Umumiy: {summa} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/Maxiboxtrendvich.jpg', 'rb'), chat_id=call.message.chat.id,
                                    message_id=call.message.message_id, caption=new_caption
                                    ), reply_markup=MaxiBoxTrendvich,
    )


@dp.callback_query_handler(text='minustrendvich')
async def minusmaxiboxtrendvich(call: types.CallbackQuery):
    print(sontrendvich)

    if sontrendvich['count'] > 1:
        sontrendvich['count'] -= 1

        if call.message.chat.id in sarimsoqli_soustrendvich:
            if 'sarimsoqli sous' in sarimsoqli_soustrendvich[call.message.chat.id]:
                button_text = sarimsoqli_soustrendvich[call.message.chat.id]
            else:
                button_text = "sarimsoqli sous"
        else:
            button_text = "sarimsoqli sous"

        if call.message.chat.id in pishloqli_soustrendvich:
            if 'pishloqli sous' in pishloqli_soustrendvich[call.message.chat.id]:
                p_text = pishloqli_soustrendvich[call.message.chat.id]
            else:
                p_text = "pishloqli sous"
        else:
            p_text = "pishloqli sous"

        if call.message.chat.id in ketchuptrendvich:
            if 'ketchup' in ketchuptrendvich[call.message.chat.id]:
                k_text = ketchuptrendvich[call.message.chat.id]
            else:
                k_text = "ketchup"
        else:
            k_text = "ketchup"

        if call.message.chat.id in quyma_colatrendvich:
            if 'quyma cola' in quyma_colatrendvich[call.message.chat.id]:
                cola_text = quyma_colatrendvich[call.message.chat.id]
            else:
                cola_text = "quyma cola"
        else:
            cola_text = "quyma cola"

        if call.message.chat.id in limonli_choytrendvich:
            if 'limonli choy' in limonli_choytrendvich[call.message.chat.id]:
                limonli_text = limonli_choytrendvich[call.message.chat.id]
            else:
                limonli_text = "limonli choy"
        else:
            limonli_text = "limonli choy"

        MaxiBoxTrendvich = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="minustrendvich"),
                    InlineKeyboardButton(text=str(sontrendvich['count']), callback_data='0'),
                    InlineKeyboardButton(text='+', callback_data="plustrendvich")
                ],
                [
                    InlineKeyboardButton(text="⬇️ kartoshka-fri ⬇️", callback_data="0")
                ],
                [
                    InlineKeyboardButton(text=sontrendvich[call.message.chat.id], callback_data="kichik_kartoshka_fritrendvich")
                ],
                [
                    InlineKeyboardButton(text="⬇️ siz tanlagan sous ⬇️", callback_data="0")
                ],
                [
                    InlineKeyboardButton(text=f"""{button_text}""", callback_data="sarimsoqli_soustrendvich"),
                    InlineKeyboardButton(text=f'{p_text}', callback_data="pishloqli_soustrendvich"),
                    InlineKeyboardButton(text=f'{k_text}', callback_data="ketchuptrendvich")
                ],
                [
                    InlineKeyboardButton(text="⬇️ ichimlik ⬇️", callback_data="0")
                ],
                [
                    InlineKeyboardButton(text=f'{cola_text}', callback_data="quyma_colatrendvich"),
                    InlineKeyboardButton(text=f'{limonli_text}', callback_data="limonli_choytrendvich")
                ],
                [
                    InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
                ]
            ]
        )

        if call.message.chat.id not in fri_narxtrendvich.keys():
            a = ''
        else:
            a = fri_narxtrendvich[call.message.chat.id]

        summa = 45000 * sontrendvich['count']
        new_caption = f"""
Maxi BOX Trendvich 
Trendvich, kartoshka fri, 0,4 l coca cola, tanlash uchun sous

Maxi BOX Trendvich 45 000 x {sontrendvich['count']} = {summa}
{a}
{ssous_checkertrendvich(call.message.chat.id)}
{psous_checkertrendvich(call.message.chat.id)}
{ketchup_checkertrendvich(call.message.chat.id)}
{quyma_cola_checkertrendvich(call.message.chat.id)}
{limonli_choy_checkertrendvich(call.message.chat.id)}
Umumiy: {summa} UZS"""

        await call.message.edit_media(
            media=types.InputMediaPhoto(open('images/Maxiboxtrendvich.jpg', 'rb'), caption=new_caption),
            reply_markup=MaxiBoxTrendvich
        )
    else:
        await call.answer("1dan kam mahsulot tanlash mumkin emas")



@dp.callback_query_handler(text='kichik_kartoshka_fritrendvich')
async def kichikfritrendvich(call: types.CallbackQuery):
    if call.message.chat.id not in fri_narxtrendvich.keys():
        fri_narxtrendvich[call.message.chat.id] = '''
kartoshka-fri :
  - kichik kartoshka-fri      0 x 1 = 0  
        '''
    else:
        del fri_narxtrendvich[call.message.chat.id]
    # try:
    #     print(son[call.message.chat.id])
    # except:
    #     son[call.message.chat.id] = "✅kichik kartoshka-fri"

    if call.message.chat.id in sontrendvich.keys():

        if '✅' not in sontrendvich[call.message.chat.id]:
            sontrendvich[call.message.chat.id] = "✅kichik kartoshka-fri"
        else:
            sontrendvich[call.message.chat.id] = "kichik kartoshka-fri"

    else:
        sontrendvich[call.message.chat.id] = "✅kichik kartoshka-fri"

    if call.message.chat.id in sarimsoqli_soustrendvich:
        if 'sarimsoqli sous' in sarimsoqli_soustrendvich[call.message.chat.id]:
            button_text = sarimsoqli_soustrendvich[call.message.chat.id]
        else:
            button_text = "sarimsoqli sous"
    else:
        button_text = "sarimsoqli sous"

    if call.message.chat.id in pishloqli_soustrendvich:
        if 'pishloqli sous' in pishloqli_soustrendvich[call.message.chat.id]:
            p_text = pishloqli_soustrendvich[call.message.chat.id]
        else:
            p_text = "pishloqli sous"
    else:
        p_text = "pishloqli sous"

    if call.message.chat.id in ketchuptrendvich:
        if 'ketchup' in ketchuptrendvich[call.message.chat.id]:
            k_text = ketchuptrendvich[call.message.chat.id]
        else:
            k_text = "ketchup"
    else:
        k_text = "ketchup"

    if call.message.chat.id in quyma_colatrendvich:
        if 'quyma cola' in quyma_colatrendvich[call.message.chat.id]:
            cola_text = quyma_colatrendvich[call.message.chat.id]
        else:
            cola_text = "quyma cola"
    else:
        cola_text = "quyma cola"

    if call.message.chat.id in limonli_choytrendvich:
        if 'limonli choy' in limonli_choytrendvich[call.message.chat.id]:
            limonli_text = limonli_choytrendvich[call.message.chat.id]
        else:
            limonli_text = "limonli choy"
    else:
        limonli_text = "limonli choy"

    update_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minustrendvich"),
                InlineKeyboardButton(text=str(sontrendvich['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plustrendvich")
            ],
            [
                InlineKeyboardButton(text="⬇️ kartoshka-fri ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=sontrendvich[call.message.chat.id], callback_data="kichik_kartoshka_fritrendvich")
            ],
            [
                InlineKeyboardButton(text="⬇️ siz tanlagan sous ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=f'{button_text}', callback_data="sarimsoqli_soustrendvich"),
                InlineKeyboardButton(text=f'{p_text}', callback_data="pishloqli_soustrendvich"),
                InlineKeyboardButton(text=f'{k_text}', callback_data="ketchuptrendvich")
            ],

            [
                InlineKeyboardButton(text="⬇️ ichimlik ⬇️", callback_data="0")
            ],

            [
                InlineKeyboardButton(text=f'{cola_text}', callback_data="quyma_colatrendvich"),
                InlineKeyboardButton(text=f'{limonli_text}', callback_data="limonli_choytrendvich")
            ],

            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ],

        ]
    )
    summa = 45000 * sontrendvich['count']
    global checktrendvich
    print(sontrendvich[call.message.chat.id])
    if '✅' in sontrendvich[call.message.chat.id]:
        checktrendvich = sontrendvich['fri_caption']
    else:
        checktrendvich = ''

    new_caption = f"""
Maxi BOX Trendvich 
Trendvich, kartoshka fri, 0,4 l coca cola, tanlash uchun sous

Maxi BOX Trendvich 45 000 x {sontrendvich['count']} = {summa}
{checktrendvich}
{ssous_checkertrendvich(call.message.chat.id)}
{psous_checkertrendvich(call.message.chat.id)}
{ketchup_checkertrendvich(call.message.chat.id)}
{quyma_cola_checkertrendvich(call.message.chat.id)}
{limonli_choy_checkertrendvich(call.message.chat.id)}
Umumiy: {summa} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/Maxiboxtrendvich.jpg', 'rb'), caption=new_caption),
        reply_markup=update_button
    )
    print(sontrendvich)


@dp.callback_query_handler(text='sarimsoqli_soustrendvich')
async def sous1trendvich(call: types.CallbackQuery):
    pishloqli_soustrendvich[call.message.chat.id] = "pishloqli sous"
    ketchuptrendvich[call.message.chat.id] = 'ketchup'

    if call.message.chat.id in sontrendvich.keys():

        if '✅' not in sarimsoqli_soustrendvich[call.message.chat.id]:
            sarimsoqli_soustrendvich[call.message.chat.id] = "✅sarimsoqli sous"
        else:
            sarimsoqli_soustrendvich[call.message.chat.id] = "sarimsoqli sous"

    else:
        sarimsoqli_soustrendvich[call.message.chat.id] = "✅sarimsoqli sous"
    if call.message.chat.id not in sontrendvich.keys():
        sontrendvich[call.message.chat.id] = "kichik kartoshka-fri"

    if call.message.chat.id in quyma_colatrendvich:
        if 'quyma cola' in quyma_colatrendvich[call.message.chat.id]:
            cola_text = quyma_colatrendvich[call.message.chat.id]
        else:
            cola_text = "quyma cola"
    else:
        cola_text = "quyma cola"

    if call.message.chat.id in limonli_choytrendvich:
        if 'limonli choy' in limonli_choytrendvich[call.message.chat.id]:
            limonli_text = limonli_choytrendvich[call.message.chat.id]
        else:
            limonli_text = "limonli choy"
    else:
        limonli_text = "limonli choy"

    update_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minustrendvich"),
                InlineKeyboardButton(text=str(sontrendvich['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plustrendvich")
            ],
            [
                InlineKeyboardButton(text="⬇️ kartoshka-fri ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=sontrendvich[call.message.chat.id], callback_data="kichik_kartoshka_fritrendvich")
            ],
            [
                InlineKeyboardButton(text="⬇️ siz tanlagan sous ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=f"{sarimsoqli_soustrendvich[call.message.chat.id]}", callback_data="sarimsoqli_soustrendvich"),
                InlineKeyboardButton(text=f"pishloqli sous", callback_data="pishloqli_soustrendvich"),
                InlineKeyboardButton(text=f"ketchup", callback_data="ketchuptrendvich")
            ],

            [
                InlineKeyboardButton(text="⬇️ ichimlik ⬇️", callback_data="0")
            ],

            [
                InlineKeyboardButton(text=f'{cola_text}', callback_data="quyma_colatrendvich"),
                InlineKeyboardButton(text=f'{limonli_text}', callback_data="limonli_choytrendvich")
            ],

            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ],

        ]
    )
    global checktrendvich
    summa = 45000 * sontrendvich['count']
    new_caption = f"""
Maxi BOX Trendvich 
Trendvich, kartoshka fri, 0,4 l coca cola, tanlash uchun sous

Maxi BOX Trendvich 45 000 x {sontrendvich['count']} = {summa}
{checktrendvich}
{ssous_checkertrendvich(call.message.chat.id)}
{psous_checkertrendvich(call.message.chat.id)}
{ketchup_checkertrendvich(call.message.chat.id)}
{quyma_cola_checkertrendvich(call.message.chat.id)}
{limonli_choy_checkertrendvich(call.message.chat.id)}
Umumiy: {summa} UZS"""

    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/Maxiboxtrendvich.jpg', 'rb'), caption=new_caption),
        reply_markup=update_button,
        # message_id=call.message.message_id,
        # chat_id=call.message.chat.id
    )


@dp.callback_query_handler(text='pishloqli_soustrendvich')
async def sous2trendvich(call: types.CallbackQuery):
    sarimsoqli_soustrendvich[call.message.chat.id] = "sarimsoqli sous"
    ketchuptrendvich[call.message.chat.id] = 'ketchup'

    if call.message.chat.id in sontrendvich.keys():

        if '✅' not in pishloqli_soustrendvich[call.message.chat.id]:
            pishloqli_soustrendvich[call.message.chat.id] = "✅pishloqli sous"
        else:
            pishloqli_soustrendvich[call.message.chat.id] = "pishloqli sous"

    else:
        pishloqli_soustrendvich[call.message.chat.id] = "✅pishloqli sous"

    if call.message.chat.id not in sontrendvich.keys():
        sontrendvich[call.message.chat.id] = "kichik kartoshka-fri"

    if call.message.chat.id in quyma_colatrendvich:
        if 'quyma cola' in quyma_colatrendvich[call.message.chat.id]:
            cola_text = quyma_colatrendvich[call.message.chat.id]
        else:
            cola_text = "quyma cola"
    else:
        cola_text = "quyma cola"

    if call.message.chat.id in limonli_choytrendvich:
        if 'limonli choy' in limonli_choytrendvich[call.message.chat.id]:
            limonli_text = limonli_choytrendvich[call.message.chat.id]
        else:
            limonli_text = "limonli choy"
    else:
        limonli_text = "limonli choy"

    update_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minustrendvich"),
                InlineKeyboardButton(text=str(sontrendvich['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plustrendvich")
            ],
            [
                InlineKeyboardButton(text="⬇️ kartoshka-fri ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=sontrendvich[call.message.chat.id], callback_data="kichik_kartoshka_fritrendvich")
            ],
            [
                InlineKeyboardButton(text="⬇️ siz tanlagan sous ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=f"{sarimsoqli_soustrendvich[call.message.chat.id]}", callback_data="sarimsoqli_soustrendvich"),
                InlineKeyboardButton(text=f"{pishloqli_soustrendvich[call.message.chat.id]}", callback_data="pishloqli_soustrendvich"),
                InlineKeyboardButton(text=f"ketchup", callback_data="ketchup")
            ],

            [
                InlineKeyboardButton(text="⬇️ ichimlik ⬇️", callback_data="0")
            ],

            [
                InlineKeyboardButton(text=f'{cola_text}', callback_data="quyma_colatrendvich"),
                InlineKeyboardButton(text=f'{limonli_text}', callback_data="limonli_choytrendvich")
            ],

            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ],

        ]
    )
    global checktrendvich
    summa = 45000 * sontrendvich['count']

    new_caption = f"""
Maxi BOX Trendvich 
Trendvich, kartoshka fri, 0,4 l coca cola, tanlash uchun sous

Maxi BOX Trendvich 45 000 x {sontrendvich['count']} = {summa}
{checktrendvich}
{ssous_checkertrendvich(call.message.chat.id)}
{psous_checkertrendvich(call.message.chat.id)}
{ketchup_checkertrendvich(call.message.chat.id)}
{quyma_cola_checkertrendvich(call.message.chat.id)}
{limonli_choy_checkertrendvich(call.message.chat.id)}
Umumiy: {summa} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/Maxiboxtrendvich.jpg', 'rb'), caption=new_caption),
        reply_markup=update_button,
        # message_id=call.message.message_id,
        # chat_id=call.message.chat.id
    )


@dp.callback_query_handler(text='ketchuptrendvich')
async def sous3trendvich(call: types.CallbackQuery):
    sarimsoqli_soustrendvich[call.message.chat.id] = "sarimsoqli sous"
    pishloqli_soustrendvich[call.message.chat.id] = 'pishloqli sous'

    if call.message.chat.id in sontrendvich.keys():

        if '✅' not in ketchuptrendvich[call.message.chat.id]:
            ketchuptrendvich[call.message.chat.id] = "✅ketchup"
        else:
            ketchuptrendvich[call.message.chat.id] = "ketchup"

    else:
        ketchuptrendvich[call.message.chat.id] = "✅ketchup"

    if call.message.chat.id not in sontrendvich.keys():
        sontrendvich[call.message.chat.id] = "kichik kartoshka-fri"

    if call.message.chat.id in quyma_colatrendvich:
        if 'quyma cola' in quyma_colatrendvich[call.message.chat.id]:
            cola_text = quyma_colatrendvich[call.message.chat.id]
        else:
            cola_text = "quyma cola"
    else:
        cola_text = "quyma cola"

    if call.message.chat.id in limonli_choytrendvich:
        if 'limonli choy' in limonli_choytrendvich[call.message.chat.id]:
            limonli_text = limonli_choytrendvich[call.message.chat.id]
        else:
            limonli_text = "limonli choy"
    else:
        limonli_text = "limonli choy"

    update_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minustrendvich"),
                InlineKeyboardButton(text=str(sontrendvich['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plustrendvich")
            ],
            [
                InlineKeyboardButton(text="⬇️ kartoshka-fri ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=sontrendvich[call.message.chat.id], callback_data="kichik_kartoshka_fritrendvich")
            ],
            [
                InlineKeyboardButton(text="⬇️ siz tanlagan sous ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=f"{sarimsoqli_soustrendvich[call.message.chat.id]}", callback_data="sarimsoqli_soustrendvich"),
                InlineKeyboardButton(text=f"{pishloqli_soustrendvich[call.message.chat.id]}", callback_data="pishloqli_soustrendvich"),
                InlineKeyboardButton(text=f"{ketchuptrendvich[call.message.chat.id]}", callback_data="ketchuptrendvich")
            ],

            [
                InlineKeyboardButton(text="⬇️ ichimlik ⬇️", callback_data="0")
            ],

            [
                InlineKeyboardButton(text=f'{cola_text}', callback_data="quyma_colatrendvich"),
                InlineKeyboardButton(text=f'{limonli_text}', callback_data="limonli_choytrendvich")
            ],

            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ],

        ]
    )
    global checktrendvich
    summa = 45000 * sontrendvich['count']

    new_caption = f"""
Maxi BOX Trendvich 
Trendvich, kartoshka fri, 0,4 l coca cola, tanlash uchun sous

Maxi BOX Trendvich 45 000 x {sontrendvich['count']} = {summa}
{checktrendvich}
{ssous_checkertrendvich(call.message.chat.id)}
{psous_checkertrendvich(call.message.chat.id)}
{ketchup_checkertrendvich(call.message.chat.id)}
{quyma_cola_checkertrendvich(call.message.chat.id)}
{limonli_choy_checkertrendvich(call.message.chat.id)}
Umumiy: {summa} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/Maxiboxtrendvich.jpg', 'rb'), caption=new_caption),
        reply_markup=update_button,
        # message_id=call.message.message_id,
        # chat_id=call.message.chat.id
    )


@dp.callback_query_handler(text='quyma_colatrendvich')
async def colatrendvich(call: types.CallbackQuery):
    limonli_choytrendvich[call.message.chat.id] = 'limonli choy'


    if call.message.chat.id in sontrendvich.keys():

        if '✅' not in quyma_colatrendvich[call.message.chat.id]:
            quyma_colatrendvich[call.message.chat.id] = "✅quyma cola"
        else:
            quyma_colatrendvich[call.message.chat.id] = "quyma cola"

    else:
        quyma_colatrendvich[call.message.chat.id] = "✅quyma cola"

    if call.message.chat.id in sarimsoqli_soustrendvich:
        if 'sarimsoqli sous' in sarimsoqli_soustrendvich[call.message.chat.id]:
            button_text = sarimsoqli_soustrendvich[call.message.chat.id]
        else:
            button_text = "sarimsoqli sous"
    else:
        button_text = "sarimsoqli sous"

    if call.message.chat.id in pishloqli_soustrendvich:
        if 'pishloqli sous' in pishloqli_soustrendvich[call.message.chat.id]:
            p_text = pishloqli_soustrendvich[call.message.chat.id]
        else:
            p_text = "pishloqli sous"
    else:
        p_text = "pishloqli sous"

    if call.message.chat.id in ketchuptrendvich:
        if 'ketchup' in ketchuptrendvich[call.message.chat.id]:
            k_text = ketchuptrendvich[call.message.chat.id]
        else:
            k_text = "ketchup"
    else:
        k_text = "ketchup"

    if call.message.chat.id not in sontrendvich.keys():
        sontrendvich[call.message.chat.id] = "kichik kartoshka-fri"

    update_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minustrendvich"),
                InlineKeyboardButton(text=str(sontrendvich['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plustrendvich")
            ],
            [
                InlineKeyboardButton(text="⬇️ kartoshka-fri ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=sontrendvich[call.message.chat.id], callback_data="kichik_kartoshka_fritrendvich")
            ],
            [
                InlineKeyboardButton(text="⬇️ siz tanlagan sous ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=f'{button_text}', callback_data="sarimsoqli_soustrendvich"),
                InlineKeyboardButton(text=f'{p_text}', callback_data="pishloqli_soustrendvich"),
                InlineKeyboardButton(text=f'{k_text}', callback_data="ketchuptrendvich")
            ],

            [
                InlineKeyboardButton(text="⬇️ ichimlik ⬇️", callback_data="0")
            ],

            [
                InlineKeyboardButton(text=f"{quyma_colatrendvich[call.message.chat.id]}", callback_data="quyma_colatrendvich"),
                InlineKeyboardButton(text="limonli choy", callback_data="limonli_choytrendvich")
            ],

            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ],

        ]
    )
    global checktrendvich
    summa = 45000 * sontrendvich['count']

    new_caption = f"""
Maxi BOX Trendvich 
Trendvich, kartoshka fri, 0,4 l coca cola, tanlash uchun sous

Maxi BOX Trendvich 45 000 x {sontrendvich['count']} = {summa}
{checktrendvich}
{ssous_checkertrendvich(call.message.chat.id)}
{psous_checkertrendvich(call.message.chat.id)}
{ketchup_checkertrendvich(call.message.chat.id)}
{quyma_cola_checkertrendvich(call.message.chat.id)}
{limonli_choy_checkertrendvich(call.message.chat.id)}
Umumiy: {summa} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/Maxiboxtrendvich.jpg', 'rb'), caption=new_caption),
        reply_markup=update_button,
        # message_id=call.message.message_id,
        # chat_id=call.message.chat.id
    )



@dp.callback_query_handler(text='limonli_choytrendvich')
async def limonlitrendvich(call: types.CallbackQuery):
    quyma_colatrendvich[call.message.chat.id] = 'quyma cola'


    if call.message.chat.id in sontrendvich.keys():

        if '✅' not in limonli_choytrendvich[call.message.chat.id]:
            limonli_choytrendvich[call.message.chat.id] = "✅limonli choy"
        else:
            limonli_choytrendvich[call.message.chat.id] = "limonli choy"

    else:
        limonli_choytrendvich[call.message.chat.id] = "✅limonli choy"

    if call.message.chat.id in sarimsoqli_soustrendvich:
        if 'sarimsoqli sous' in sarimsoqli_soustrendvich[call.message.chat.id]:
            button_text = sarimsoqli_soustrendvich[call.message.chat.id]
        else:
            button_text = "sarimsoqli sous"
    else:
        button_text = "sarimsoqli sous"

    if call.message.chat.id in pishloqli_soustrendvich:
        if 'pishloqli sous' in pishloqli_soustrendvich[call.message.chat.id]:
            p_text = pishloqli_soustrendvich[call.message.chat.id]
        else:
            p_text = "pishloqli sous"
    else:
        p_text = "pishloqli sous"

    if call.message.chat.id in ketchuptrendvich:
        if 'ketchup' in ketchuptrendvich[call.message.chat.id]:
            k_text = ketchuptrendvich[call.message.chat.id]
        else:
            k_text = "ketchup"
    else:
        k_text = "ketchup"

    if call.message.chat.id not in sontrendvich.keys():
        sontrendvich[call.message.chat.id] = "kichik kartoshka-fri"

    update_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minustrendvich"),
                InlineKeyboardButton(text=str(sontrendvich['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plustrendvich")
            ],
            [
                InlineKeyboardButton(text="⬇️ kartoshka-fri ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=sontrendvich[call.message.chat.id], callback_data="kichik_kartoshka_fritrendvich")
            ],
            [
                InlineKeyboardButton(text="⬇️ siz tanlagan sous ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=f'{button_text}', callback_data="sarimsoqli_soustrendvich"),
                InlineKeyboardButton(text=f'{p_text}', callback_data="pishloqli_soustrendvich"),
                InlineKeyboardButton(text=f'{k_text}', callback_data="ketchuptrendvich")
            ],

            [
                InlineKeyboardButton(text="⬇️ ichimlik ⬇️", callback_data="0")
            ],

            [
                InlineKeyboardButton(text=f"{quyma_colatrendvich[call.message.chat.id]}", callback_data="quyma_colatrendvich"),
                InlineKeyboardButton(text=f"{limonli_choytrendvich[call.message.chat.id]}", callback_data="limonli_choytrendvich")
            ],

            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ],

        ]
    )
    global checktrendvich
    summa = 45000 * sontrendvich['count']

    new_caption = f"""
Maxi BOX Trendvich 
Trendvich, kartoshka fri, 0,4 l coca cola, tanlash uchun sous

Maxi BOX Trendvich 45 000 x {sontrendvich['count']} = {summa}
{checktrendvich}
{ssous_checkertrendvich(call.message.chat.id)}
{psous_checkertrendvich(call.message.chat.id)}
{ketchup_checkertrendvich(call.message.chat.id)}
{quyma_cola_checkertrendvich(call.message.chat.id)}
{limonli_choy_checkertrendvich(call.message.chat.id)}
Umumiy: {summa} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/Maxiboxtrendvich.jpg', 'rb'), caption=new_caption),
        reply_markup=update_button,
        # message_id=call.message.message_id,
        # chat_id=call.message.chat.id
    )