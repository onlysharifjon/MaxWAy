from aiogram import types
from aiogram.dispatcher.filters import Text, state
from aiogram.dispatcher import FSMContext

from keyboards.default.menubuttons import buyurtma_berish, start_menu, orqaga, filiallar, buyurtmalarim, izoh, \
    joylashuv, locatsiya_ol, menu
from loader import dp
from states.states import Bolimlar


@dp.message_handler(text="🛍 Buyurtma berish")
async def handle_buyurtma_berish(message: types.Message):
    await message.answer("Yetkazib berish turini tanlang", reply_markup=buyurtma_berish)


@dp.message_handler(text='🎉 Aksiya')
async def handle_aksiya(message: types.Message):
    await message.answer_photo(open(f'images/aksiya.jpg', 'rb'), caption=f"""BEPUL YETKAZIB BERAMIZ 🚚 
 3ta Maxi Box yoki ko’proq buyurtma qiling va bepul yetkazib berish xizmatiga ega bo’ling!😋""",
                               reply_markup=orqaga)


@dp.message_handler(text='🏘 Barcha filiallar')
async def handle_filiallar(message: types.Message):
    await message.answer("Bizning filiallarimiz :", reply_markup=filiallar)


@dp.message_handler(text='📋 Mening buyurtmalarim')
async def handle_buyrtmalar(message: types.Message):
    await message.answer("Sizda buyurtmalar yo'q :", reply_markup=buyurtmalarim)


@dp.message_handler(text='✍️Izoh qoldirish')
async def handle_izoh(message: types.Message):
    await message.answer("Izoh qoldiring. Sizning fikringiz biz uchun muhim", reply_markup=izoh)
    await Bolimlar.izoh.set()


@dp.message_handler(state=Bolimlar.izoh)
async def handle_user_izoh(message: types.Message, state: FSMContext):
    await message.answer("✅ Izohingiz qabul qilindi")

    await message.answer(
        """Buyurtma berishni boshlash uchun 🛍 Buyurtma berish tugmasini bosing

Shuningdek, aksiyalarni ko'rishingiz va bizning filiallar bilan tanishishingiz mumkin: 

<a href = "https://maxway.uz/uz">menu</a>

""",
        reply_markup=start_menu,

    )
    await state.finish()


@dp.message_handler(text='ℹ️ Biz haqimizda')
async def handle_biz(message: types.Message):
    await message.answer_photo(open(f'images/biz_haqimizda.jpg', 'rb'), caption=f"""🍟 Max Way \n 
☎️ Aloqa markazi: +998712005400""",
                               reply_markup=orqaga)


@dp.message_handler(text='🚖 Yetkazib berish')
async def yetkazish(message: types.Message):
    await message.answer("Buyurtmani davom ettirish uchun iltimos lokatsiyangizni yuboring", reply_markup=joylashuv)
    # await message.answer("Locatsiya qabul qilindi", reply_markup=locatsiya_ol)
    # Original line causing the warning
    await Bolimlar.location_state.set()


@dp.message_handler(content_types=types.ContentTypes.LOCATION, state=Bolimlar.location_state)
async def locator(message: types.Message, state: FSMContext):
    await message.answer("Locatsiya qabul qilindi", reply_markup=locatsiya_ol)
    await state.finish()


@dp.message_handler(text="✅Tasdiqlash")
async def tasdiqlash(message: types.Message):
    await message.answer("Kategoriyani tanlang", reply_markup=menu)


@dp.message_handler(text='🗂 | Asosiy menu')
async def handle_asosiy_menu(message: types.Message):
    await message.answer(
        """Buyurtma berishni boshlash uchun 🛍 Buyurtma berish tugmasini bosing

Shuningdek, aksiyalarni ko'rishingiz va bizning filiallar bilan tanishishingiz mumkin: 

<a href = "https://maxway.uz/uz">menu</a>

""",
        reply_markup=start_menu,

    )


@dp.message_handler(text='⬅️ Orqaga')
async def handle_orqaga(message: types.Message):
    await message.answer(
        """Buyurtma berishni boshlash uchun 🛍 Buyurtma berish tugmasini bosing

Shuningdek, aksiyalarni ko'rishingiz va bizning filiallar bilan tanishishingiz mumkin: 

<a href = "https://maxway.uz/uz">menu</a>

""",
        reply_markup=start_menu,

    )
