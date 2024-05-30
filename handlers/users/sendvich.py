from keyboards.default.menubuttons import sous
from keyboards.inline.inline_buttons import Klabsendvich,Sendvichoriginal,Trendvich
from loader import dp
from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

sonklab = {
    'count': 1,
}

ketchupklab = {'user_id': True}
pishloqli_sousklab = {'user_id': True}
sarimsoqli_sousklab = {'user_id': True}

def ssous_checkerklab(user_id):
    if user_id in sarimsoqli_sousklab.keys():
        if '✅' in sarimsoqli_sousklab[user_id]:
            return """
siz tanlagan sous :
- sarimsoqli sous      0 x 1 = 0  
    """
        else:
            return ''


def psous_checkerklab(user_id):
    if user_id in pishloqli_sousklab.keys():
        if '✅' in pishloqli_sousklab[user_id]:
            return """
siz tanlagan sous :
- pishloqli sous      0 x 1 = 0  
        """
        else:
            return ''


def ketchup_checkerklab(user_id):
    if user_id in ketchupklab.keys():
        if '✅' in ketchupklab[user_id]:
            return """
siz tanlagan sous :
- ketchup       0 x 1 = 0
        """
        else:
            return ''




@dp.message_handler(text="Klab sendvich")
async def Klab_sendvich(message: types.Message):
    ketchupklab[message.from_user.id] = ''
    sarimsoqli_sousklab[message.from_user.id] = ''
    pishloqli_sousklab[message.from_user.id] = ''


    await message.answer("Mahsulot miqdorini tanlang")
    await message.answer_photo(photo=open('images/klabsendvich.jpg', 'rb'), caption="""
Klab sendvich 
Original sendvich, kartoshka fri, tanlash uchun sous
 

Klab sendvich 38 000 x 1 = 38 000

Umumiy: 38 000 UZS""", reply_markup=Klabsendvich)


@dp.callback_query_handler(text='plusklab')
async def plusklab(call: types.CallbackQuery):


    print(sonklab)
    sonklab['count'] += 1

    if call.message.chat.id in sarimsoqli_sousklab:
        if 'sarimsoqli sous' in sarimsoqli_sousklab[call.message.chat.id]:
            button_text = sarimsoqli_sousklab[call.message.chat.id]
        else:
            button_text = "sarimsoqli sous"
    else:
        button_text = "sarimsoqli sous"

    if call.message.chat.id in pishloqli_sousklab:
        if 'pishloqli sous' in pishloqli_sousklab[call.message.chat.id]:
            p_text = pishloqli_sousklab[call.message.chat.id]
        else:
            p_text = "pishloqli sous"
    else:
        p_text = "pishloqli sous"

    if call.message.chat.id in ketchupklab:
        if 'ketchup' in ketchupklab[call.message.chat.id]:
            k_text = ketchupklab[call.message.chat.id]
        else:
            k_text = "ketchup"
    else:
        k_text = "ketchup"



    Klabsendvich = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minusklab"),
                InlineKeyboardButton(text=str(sonklab['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plusklab")
            ],

            [
                InlineKeyboardButton(text="⬇️ siz tanlagan sous ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=f'{button_text}', callback_data="sarimsoqli_sousklab"),
                InlineKeyboardButton(text=f'{p_text}', callback_data="pishloqli_sousklab"),
                InlineKeyboardButton(text=f'{k_text}', callback_data="ketchupklab")
            ],


            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ]
        ]
    )


    summa = 38000 * sonklab['count']
    new_caption = f"""
Klab sendvich 
Original sendvich, kartoshka fri, tanlash uchun sous

Klab sendvich 38 000 x {sonklab['count']} = {summa}

{ssous_checkerklab(call.message.chat.id)}
{psous_checkerklab(call.message.chat.id)}
{ketchup_checkerklab(call.message.chat.id)}

Umumiy: {summa} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/klabsendvich.jpg', 'rb'), chat_id=call.message.chat.id,
                                    message_id=call.message.message_id, caption=new_caption
                                    ), reply_markup=Klabsendvich,
    )


@dp.callback_query_handler(text='minusklab')
async def minusklab(call: types.CallbackQuery):
    print(sonklab)

    if sonklab['count'] > 1:
        sonklab['count'] -= 1

        if call.message.chat.id in sarimsoqli_sousklab:
            if 'sarimsoqli sous' in sarimsoqli_sousklab[call.message.chat.id]:
                button_text = sarimsoqli_sousklab[call.message.chat.id]
            else:
                button_text = "sarimsoqli sous"
        else:
            button_text = "sarimsoqli sous"

        if call.message.chat.id in pishloqli_sousklab:
            if 'pishloqli sous' in pishloqli_sousklab[call.message.chat.id]:
                p_text = pishloqli_sousklab[call.message.chat.id]
            else:
                p_text = "pishloqli sous"
        else:
            p_text = "pishloqli sous"

        if call.message.chat.id in ketchupklab:
            if 'ketchup' in ketchupklab[call.message.chat.id]:
                k_text = ketchupklab[call.message.chat.id]
            else:
                k_text = "ketchup"
        else:
            k_text = "ketchup"



        Klabsendvich= InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="minusklab"),
                    InlineKeyboardButton(text=str(sonklab['count']), callback_data='0'),
                    InlineKeyboardButton(text='+', callback_data="plusklab")
                ],

                [
                    InlineKeyboardButton(text="⬇️ siz tanlagan sous ⬇️", callback_data="0")
                ],
                [
                    InlineKeyboardButton(text=f"""{button_text}""", callback_data="sarimsoqli_sousklab"),
                    InlineKeyboardButton(text=f'{p_text}', callback_data="pishloqli_sousklab"),
                    InlineKeyboardButton(text=f'{k_text}', callback_data="ketchupklab")
                ],

                [
                    InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
                ]
            ]
        )



        summa = 38000 * sonklab['count']
        new_caption = f"""
Klab sendvich 
Original sendvich, kartoshka fri, tanlash uchun sous

Klab sendvich 38 000 x 1 x {sonklab['count']} = {summa}

{ssous_checkerklab(call.message.chat.id)}
{psous_checkerklab(call.message.chat.id)}
{ketchup_checkerklab(call.message.chat.id)}

Umumiy: {summa} UZS"""

        await call.message.edit_media(
            media=types.InputMediaPhoto(open('images/klabsendvich.jpg', 'rb'), caption=new_caption),
            reply_markup=Klabsendvich
        )
    else:
        await call.answer("1dan kam mahsulot tanlash mumkin emas")





@dp.callback_query_handler(text='sarimsoqli_sousklab')
async def sous1klab(call: types.CallbackQuery):
    pishloqli_sousklab[call.message.chat.id] = "pishloqli sous"
    ketchupklab[call.message.chat.id] = 'ketchup'

    if call.message.chat.id in sonklab.keys():

        if '✅' not in sarimsoqli_sousklab[call.message.chat.id]:
            sarimsoqli_sousklab[call.message.chat.id] = "✅sarimsoqli sous"
        else:
            sarimsoqli_sousklab[call.message.chat.id] = "sarimsoqli sous"

    else:
        sarimsoqli_sousklab[call.message.chat.id] = "✅sarimsoqli sous"




    update_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minusklab"),
                InlineKeyboardButton(text=str(sonklab['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plusklab")
            ],

            [
                InlineKeyboardButton(text="⬇️ siz tanlagan sous ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=f"{sarimsoqli_sousklab[call.message.chat.id]}", callback_data="sarimsoqli_sousklab"),
                InlineKeyboardButton(text=f"pishloqli sous", callback_data="pishloqli_sousklab"),
                InlineKeyboardButton(text=f"ketchup", callback_data="ketchupklab")
            ],


            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ],

        ]
    )

    summa = 38000 * sonklab['count']
    new_caption = f"""
Klab sendvich 
Original sendvich, kartoshka fri, tanlash uchun sous

Klab sendvich 38 000 x 1 x {sonklab['count']} = {summa}
{ssous_checkerklab(call.message.chat.id)}
{psous_checkerklab(call.message.chat.id)}
{ketchup_checkerklab(call.message.chat.id)}

Umumiy: {summa} UZS"""

    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/klabsendvich.jpg', 'rb'), caption=new_caption),
        reply_markup=update_button,

    )


@dp.callback_query_handler(text='pishloqli_sousklab')
async def sous2klab(call: types.CallbackQuery):
    sarimsoqli_sousklab[call.message.chat.id] = "sarimsoqli sous"
    ketchupklab[call.message.chat.id] = 'ketchup'

    if call.message.chat.id in sonklab.keys():

        if '✅' not in pishloqli_sousklab[call.message.chat.id]:
            pishloqli_sousklab[call.message.chat.id] = "✅pishloqli sous"
        else:
            pishloqli_sousklab[call.message.chat.id] = "pishloqli sous"

    else:
        pishloqli_sousklab[call.message.chat.id] = "✅pishloqli sous"



    update_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minusklab"),
                InlineKeyboardButton(text=str(sonklab['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plusklab")
            ],

            [
                InlineKeyboardButton(text="⬇️ siz tanlagan sous ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=f"{sarimsoqli_sousklab[call.message.chat.id]}", callback_data="sarimsoqli_sousklab"),
                InlineKeyboardButton(text=f"{pishloqli_sousklab[call.message.chat.id]}", callback_data="pishloqli_sousklab"),
                InlineKeyboardButton(text=f"ketchup", callback_data="ketchupklab")
            ],


            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ],

        ]
    )

    summa = 38000 * sonklab['count']

    new_caption = f"""
Klab sendvich 
Original sendvich, kartoshka fri, tanlash uchun sous

Klab sendvich 38 000 x 1 x {sonklab['count']} = {summa}

{ssous_checkerklab(call.message.chat.id)}
{psous_checkerklab(call.message.chat.id)}
{ketchup_checkerklab(call.message.chat.id)}

Umumiy: {summa} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/klabsendvich.jpg', 'rb'), caption=new_caption),
        reply_markup=update_button,

    )


@dp.callback_query_handler(text='ketchupklab')
async def sous3klab(call: types.CallbackQuery):
    sarimsoqli_sousklab[call.message.chat.id] = "sarimsoqli sous"
    pishloqli_sousklab[call.message.chat.id] = 'pishloqli sous'

    if call.message.chat.id in sonklab.keys():

        if '✅' not in ketchupklab[call.message.chat.id]:
            ketchupklab[call.message.chat.id] = "✅ketchup"
        else:
            ketchupklab[call.message.chat.id] = "ketchup"

    else:
        ketchupklab[call.message.chat.id] = "✅ketchup"


    update_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minusklab"),
                InlineKeyboardButton(text=str(sonklab['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plusklab")
            ],


            [
                InlineKeyboardButton(text="⬇️ siz tanlagan sous ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=f"{sarimsoqli_sousklab[call.message.chat.id]}", callback_data="sarimsoqli_sousklab"),
                InlineKeyboardButton(text=f"{pishloqli_sousklab[call.message.chat.id]}", callback_data="pishloqli_sousklab"),
                InlineKeyboardButton(text=f"{ketchupklab[call.message.chat.id]}", callback_data="ketchupklab")
            ],

            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ],

        ]
    )

    summa = 38000 * sonklab['count']

    new_caption = f"""
Klab sendvich 
Original sendvich, kartoshka fri, tanlash uchun sous

Klab sendvich 38 000 x 1 x {sonklab['count']} = {summa}

{ssous_checkerklab(call.message.chat.id)}
{psous_checkerklab(call.message.chat.id)}
{ketchup_checkerklab(call.message.chat.id)}

Umumiy: {summa} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/klabsendvich.jpg', 'rb'), caption=new_caption),
        reply_markup=update_button,

    )
#------------------------------------------------------------------------------------------------------------------------

sonoriginal = {
    'count': 1,
}
@dp.message_handler(text="Sendvich Original")
async def Sendvich_original(message: types.Message):
    await message.answer("Mahsulot miqdorini tanlang")
    await message.answer_photo(photo=open('images/senvichoriginal.jpg', 'rb'), caption="""
Sendvich Original 
Toster non, tovuq shnitseli, yangi bodring, pomidor, klab sousi, Xoxland pishloq
 

Sendvich Original 30 000 x 1 = 30 000
Umumiy: 30 000 UZS""", reply_markup=Sendvichoriginal)


@dp.callback_query_handler(text='plusoriginal')
async def plusoriginal(call: types.CallbackQuery):


    print(sonoriginal)
    sonoriginal['count'] += 1


    Sendvichoriginal = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minusoriginal"),
                InlineKeyboardButton(text=str(sonoriginal['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plusoriginal")
            ],
            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ]
        ]
    )


    summaoriginal = 30000 * sonoriginal['count']
    new_caption = f"""
Sendvich Original 
Toster non, tovuq shnitseli, yangi bodring, pomidor, klab sousi, Xoxland pishloq

Sendvich Original 30 000 x  {sonoriginal['count']} = {summaoriginal}

Umumiy: {summaoriginal} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/senvichoriginal.jpg', 'rb'), chat_id=call.message.chat.id,
                                    message_id=call.message.message_id, caption=new_caption
                                    ), reply_markup=Sendvichoriginal,
    )


@dp.callback_query_handler(text='minusoriginal')
async def minusoriginal(call: types.CallbackQuery):
    print(sonklab)

    if sonoriginal['count'] > 1:
        sonoriginal['count'] -= 1



        Sendvichoriginal= InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="minusoriginal"),
                    InlineKeyboardButton(text=str(sonoriginal['count']), callback_data='0'),
                    InlineKeyboardButton(text='+', callback_data="plusoriginal")
                ],

                [
                    InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
                ]
            ]
        )

        summaoriginal = 30000 * sonoriginal['count']
        new_caption = f"""
Sendvich Original 
Toster non, tovuq shnitseli, yangi bodring, pomidor, klab sousi, Xoxland pishloq

Sendvich Original 30 000 x  {sonoriginal['count']} = {summaoriginal}

Umumiy: {summaoriginal} UZS"""

        await call.message.edit_media(
            media=types.InputMediaPhoto(open('images/senvichoriginal.jpg', 'rb'), caption=new_caption),
            reply_markup=Sendvichoriginal
        )
    else:
        await call.answer("1dan kam mahsulot tanlash mumkin emas")



#------------------------------------------------------------------------------------------------------------------------------

sonstrendvich = {
    'count': 1,
}


@dp.message_handler(text="Trendvich")
async def trendvich(message: types.Message):
    await message.answer("Mahsulot miqdorini tanlang")
    await message.answer_photo(photo=open('images/Trendvich.jpg', 'rb'), caption="""
Trendvich

Toster bulochkasi, mayonez, aysberg salat bargi, 1 dona pomidor va tovuqli shnitsel 


Trendvich 30 000 x 1 = 30 000
Umumiy: 30 000 UZS""", reply_markup=Trendvich)


@dp.callback_query_handler(text='plusstrendvich')
async def plustrendvich(call: types.CallbackQuery):
    print(sonstrendvich)
    sonstrendvich['count'] += 1

    Trendvich = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minusstrendvich"),
                InlineKeyboardButton(text=str(sonstrendvich['count']), callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plusstrendvich")
            ],
            [
                InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
            ]
        ]
    )

    summatrendvich = 30000 * sonstrendvich['count']
    new_caption = f"""
Trendvich

Toster bulochkasi, mayonez, aysberg salat bargi, 1 dona pomidor va tovuqli shnitsel

Trendvich 30 000 x  {sonstrendvich['count']} = {summatrendvich}

Umumiy: {summatrendvich} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/Trendvich.jpg', 'rb'), chat_id=call.message.chat.id,
                                    message_id=call.message.message_id, caption=new_caption
                                    ), reply_markup=Trendvich,
    )


@dp.callback_query_handler(text='minusstrendvich')
async def minustrendvich(call: types.CallbackQuery):
    print(sonstrendvich)

    if sonstrendvich['count'] > 1:
        sonstrendvich['count'] -= 1

        Trendvich = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="minusstrendvich"),
                    InlineKeyboardButton(text=str(sonstrendvich['count']), callback_data='0'),
                    InlineKeyboardButton(text='+', callback_data="plusstrendvich")
                ],

                [
                    InlineKeyboardButton(text="📥Savatga qo'shish", callback_data="save")
                ]
            ]
        )

        summatrendvich = 30000 * sonstrendvich['count']
        new_caption = f"""
Trendvich

Toster bulochkasi, mayonez, aysberg salat bargi, 1 dona pomidor va tovuqli shnitsel

Trendvich 30 000 x  {sonstrendvich['count']} = {summatrendvich}

Umumiy: {summatrendvich} UZS"""

        await call.message.edit_media(
            media=types.InputMediaPhoto(open('images/Trendvich.jpg', 'rb'), caption=new_caption),
            reply_markup=Trendvich
        )
    else:
        await call.answer("1dan kam mahsulot tanlash mumkin emas")
