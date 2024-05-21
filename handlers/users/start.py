from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.menubuttons import start_menu
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(
        """Buyurtma berishni boshlash uchun 🛍 Buyurtma berish tugmasini bosing

Shuningdek, aksiyalarni ko'rishingiz va bizning filiallar bilan tanishishingiz mumkin: 

<a href = "https://maxway.uz/uz">menu</a>

""",
        reply_markup=start_menu,

    )

