from handlers.users.product2 import son2
from keyboards.inline.inline_buttons import Tozalash
from loader import dp
from aiogram import types
import sqlite3

connect = sqlite3.connect('C:/Users/user/PycharmProjects/MaxWAy/savat.db')

cursor = connect.cursor()

cursor.execute(
    'CREATE TABLE IF NOT EXISTS savatcha(id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, mahsulotlar TEXT)')
connect.commit()


def savat(result, result2, user_id):
    mahsulotlar = f'''
        Maxi BOX Popular: {son2.get('count')}
        Kartoshka-fri: Kichik kartoshka-fri
        Siz tanlagan sous: {result}
        Ichimlik: {result2}
    '''

    cursor.execute('INSERT INTO savatcha (user_id, mahsulotlar) VALUES (?, ?)', (user_id, mahsulotlar))
    connect.commit()

@dp.message_handler(text='📋 Mening buyurtmalarim')
async def mening_buyurtmalarim(message: types.Message):
    user_id = message.from_user.id

    cursor.execute('SELECT mahsulotlar FROM savatcha WHERE user_id = ?', (user_id,))
    buyurtmalar = cursor.fetchall()

    if buyurtmalar:
        order_list = "\n\n".join([order[0] for order in buyurtmalar])
        await message.answer(f"Sizning buyurtmalaringiz:\n\n{order_list}")
    else:
        await message.answer("Sizda buyurtmalar yo'q :")


@dp.message_handler(text='📥 Savat')
async def savat_handler(message: types.Message):
    user_id = message.from_user.id

    cursor.execute('SELECT mahsulotlar FROM savatcha WHERE user_id = ?', (user_id,))
    savat = cursor.fetchall()

    if savat:
        order_list = "\n\n".join([order[0] for order in savat])
        await message.answer(f"Sizning savatchangiz:\n\n{order_list}",reply_markup=Tozalash)
    else:
        await message.answer("Sizning savatchangiz bo'sh.",reply_markup=Tozalash)


@dp.callback_query_handler(text="tozalash")
async def tozalsh(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id

    cursor.execute('DELETE FROM savatcha WHERE user_id = ?', (user_id,))
    connect.commit()

    await callback_query.message.answer("Sizning savatchangiz tozalandi.")
    await callback_query.message.delete()

