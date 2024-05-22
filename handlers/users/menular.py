from aiogram import types
from aiogram.dispatcher.filters import Text, state
from aiogram.dispatcher import FSMContext

from keyboards.default.menubuttons import buyurtma_berish, start_menu, orqaga, filiallar, buyurtmalarim, izoh, \
    joylashuv, locatsiya_ol, menu, yengilik, Maxi_box, sendvich, lavash, shaurma, burger, donar_kebab, hot_dog, gazak, \
    tamaddi, desert, ichimliklar, sous, sozlamalar
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


@dp.message_handler(text="⚙️ Sozlamalar")
async def sozlamala(message: types.Message):
    await message.answer("Sozlamani tanlang", reply_markup=sozlamalar)


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


@dp.message_handler(text="Yangilik 📣")
async def yangilik(message: types.Message):
    await message.answer(f"""Yangilik 📣
📣YANGILIK 📣

Eng zamonaviylar uchun haqiqiy trend - bu TRENDVICH 🥪

Biz uzoq vaqt davomida yangi retsept va yangi format ishlab chiqardik - va, nihoyat, qarsildoq TRENDVICH tayyor! 🔥

Sersuv pomidorlar, tovuq shintseli, pishloq, aysberg salati va maxsus “Klab” sousi qirs-qirs qiladigan non orasida 😋

Siz ham trendda bo’ling - yangi TRENDVICHni ta’tib ko’ring! 
Mahsulotni tanlang:""", reply_markup=yengilik)


@dp.message_handler(text="🍟🍔🥤BARAKALI Maxi BOX")
async def maxi_box(message: types.Message):
    await message.answer("""🍟🍔🥤BARAKALI Maxi BOX
    
  Mahsulotni tanlang:""", reply_markup=Maxi_box)
    print(True)


@dp.message_handler(text="🥪Klab-Sendvich")
async def k_sendvich(message: types.Message):
    await message.answer("""🥪Klab-Sendvich
  
Mahsulotni tanlang:""", reply_markup=sendvich)


@dp.message_handler(text="🌯Lavash")
async def lavash(message: types.Message):
    await message.answer("""🌯Lavash
🌯Lavash
Mahsulotni tanlang:""", reply_markup=lavash)


@dp.message_handler(text="🌮Shaurma")
async def Shaurma(message: types.Message):
    await message.answer("""🌮Shaurma
🌮Shaurma
Mahsulotni tanlang:""", reply_markup=shaurma)


@dp.message_handler(text="🍔Burger")
async def Burger(message: types.Message):
    await message.answer("""🍔Burger
🍔Burger
Mahsulotni tanlang:""", reply_markup=burger)


@dp.message_handler(text="🍱Donar kebab")
async def Donar_kebab(message: types.Message):
    await message.answer("""🍱Donar kebab
🍱Donar kebab
Mahsulotni tanlang:""", reply_markup=donar_kebab)


@dp.message_handler(text="🌭Hot-Dog")
async def Hot_dog(message: types.Message):
    await message.answer("""🌭Hot-Dog
🌭Hot-Dog
Mahsulotni tanlang:""", reply_markup=hot_dog)


@dp.message_handler(text="🍟Gazaklar")
async def Gazak(message: types.Message):
    await message.answer("""🍟Gazaklar
🍟Gazaklar
Mahsulotni tanlang:""", reply_markup=gazak)


@dp.message_handler(text="🍚Tamaddilar")
async def Tamaddi(message: types.Message):
    await message.answer("""🍚Tamaddilar
🍚Tamaddilar
Mahsulotni tanlang:""", reply_markup=tamaddi)


@dp.message_handler(text="🍰Desertlar")
async def Desert(message: types.Message):
    await message.answer("""🍰Desertlar
🍰Desertlar
Mahsulotni tanlang:""", reply_markup=desert)


@dp.message_handler(text="🥤Ichimliklar")
async def Ichimliklar(message: types.Message):
    await message.answer("""🥤Ichimliklar
🥤Ichimliklar
Mahsulotni tanlang:""", reply_markup=ichimliklar)


@dp.message_handler(text="🥫Souslar")
async def souslar(message: types.Message):
    await message.answer("""🥫Souslar
🥫Souslar
Mahsulotni tanlang:""", reply_markup=sous)


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
