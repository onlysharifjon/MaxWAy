from keyboards.default.menubuttons import sous
from keyboards.inline.inline_buttons import Maxi_BOX_Traditsiya
from loader import dp
from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

son = {
    'count': 1,
    'kichik_kartorshka_fri': "Kichik kartoshka-fri",
    'fri_caption': """"""
}


@dp.message_handler(text="Maxi BOX Traditsiya")
async def maxi_box_traditsiya(message: types.Message):
    await message.answer("Mahsulot miqdorini tanlang")
    await message.answer_photo(photo=open('images/MaxiBOXTraditsiya.png', 'rb'), caption="""Maxi BOX Traditsiya
Original sendvich, kartoshka fri, 0,4 l coca cola, tanlash uchun sous

Maxi BOX Traditsiya 45 000 x 1 = 45 000

Umumiy: 45 000 UZS""", reply_markup=Maxi_BOX_Traditsiya)


@dp.callback_query_handler(text='plus')
async def plusmaxibox(call: types.CallbackQuery):
    print(son)
    son['count'] += 1
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
                InlineKeyboardButton(text=son['kichik_kartorshka_fri'], callback_data="kichik_kartoshka_fri")
            ],
            [
                InlineKeyboardButton(text="⬇️ Siz tanlagan sous ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text="Sarimsoqli sous", callback_data="sarimsoqli_sous"),
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

    summa = 45000 * son['count']
    new_caption = f"""Maxi BOX Traditsiya
Original sendvich, kartoshka fri, 0.4L coca cola, tanlash uchun sous

Maxi BOX Traditsiya 45 000 x {son['count']} = {summa}
{son['fri_caption']}
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
                        InlineKeyboardButton(text=son['kichik_kartorshka_fri'], callback_data="kichik_kartoshka_fri")
                    ],
                    [
                        InlineKeyboardButton(text="⬇️ Siz tanlagan sous ⬇️", callback_data="0")
                    ],
                    [
                        InlineKeyboardButton(text="Sarimsoqli sous", callback_data="sarimsoqli_sous"),
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

            summa = 45000 * son['count']
            new_caption = f"""Maxi BOX Traditsiya
Original sendvich, kartoshka fri, 0.4L coca cola, tanlash uchun sous

Maxi BOX Traditsiya 45 000 x {son['count']} = {summa}
{son['fri_caption']}
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
    son['kichik_kartorshka_fri'] = "✅kichik kartoshka-fri"
    update_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="minus"),
                InlineKeyboardButton(text='1', callback_data='0'),
                InlineKeyboardButton(text='+', callback_data="plus")
            ],
            [
                InlineKeyboardButton(text="⬇️ kartoshka-fri ⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text=son['kichik_kartorshka_fri'], callback_data="kichik_kartoshka_fri")
            ],
            [
                InlineKeyboardButton(text="⬇️siz tanlagan sous⬇️", callback_data="0")
            ],
            [
                InlineKeyboardButton(text="sarimsoqli sous", callback_data="sarimsoqli_sous"),
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
    son['fri_caption'] = """
kartoshka-fri :
  - kichik kartoshka-fri      0 x 1 = 0    
    """
    new_caption = f"""Maxi BOX Traditsiya
    Original sendvich, kartoshka fri, 0.4L coca cola, tanlash uchun sous

    Maxi BOX Traditsiya 45 000 x {son['count']} = {summa}
    {son['fri_caption']}
    Umumiy: {summa} UZS"""
    await call.message.edit_media(
        media=types.InputMediaPhoto(open('images/MaxiBOXTraditsiya.png', 'rb'), caption=new_caption),
        reply_markup=update_button
    )
