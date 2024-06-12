from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🛍 Buyurtma berish')
        ],
        [
            KeyboardButton(text='🎉 Aksiya'),
            KeyboardButton(text='🏘 Barcha filiallar')
        ],
        [
            KeyboardButton(text='📋 Mening buyurtmalarim'),
            KeyboardButton(text='✍️Izoh qoldirish')
        ],
        [
            KeyboardButton("💼 Vakansiyalar"),
            KeyboardButton('ℹ️ Biz haqimizda')
        ],

        [
            KeyboardButton('⚙️ Sozlamalar')
        ],

    ],
    resize_keyboard=True
)

buyurtma_berish = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("🚖 Yetkazib berish"),
            KeyboardButton("🏃 Olib ketish")
        ],

        [
            KeyboardButton("⬅️ Orqaga"),
        ],
    ],
    resize_keyboard=True
)
orqaga = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("⬅️ Orqaga"),
        ]
    ],
    resize_keyboard=True
)

filiallar = ReplyKeyboardMarkup(
    keyboard=[

        [
            KeyboardButton(text='⬅️ Orqaga'),
            KeyboardButton(text='▶️ Oldinga')
        ],
        [
            KeyboardButton(text='MAX WAY UNIVERSAM'),
            KeyboardButton(text='MAX WAY ATLAS')
        ],
        [
            KeyboardButton("MAX WAY - DRUJBA"),
            KeyboardButton('MAX WAY MEGA PLANET')
        ],

        [
            KeyboardButton("MAX WAY AVIASOZLAR"),
            KeyboardButton('MAX WAY RISOVIY')
        ],

        [
            KeyboardButton("MAX WAY PARUS"),
            KeyboardButton('MAX WAY MAGIC CITY')
        ],

        [
            KeyboardButton("MAX WAY SAMARQAND DARVOZA"),
            KeyboardButton('MAX WAY MAGIC PARKENT')
        ],

    ],
    resize_keyboard=True
)

buyurtmalarim = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("🗂 | Asosiy menu"),
        ]
    ],
    resize_keyboard=True
)

izoh = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("⬅️ Orqaga"),
        ]
    ],
    resize_keyboard=True
)

joylashuv = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Lokatsiya yuborish', request_location=True)
        ],
        [
            KeyboardButton("⬅️ Orqaga"),
        ]

    ],
    resize_keyboard=True
)

locatsiya_ol = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Locatsiyani qayta yuborish"),
            KeyboardButton("✅Tasdiqlash")
        ],

        [
            KeyboardButton("Mening manzillarimga qo'shish"),
            KeyboardButton("⬅️ Orqaga")
        ],

    ],
    resize_keyboard=True
)

sozlamalar = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Tilni o'zgartirish"),
            KeyboardButton("Tug'ilgan kunni qo'shish")
        ],
        [
            KeyboardButton("Telefon raqamni o'zgartirish"),
            KeyboardButton("⬅️ Orqaga")
        ]
    ],
    resize_keyboard=True
)

menu = ReplyKeyboardMarkup(
    keyboard=[

        [
            KeyboardButton(text='Interaktiv menu')
        ],
        [
            KeyboardButton(text='⬅️ Orqaga'),
            KeyboardButton(text='📥 Savat')
        ],
        [
            KeyboardButton("Yangilik 📣"),
            KeyboardButton('🍟🍔🥤BARAKALI Maxi BOX')
        ],

        [
            KeyboardButton("🥪Klab-Sendvich"),
            KeyboardButton('🌯Lavash')
        ],

        [
            KeyboardButton("🌮Shaurma"),
            KeyboardButton('🍔Burger')
        ],

        [
            KeyboardButton("🍱Donar kebab"),
            KeyboardButton('🌭Hot-Dog')
        ],

        [
            KeyboardButton("🍟Gazaklar"),
            KeyboardButton('🍚Tamaddilar')
        ],

        [
            KeyboardButton("🍰Desertlar"),
            KeyboardButton('🥤Ichimliklar')
        ],

        [
            KeyboardButton(text='🥫Souslar')
        ],

    ],
    resize_keyboard=True
)

yengilik = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='⬅️ Orqaga'),
            KeyboardButton(text='📥 Savat')
        ],

        [
            KeyboardButton("Trendvich"),
            KeyboardButton("Maxi BOX Trendvich")
        ],

    ],
    resize_keyboard=True
)

Maxi_box = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='⬅️ Orqaga'),
            KeyboardButton(text='📥 Savat')
        ],

        [
            KeyboardButton("Maxi BOX Traditsiya"),
            KeyboardButton("Maxi BOX Popular")
        ],

        [
            KeyboardButton("Maxi BOX Retro"),
            KeyboardButton("Max BOX German")
        ],

        [
            KeyboardButton("Maxi BOX Trend"),
            KeyboardButton("Mini BOX")
        ],

        [
            KeyboardButton("Maxi BOX Trendvich"),
        ],

    ],
    resize_keyboard=True
)

sendvich = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='⬅️ Orqaga'),
            KeyboardButton(text='📥 Savat')
        ],

        [
            KeyboardButton("Klab sendvich"),
            KeyboardButton("Sendvich Original")
        ],

        [
            KeyboardButton("Trendvich"),
        ],

    ],
    resize_keyboard=True
)

lavash = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='⬅️ Orqaga'),
            KeyboardButton(text='📥 Savat')
        ],

        [
            KeyboardButton("Lavash standart klassik"),
            KeyboardButton("Lavash standart pishloqli")
        ],

        [
            KeyboardButton("Lavash standart achchiq"),
            KeyboardButton("Lavash mini klassik")
        ],

        [
            KeyboardButton("Lavash mini pishloqli"),
        ],

    ],
    resize_keyboard=True
)

shaurma = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='⬅️ Orqaga'),
            KeyboardButton(text='📥 Savat')
        ],

        [
            KeyboardButton("German Donar"),
            KeyboardButton("Shaurma")
        ],
        [
            KeyboardButton("Shaurma pishloqli"),
        ],

    ],
    resize_keyboard=True
)

burger = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='⬅️ Orqaga'),
            KeyboardButton(text='📥 Savat')
        ],

        [
            KeyboardButton("Gamburger"),
            KeyboardButton("Chizburger")
        ],
        [
            KeyboardButton("Bigburger"),
        ],

    ],
    resize_keyboard=True
)

donar_kebab = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='⬅️ Orqaga'),
            KeyboardButton(text='📥 Savat')
        ],

        [
            KeyboardButton("Donar kebab"),
            KeyboardButton("Donar Box")
        ],
        [
            KeyboardButton("Non"),
        ],

    ],
    resize_keyboard=True
)

hot_dog = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='⬅️ Orqaga'),
            KeyboardButton(text='📥 Savat')
        ],

        [
            KeyboardButton("Hot Dog"),
            KeyboardButton("Chiz dog")
        ],
        [
            KeyboardButton("Longer"),
        ],

    ],
    resize_keyboard=True
)

gazak = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='⬅️ Orqaga'),
            KeyboardButton(text='📥 Savat')
        ],

        [
            KeyboardButton("Kartoshka fri katta"),
            KeyboardButton("Kartoshka fri  standart")
        ],

        [
            KeyboardButton("Kartoshka fri  mini"),
            KeyboardButton("Po derevenski")
        ],

        [
            KeyboardButton("Naggets BOX"),
            KeyboardButton("Mix Box")
        ],

    ],
    resize_keyboard=True
)

tamaddi = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='⬅️ Orqaga'),
            KeyboardButton(text='📥 Savat')
        ],

        [
            KeyboardButton("Guruch"),
            KeyboardButton("Salat")
        ],

    ],
    resize_keyboard=True
)

desert = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='⬅️ Orqaga'),
            KeyboardButton(text='📥 Savat')
        ],

        [
            KeyboardButton("Tiramisu"),
            KeyboardButton("Brauni")
        ],

        [
            KeyboardButton("San-sebastian"),
            KeyboardButton("Yo'ng'oqli donat")
        ],
        [
            KeyboardButton("Karamel donat"),
            KeyboardButton("Qulupnayli donat")
        ],

    ],
    resize_keyboard=True
)

ichimliklar = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='⬅️ Orqaga'),
            KeyboardButton(text='📥 Savat')
        ],

        [
            KeyboardButton("Moxito"),
            KeyboardButton("Ice Tea")
        ],

        [
            KeyboardButton("Coca Cola"),
            KeyboardButton("Coca Cola (quyma)")
        ],
        [
            KeyboardButton("Fanta"),
            KeyboardButton("Sharbat Dena")
        ],

        [
            KeyboardButton("Fuse Tea"),
            KeyboardButton("Bonaqua")
        ],

        [
            KeyboardButton("Bir martali stakan"),
            KeyboardButton("Qora choy")
        ],

        [
            KeyboardButton("Ko'k choy"),
            KeyboardButton("Limonli choy")
        ],

        [
            KeyboardButton("Amerikano"),
            KeyboardButton("Kapuchino")
        ],

        [
            KeyboardButton("Latte"),
        ],

    ],
    resize_keyboard=True
)

sous = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='⬅️ Orqaga'),
            KeyboardButton(text='📥 Savat')
        ],

        [
            KeyboardButton("Ketchup"),
            KeyboardButton("Pishloqli sous")
        ],

        [
            KeyboardButton("Sarimsoqli sous"),
            KeyboardButton("Xalapeno")
        ],
        [
            KeyboardButton("Shirin va nordon sous")
        ]

    ],
    resize_keyboard=True
)


Savat = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='⬅️ Orqaga'),
            KeyboardButton(text='📥 Savat')
        ],

    ],
    resize_keyboard=True
)