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

buyurtma_berish= ReplyKeyboardMarkup(
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


filiallar= ReplyKeyboardMarkup(
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


locatsiya_ol= ReplyKeyboardMarkup(
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


menu= ReplyKeyboardMarkup(
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
