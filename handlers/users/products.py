from keyboards.default.menubuttons import sous
from keyboards.inline.inline_buttons import Maxi_BOX_Traditsiya
from loader import dp
from aiogram import types





@dp.message_handler(text="Maxi BOX Traditsiya")
async def maxi_box_traditsiya(message: types.Message):
    print(True)
    await message.answer("Mahsulot miqdorini tanlang")
    await message.answer_photo(photo=open('images/MaxiBOXTraditsiya.png', 'rb'), caption="""Maxi BOX Traditsiya
Original sendvich, kartoshka fri, 0,4 l coca cola, tanlash uchun sous

Maxi BOX Traditsiya 45 000 x 1 = 45 000

Umumiy: 45 000 UZS""",reply_markup=Maxi_BOX_Traditsiya)

