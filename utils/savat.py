# from handlers.users.product2 import son2
# from loader import dp
# from aiogram import types
# import sqlite3
#
# connect = sqlite3.connect('savat.db')
#
# cursor = connect.cursor()
#
# cursor.execute(
#     'CREATE TABLE IF NOT EXISTS savatcha(id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, mahsulotlar TEXT)')
# connect.commit()
#
#
#
# def tester(result, result2,user_id):
#
#     mahsulotlar = f'''
#         Maxi BOX Popular: {son2.get('count')}
#         Kartoshka-fri: Kichik kartoshka-fri
#         Siz tanlagan sous: {result}
#         Ichimlik: {result2}
#     '''
#
#     cursor.execute('INSERT INTO savatcha (user_id, mahsulotlar) VALUES (?, ?)', (user_id, mahsulotlar))
#     connect.commit()
