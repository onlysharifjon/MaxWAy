from keyboards.default.menubuttons import sous
from keyboards.inline.inline_buttons import MiniBox
from loader import dp
from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

checkminibox = None
sonminibox = {
    'count': 1,
    'kichik_kartorshka_fri': "kichik kartoshka-fri",
    'fri_caption': """
kartoshka-fri :
  - kichik kartoshka-fri      0 x 1 = 0  
""",
    'sarimsoq_caption': """""",
}
fri_narxminibox = {}

ketchupminibox = {'user_id': True}
pishloqli_sousminibox = {'user_id': True}
sarimsoqli_sousminibox = {'user_id': True}
quyma_colaminibox = {'user_id':True}
limonli_choyminibox = {'user_id':True}
def ssous_checkerminibox(user_id):
    if user_id in sarimsoqli_sousminibox.keys():
        if '✅' in sarimsoqli_sousminibox[user_id]:
            return """
siz tanlagan sous :
- sarimsoqli sous      0 x 1 = 0  
    """
        else:
            return ''


def psous_checkerminibox(user_id):
    if user_id in pishloqli_sousminibox.keys():
        if '✅' in pishloqli_sousminibox[user_id]:
            return """
siz tanlagan sous :
- pishloqli sous      0 x 1 = 0  
        """
        else:
            return ''


def ketchup_checkerminibox(user_id):
    if user_id in ketchupminibox.keys():
        if '✅' in ketchupminibox[user_id]:
            return """
siz tanlagan sous :
- ketchup       0 x 1 = 0
        """
        else:
            return ''

def quyma_cola_checkerminibox(user_id):
    if user_id in quyma_colaminibox.keys():
        if '✅' in quyma_colaminibox[user_id]:
            return """
ichimlik :
  - quyma cola       0 x 1 = 0
    """
        else:
            return ''

def limonli_choy_checkerminibox(user_id):
    if user_id in limonli_choyminibox.keys():
        if '✅' in limonli_choyminibox[user_id]:
            return """
ichimlik :
  - limonli choy      0 x 1 = 0
    """
        else:
            return ''


@dp.message_handler(text="Mini BOX")
async def Mini_box(message: types.Message):
    ketchupminibox[message.from_user.id] = ''
    sarimsoqli_sousminibox[message.from_user.id] = ''
    pishloqli_sousminibox[message.from_user.id] = ''
    quyma_colaminibox[message.from_user.id] = ''
    limonli_choyminibox[message.from_user.id]=''

    await message.answer("Mahsulot miqdorini tanlang")
    await message.answer_photo(photo=open('images/Minibox.jpg', 'rb'), caption="""
Mini BOX 
Longer, kartoshka fri, coca-cola 0,3, tanlovga ko'ra sous

Mini BOX 25 000 x 1 = 25 000

Umumiy: 25 000 UZS""", reply_markup=MiniBox)


@dp.callback_query_handler(text='plusminibox')
async def plusminibox(call: types.CallbackQuery):
    if call.message.chat.id not in sonminibox.keys():
        sonminibox[call.message.chat.id] = "kichik kartoshka-fri"
    else:
        if '✅' in sonminibox[call.message.chat.id]:
            sonminibox[call.message.chat.id] = "✅kichik kartoshka-fri"
        else:
            sonminibox[call.message.chat.id] = "kichik kartoshka-fri"

    print(sonminibox)
    sonminibox['count'] += 1

    if call.message.chat.id in sarimsoqli_sousminibox:
        if 'sarimsoqli sous' in sarimsoqli_sousminibox[call.message.chat.id]:
            button_text = sarimsoqli_sousminibox[call.message.chat.id]
        else:
            button_text = "sarimsoqli sous"
    else:
        button_text = "sarimsoqli sous"

    if call.message.chat.id in pishloqli_sousminibox:
        if 'pishloqli sous' in pishloqli_sousminibox[call.message.chat.id]:
            p_text = pishloqli_sousminibox[call.message.chat.id]
        else:
            p_text = "pishloqli sous"
    else:
        p_text = "pishloqli sous"

    if call.message.chat.id in ketchupminibox:
        if 'ketchup' in ketchupminibox[call.message.chat.id]:
            k_text = ketchupminibox[call.message.chat.id]
        else:
            k_text = "ketchup"
    else:
        k_text = "ketchup"

    if call.message.chat.id in quyma_colaminibox:
        if 'quyma cola' in quyma_colaminibox[call.message.chat.id]:
            cola_text = quyma_colaminibox[call.message.chat.id]
        else:
            cola_text = "quyma cola"
    else:
        cola_text = "quyma cola"

    if call.message.chat.id in limonli_choyminibox:
        if 'limonli choy' in limonli_choyminibox[call.message.chat.id]:
            limonli_text = limonli_choyminibox[call.message.chat.id]
        else:
            limonli_text = "limonli choy"
    else:
        limonli_text = "limonli choy"

    MiniBox = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minusminibox"),
                InlineKeyboardButton(text=str(sonminibox['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plusminibox")
            ],
            [
                InlineKeyboardButton(text="⬇️ kartoshka-fri ⬇️", callback_data="0")
            ],
            {
                InlineKeyboardButton(text=sonminibox[call.message.chat.id], callback_data="kichik_kartoshka_friminibox")
            },
            [
                InlineKeyboardButton(text="⬇️ siz tanlagan sous ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=f'{button_text}', callback_data="sarimsoqli_sousminibox"),
                InlineKeyboardButton(text=f'{p_text}', callback_data="pishloqli_sousminibox"),
                InlineKeyboardButton(text=f'{k_text}', callback_data="ketchupminibox")
            ],
            [
                InlineKeyboardButton(text="⬇️ ichimlik ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=f'{cola_text}', callback_data="quyma_colaminibox"),
                InlineKeyboardButton(text=f'{limonli_text}', callback_data="limonli_choyminibox")
            ],
            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ]
        ]
    )
    if call.message.chat.id not in fri_narxminibox.keys():
        a = ''
    else:
        a = fri_narxminibox[call.message.chat.id]

    summa = 25000 * sonminibox['count']
    new_caption = f"""
Mini BOX 
Longer, kartoshka fri, coca-cola 0,3, tanlovga ko'ra sous

Mini BOX  25 000 x {sonminibox['count']} = {summa}
{a}
{ssous_checkerminibox(call.message.chat.id)}
{psous_checkerminibox(call.message.chat.id)}
{ketchup_checkerminibox(call.message.chat.id)}
{quyma_cola_checkerminibox(call.message.chat.id)}
{limonli_choy_checkerminibox(call.message.chat.id)}
Umumiy: {summa} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/Minibox.jpg', 'rb'), chat_id=call.message.chat.id,
                                    message_id=call.message.message_id, caption=new_caption
                                    ), reply_markup=MiniBox,
    )


@dp.callback_query_handler(text='minusminibox')
async def minusminibox(call: types.CallbackQuery):
    print(sonminibox)

    if sonminibox['count'] > 1:
        sonminibox['count'] -= 1

        if call.message.chat.id in sarimsoqli_sousminibox:
            if 'sarimsoqli sous' in sarimsoqli_sousminibox[call.message.chat.id]:
                button_text = sarimsoqli_sousminibox[call.message.chat.id]
            else:
                button_text = "sarimsoqli sous"
        else:
            button_text = "sarimsoqli sous"

        if call.message.chat.id in pishloqli_sousminibox:
            if 'pishloqli sous' in pishloqli_sousminibox[call.message.chat.id]:
                p_text = pishloqli_sousminibox[call.message.chat.id]
            else:
                p_text = "pishloqli sous"
        else:
            p_text = "pishloqli sous"

        if call.message.chat.id in ketchupminibox:
            if 'ketchup' in ketchupminibox[call.message.chat.id]:
                k_text = ketchupminibox[call.message.chat.id]
            else:
                k_text = "ketchup"
        else:
            k_text = "ketchup"

        if call.message.chat.id in quyma_colaminibox:
            if 'quyma cola' in quyma_colaminibox[call.message.chat.id]:
                cola_text = quyma_colaminibox[call.message.chat.id]
            else:
                cola_text = "quyma cola"
        else:
            cola_text = "quyma cola"

        if call.message.chat.id in limonli_choyminibox:
            if 'limonli choy' in limonli_choyminibox[call.message.chat.id]:
                limonli_text = limonli_choyminibox[call.message.chat.id]
            else:
                limonli_text = "limonli choy"
        else:
            limonli_text = "limonli choy"

        MiniBox = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="minusminibox"),
                    InlineKeyboardButton(text=str(sonminibox['count']), callback_data='0'),
                    InlineKeyboardButton(text='+', callback_data="plusminibox")
                ],
                [
                    InlineKeyboardButton(text="⬇️ kartoshka-fri ⬇️", callback_data="0")
                ],
                [
                    InlineKeyboardButton(text=sonminibox[call.message.chat.id], callback_data="kichik_kartoshka_friminibox")
                ],
                [
                    InlineKeyboardButton(text="⬇️ siz tanlagan sous ⬇️", callback_data="0")
                ],
                [
                    InlineKeyboardButton(text=f"""{button_text}""", callback_data="sarimsoqli_sousminibox"),
                    InlineKeyboardButton(text=f'{p_text}', callback_data="pishloqli_sousminibox"),
                    InlineKeyboardButton(text=f'{k_text}', callback_data="ketchupminibox")
                ],
                [
                    InlineKeyboardButton(text="⬇️ ichimlik ⬇️", callback_data="0")
                ],
                [
                    InlineKeyboardButton(text=f'{cola_text}', callback_data="quyma_colaminibox"),
                    InlineKeyboardButton(text=f'{limonli_text}', callback_data="limonli_choyminibox")
                ],
                [
                    InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
                ]
            ]
        )

        if call.message.chat.id not in fri_narxminibox.keys():
            a = ''
        else:
            a = fri_narxminibox[call.message.chat.id]

        summa = 25000 * sonminibox['count']
        new_caption = f"""
Mini BOX 
Longer, kartoshka fri, coca-cola 0,3, tanlovga ko'ra sous

Mini BOX 25 000 x {sonminibox['count']} = {summa}
{a}
{ssous_checkerminibox(call.message.chat.id)}
{psous_checkerminibox(call.message.chat.id)}
{ketchup_checkerminibox(call.message.chat.id)}
{quyma_cola_checkerminibox(call.message.chat.id)}
{limonli_choy_checkerminibox(call.message.chat.id)}
Umumiy: {summa} UZS"""

        await call.message.edit_media(
            media=types.InputMediaPhoto(open('images/Minibox.jpg', 'rb'), caption=new_caption),
            reply_markup=MiniBox
        )
    else:
        await call.answer("1dan kam mahsulot tanlash mumkin emas")



@dp.callback_query_handler(text='kichik_kartoshka_friminibox')
async def kichikfriminibox(call: types.CallbackQuery):
    if call.message.chat.id not in fri_narxminibox.keys():
        fri_narxminibox[call.message.chat.id] = '''
kartoshka-fri :
  - kichik kartoshka-fri      0 x 1 = 0  
        '''
    else:
        del fri_narxminibox[call.message.chat.id]
    # try:
    #     print(son[call.message.chat.id])
    # except:
    #     son[call.message.chat.id] = "✅kichik kartoshka-fri"

    if call.message.chat.id in sonminibox.keys():

        if '✅' not in sonminibox[call.message.chat.id]:
            sonminibox[call.message.chat.id] = "✅kichik kartoshka-fri"
        else:
            sonminibox[call.message.chat.id] = "kichik kartoshka-fri"

    else:
        sonminibox[call.message.chat.id] = "✅kichik kartoshka-fri"

    if call.message.chat.id in sarimsoqli_sousminibox:
        if 'sarimsoqli sous' in sarimsoqli_sousminibox[call.message.chat.id]:
            button_text = sarimsoqli_sousminibox[call.message.chat.id]
        else:
            button_text = "sarimsoqli sous"
    else:
        button_text = "sarimsoqli sous"

    if call.message.chat.id in pishloqli_sousminibox:
        if 'pishloqli sous' in pishloqli_sousminibox[call.message.chat.id]:
            p_text = pishloqli_sousminibox[call.message.chat.id]
        else:
            p_text = "pishloqli sous"
    else:
        p_text = "pishloqli sous"

    if call.message.chat.id in ketchupminibox:
        if 'ketchup' in ketchupminibox[call.message.chat.id]:
            k_text = ketchupminibox[call.message.chat.id]
        else:
            k_text = "ketchup"
    else:
        k_text = "ketchup"

    if call.message.chat.id in quyma_colaminibox:
        if 'quyma cola' in quyma_colaminibox[call.message.chat.id]:
            cola_text = quyma_colaminibox[call.message.chat.id]
        else:
            cola_text = "quyma cola"
    else:
        cola_text = "quyma cola"

    if call.message.chat.id in limonli_choyminibox:
        if 'limonli choy' in limonli_choyminibox[call.message.chat.id]:
            limonli_text = limonli_choyminibox[call.message.chat.id]
        else:
            limonli_text = "limonli choy"
    else:
        limonli_text = "limonli choy"

    update_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minusminibox"),
                InlineKeyboardButton(text=str(sonminibox['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plusminibox")
            ],
            [
                InlineKeyboardButton(text="⬇️ kartoshka-fri ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=sonminibox[call.message.chat.id], callback_data="kichik_kartoshka_friminibox")
            ],
            [
                InlineKeyboardButton(text="⬇️ siz tanlagan sous ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=f'{button_text}', callback_data="sarimsoqli_sousminibox"),
                InlineKeyboardButton(text=f'{p_text}', callback_data="pishloqli_sousminibox"),
                InlineKeyboardButton(text=f'{k_text}', callback_data="ketchupminibox")
            ],

            [
                InlineKeyboardButton(text="⬇️ ichimlik ⬇️", callback_data="0")
            ],

            [
                InlineKeyboardButton(text=f'{cola_text}', callback_data="quyma_colaminibox"),
                InlineKeyboardButton(text=f'{limonli_text}', callback_data="limonli_choyminibox")
            ],

            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ],

        ]
    )
    summa = 25000 * sonminibox['count']
    global checkminibox
    print(sonminibox[call.message.chat.id])
    if '✅' in sonminibox[call.message.chat.id]:
        checkminibox = sonminibox['fri_caption']
    else:
        checkminibox = ''

    new_caption = f"""
Mini BOX 
Longer, kartoshka fri, coca-cola 0,3, tanlovga ko'ra sous

Mini BOX 25 000 x {sonminibox['count']} = {summa}
{checkminibox}
{ssous_checkerminibox(call.message.chat.id)}
{psous_checkerminibox(call.message.chat.id)}
{ketchup_checkerminibox(call.message.chat.id)}
{quyma_cola_checkerminibox(call.message.chat.id)}
{limonli_choy_checkerminibox(call.message.chat.id)}
Umumiy: {summa} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/Minibox.jpg', 'rb'), caption=new_caption),
        reply_markup=update_button
    )
    print(sonminibox)


@dp.callback_query_handler(text='sarimsoqli_sousminibox')
async def sous1minibox(call: types.CallbackQuery):
    pishloqli_sousminibox[call.message.chat.id] = "pishloqli sous"
    ketchupminibox[call.message.chat.id] = 'ketchup'

    if call.message.chat.id in sonminibox.keys():

        if '✅' not in sarimsoqli_sousminibox[call.message.chat.id]:
            sarimsoqli_sousminibox[call.message.chat.id] = "✅sarimsoqli sous"
        else:
            sarimsoqli_sousminibox[call.message.chat.id] = "sarimsoqli sous"

    else:
        sarimsoqli_sousminibox[call.message.chat.id] = "✅sarimsoqli sous"
    if call.message.chat.id not in sonminibox.keys():
        sonminibox[call.message.chat.id] = "kichik kartoshka-fri"

    if call.message.chat.id in quyma_colaminibox:
        if 'quyma cola' in quyma_colaminibox[call.message.chat.id]:
            cola_text = quyma_colaminibox[call.message.chat.id]
        else:
            cola_text = "quyma cola"
    else:
        cola_text = "quyma cola"

    if call.message.chat.id in limonli_choyminibox:
        if 'limonli choy' in limonli_choyminibox[call.message.chat.id]:
            limonli_text = limonli_choyminibox[call.message.chat.id]
        else:
            limonli_text = "limonli choy"
    else:
        limonli_text = "limonli choy"

    update_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minusminibox"),
                InlineKeyboardButton(text=str(sonminibox['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plusminibox")
            ],
            [
                InlineKeyboardButton(text="⬇️ kartoshka-fri ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=sonminibox[call.message.chat.id], callback_data="kichik_kartoshka_friminibox")
            ],
            [
                InlineKeyboardButton(text="⬇️ siz tanlagan sous ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=f"{sarimsoqli_sousminibox[call.message.chat.id]}", callback_data="sarimsoqli_sousminibox"),
                InlineKeyboardButton(text=f"pishloqli sous", callback_data="pishloqli_sousminibox"),
                InlineKeyboardButton(text=f"ketchup", callback_data="ketchupminibox")
            ],

            [
                InlineKeyboardButton(text="⬇️ ichimlik ⬇️", callback_data="0")
            ],

            [
                InlineKeyboardButton(text=f'{cola_text}', callback_data="quyma_colaminibox"),
                InlineKeyboardButton(text=f'{limonli_text}', callback_data="limonli_choyminibox")
            ],

            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ],

        ]
    )
    global checkminibox
    summa = 25000 * sonminibox['count']
    new_caption = f"""
Mini BOX 
Longer, kartoshka fri, coca-cola 0,3, tanlovga ko'ra sous

Mini BOX 25 000 x {sonminibox['count']} = {summa}
{checkminibox}
{ssous_checkerminibox(call.message.chat.id)}
{psous_checkerminibox(call.message.chat.id)}
{ketchup_checkerminibox(call.message.chat.id)}
{quyma_cola_checkerminibox(call.message.chat.id)}
{limonli_choy_checkerminibox(call.message.chat.id)}
Umumiy: {summa} UZS"""

    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/Minibox.jpg', 'rb'), caption=new_caption),
        reply_markup=update_button,
        # message_id=call.message.message_id,
        # chat_id=call.message.chat.id
    )


@dp.callback_query_handler(text='pishloqli_sousminibox')
async def sous2minibox(call: types.CallbackQuery):
    sarimsoqli_sousminibox[call.message.chat.id] = "sarimsoqli sous"
    ketchupminibox[call.message.chat.id] = 'ketchup'

    if call.message.chat.id in sonminibox.keys():

        if '✅' not in pishloqli_sousminibox[call.message.chat.id]:
            pishloqli_sousminibox[call.message.chat.id] = "✅pishloqli sous"
        else:
            pishloqli_sousminibox[call.message.chat.id] = "pishloqli sous"

    else:
        pishloqli_sousminibox[call.message.chat.id] = "✅pishloqli sous"

    if call.message.chat.id not in sonminibox.keys():
        sonminibox[call.message.chat.id] = "kichik kartoshka-fri"

    if call.message.chat.id in quyma_colaminibox:
        if 'quyma cola' in quyma_colaminibox[call.message.chat.id]:
            cola_text = quyma_colaminibox[call.message.chat.id]
        else:
            cola_text = "quyma cola"
    else:
        cola_text = "quyma cola"

    if call.message.chat.id in limonli_choyminibox:
        if 'limonli choy' in limonli_choyminibox[call.message.chat.id]:
            limonli_text = limonli_choyminibox[call.message.chat.id]
        else:
            limonli_text = "limonli choy"
    else:
        limonli_text = "limonli choy"

    update_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minusminibox"),
                InlineKeyboardButton(text=str(sonminibox['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plusminibox")
            ],
            [
                InlineKeyboardButton(text="⬇️ kartoshka-fri ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=sonminibox[call.message.chat.id], callback_data="kichik_kartoshka_friminibox")
            ],
            [
                InlineKeyboardButton(text="⬇️ siz tanlagan sous ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=f"{sarimsoqli_sousminibox[call.message.chat.id]}", callback_data="sarimsoqli_sousminibox"),
                InlineKeyboardButton(text=f"{pishloqli_sousminibox[call.message.chat.id]}", callback_data="pishloqli_sousminibox"),
                InlineKeyboardButton(text=f"ketchup", callback_data="ketchup")
            ],

            [
                InlineKeyboardButton(text="⬇️ ichimlik ⬇️", callback_data="0")
            ],

            [
                InlineKeyboardButton(text=f'{cola_text}', callback_data="quyma_colaminibox"),
                InlineKeyboardButton(text=f'{limonli_text}', callback_data="limonli_choyminibox")
            ],

            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ],

        ]
    )
    global checkminibox
    summa = 25000 * sonminibox['count']

    new_caption = f"""
Mini BOX 
Longer, kartoshka fri, coca-cola 0,3, tanlovga ko'ra sous

Mini BOX 25 000 x {sonminibox['count']} = {summa}
{checkminibox}
{ssous_checkerminibox(call.message.chat.id)}
{psous_checkerminibox(call.message.chat.id)}
{ketchup_checkerminibox(call.message.chat.id)}
{quyma_cola_checkerminibox(call.message.chat.id)}
{limonli_choy_checkerminibox(call.message.chat.id)}
Umumiy: {summa} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/Minibox.jpg', 'rb'), caption=new_caption),
        reply_markup=update_button,
        # message_id=call.message.message_id,
        # chat_id=call.message.chat.id
    )


@dp.callback_query_handler(text='ketchupminibox')
async def sous3minibox(call: types.CallbackQuery):
    sarimsoqli_sousminibox[call.message.chat.id] = "sarimsoqli sous"
    pishloqli_sousminibox[call.message.chat.id] = 'pishloqli sous'

    if call.message.chat.id in sonminibox.keys():

        if '✅' not in ketchupminibox[call.message.chat.id]:
            ketchupminibox[call.message.chat.id] = "✅ketchup"
        else:
            ketchupminibox[call.message.chat.id] = "ketchup"

    else:
        ketchupminibox[call.message.chat.id] = "✅ketchup"

    if call.message.chat.id not in sonminibox.keys():
        sonminibox[call.message.chat.id] = "kichik kartoshka-fri"

    if call.message.chat.id in quyma_colaminibox:
        if 'quyma cola' in quyma_colaminibox[call.message.chat.id]:
            cola_text = quyma_colaminibox[call.message.chat.id]
        else:
            cola_text = "quyma cola"
    else:
        cola_text = "quyma cola"

    if call.message.chat.id in limonli_choyminibox:
        if 'limonli choy' in limonli_choyminibox[call.message.chat.id]:
            limonli_text = limonli_choyminibox[call.message.chat.id]
        else:
            limonli_text = "limonli choy"
    else:
        limonli_text = "limonli choy"

    update_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minusminibox"),
                InlineKeyboardButton(text=str(sonminibox['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plusminibox")
            ],
            [
                InlineKeyboardButton(text="⬇️ kartoshka-fri ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=sonminibox[call.message.chat.id], callback_data="kichik_kartoshka_friminibox")
            ],
            [
                InlineKeyboardButton(text="⬇️ siz tanlagan sous ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=f"{sarimsoqli_sousminibox[call.message.chat.id]}", callback_data="sarimsoqli_sousminibox"),
                InlineKeyboardButton(text=f"{pishloqli_sousminibox[call.message.chat.id]}", callback_data="pishloqli_sousminibox"),
                InlineKeyboardButton(text=f"{ketchupminibox[call.message.chat.id]}", callback_data="ketchupminibox")
            ],

            [
                InlineKeyboardButton(text="⬇️ ichimlik ⬇️", callback_data="0")
            ],

            [
                InlineKeyboardButton(text=f'{cola_text}', callback_data="quyma_colaminibox"),
                InlineKeyboardButton(text=f'{limonli_text}', callback_data="limonli_choyminibox")
            ],

            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ],

        ]
    )
    global checkminibox
    summa = 25000 * sonminibox['count']

    new_caption = f"""
Mini BOX 
Longer, kartoshka fri, coca-cola 0,3, tanlovga ko'ra sous

Mini BOX 25 000 x {sonminibox['count']} = {summa}
{checkminibox}
{ssous_checkerminibox(call.message.chat.id)}
{psous_checkerminibox(call.message.chat.id)}
{ketchup_checkerminibox(call.message.chat.id)}
{quyma_cola_checkerminibox(call.message.chat.id)}
{limonli_choy_checkerminibox(call.message.chat.id)}
Umumiy: {summa} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/Minibox.jpg', 'rb'), caption=new_caption),
        reply_markup=update_button,
        # message_id=call.message.message_id,
        # chat_id=call.message.chat.id
    )


@dp.callback_query_handler(text='quyma_colaminibox')
async def colaminibox(call: types.CallbackQuery):
    limonli_choyminibox[call.message.chat.id] = 'limonli choy'


    if call.message.chat.id in sonminibox.keys():

        if '✅' not in quyma_colaminibox[call.message.chat.id]:
            quyma_colaminibox[call.message.chat.id] = "✅quyma cola"
        else:
            quyma_colaminibox[call.message.chat.id] = "quyma cola"

    else:
        quyma_colaminibox[call.message.chat.id] = "✅quyma cola"

    if call.message.chat.id in sarimsoqli_sousminibox:
        if 'sarimsoqli sous' in sarimsoqli_sousminibox[call.message.chat.id]:
            button_text = sarimsoqli_sousminibox[call.message.chat.id]
        else:
            button_text = "sarimsoqli sous"
    else:
        button_text = "sarimsoqli sous"

    if call.message.chat.id in pishloqli_sousminibox:
        if 'pishloqli sous' in pishloqli_sousminibox[call.message.chat.id]:
            p_text = pishloqli_sousminibox[call.message.chat.id]
        else:
            p_text = "pishloqli sous"
    else:
        p_text = "pishloqli sous"

    if call.message.chat.id in ketchupminibox:
        if 'ketchup' in ketchupminibox[call.message.chat.id]:
            k_text = ketchupminibox[call.message.chat.id]
        else:
            k_text = "ketchup"
    else:
        k_text = "ketchup"

    if call.message.chat.id not in sonminibox.keys():
        sonminibox[call.message.chat.id] = "kichik kartoshka-fri"

    update_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minusminibox"),
                InlineKeyboardButton(text=str(sonminibox['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plusminibox")
            ],
            [
                InlineKeyboardButton(text="⬇️ kartoshka-fri ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=sonminibox[call.message.chat.id], callback_data="kichik_kartoshka_friminibox")
            ],
            [
                InlineKeyboardButton(text="⬇️ siz tanlagan sous ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=f'{button_text}', callback_data="sarimsoqli_sousminibox"),
                InlineKeyboardButton(text=f'{p_text}', callback_data="pishloqli_sousminibox"),
                InlineKeyboardButton(text=f'{k_text}', callback_data="ketchupminibox")
            ],

            [
                InlineKeyboardButton(text="⬇️ ichimlik ⬇️", callback_data="0")
            ],

            [
                InlineKeyboardButton(text=f"{quyma_colaminibox[call.message.chat.id]}", callback_data="quyma_colaminibox"),
                InlineKeyboardButton(text="limonli choy", callback_data="limonli_choyminibox")
            ],

            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ],

        ]
    )
    global checkminibox
    summa = 25000 * sonminibox['count']

    new_caption = f"""
Mini BOX 
Longer, kartoshka fri, coca-cola 0,3, tanlovga ko'ra sous

Mini BOX 25 000 x {sonminibox['count']} = {summa}
{checkminibox}
{ssous_checkerminibox(call.message.chat.id)}
{psous_checkerminibox(call.message.chat.id)}
{ketchup_checkerminibox(call.message.chat.id)}
{quyma_cola_checkerminibox(call.message.chat.id)}
{limonli_choy_checkerminibox(call.message.chat.id)}
Umumiy: {summa} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/Minibox.jpg', 'rb'), caption=new_caption),
        reply_markup=update_button,
        # message_id=call.message.message_id,
        # chat_id=call.message.chat.id
    )



@dp.callback_query_handler(text='limonli_choyminibox')
async def limonliminibox(call: types.CallbackQuery):
    quyma_colaminibox[call.message.chat.id] = 'quyma cola'


    if call.message.chat.id in sonminibox.keys():

        if '✅' not in limonli_choyminibox[call.message.chat.id]:
            limonli_choyminibox[call.message.chat.id] = "✅limonli choy"
        else:
            limonli_choyminibox[call.message.chat.id] = "limonli choy"

    else:
        limonli_choyminibox[call.message.chat.id] = "✅limonli choy"

    if call.message.chat.id in sarimsoqli_sousminibox:
        if 'sarimsoqli sous' in sarimsoqli_sousminibox[call.message.chat.id]:
            button_text = sarimsoqli_sousminibox[call.message.chat.id]
        else:
            button_text = "sarimsoqli sous"
    else:
        button_text = "sarimsoqli sous"

    if call.message.chat.id in pishloqli_sousminibox:
        if 'pishloqli sous' in pishloqli_sousminibox[call.message.chat.id]:
            p_text = pishloqli_sousminibox[call.message.chat.id]
        else:
            p_text = "pishloqli sous"
    else:
        p_text = "pishloqli sous"

    if call.message.chat.id in ketchupminibox:
        if 'ketchup' in ketchupminibox[call.message.chat.id]:
            k_text = ketchupminibox[call.message.chat.id]
        else:
            k_text = "ketchup"
    else:
        k_text = "ketchup"

    if call.message.chat.id not in sonminibox.keys():
        sonminibox[call.message.chat.id] = "kichik kartoshka-fri"

    update_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minusminibox"),
                InlineKeyboardButton(text=str(sonminibox['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plusminibox")
            ],
            [
                InlineKeyboardButton(text="⬇️ kartoshka-fri ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=sonminibox[call.message.chat.id], callback_data="kichik_kartoshka_friminibox")
            ],
            [
                InlineKeyboardButton(text="⬇️ siz tanlagan sous ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=f'{button_text}', callback_data="sarimsoqli_sousminibox"),
                InlineKeyboardButton(text=f'{p_text}', callback_data="pishloqli_sousminibox"),
                InlineKeyboardButton(text=f'{k_text}', callback_data="ketchupminibox")
            ],

            [
                InlineKeyboardButton(text="⬇️ ichimlik ⬇️", callback_data="0")
            ],

            [
                InlineKeyboardButton(text=f"{quyma_colaminibox[call.message.chat.id]}", callback_data="quyma_colaminibox"),
                InlineKeyboardButton(text=f"{limonli_choyminibox[call.message.chat.id]}", callback_data="limonli_choyminibox")
            ],

            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ],

        ]
    )
    global checkminibox
    summa = 25000 * sonminibox['count']

    new_caption = f"""
Mini BOX 
Longer, kartoshka fri, coca-cola 0,3, tanlovga ko'ra sous

Mini BOX 25 000 x {sonminibox['count']} = {summa}
{checkminibox}
{ssous_checkerminibox(call.message.chat.id)}
{psous_checkerminibox(call.message.chat.id)}
{ketchup_checkerminibox(call.message.chat.id)}
{quyma_cola_checkerminibox(call.message.chat.id)}
{limonli_choy_checkerminibox(call.message.chat.id)}
Umumiy: {summa} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/Minibox.jpg', 'rb'), caption=new_caption),
        reply_markup=update_button,
        # message_id=call.message.message_id,
        # chat_id=call.message.chat.id
    )