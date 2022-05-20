import logging
import pymongo
from aiogram import Bot, Dispatcher, executor, types
import random
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import time
from datetime import datetime, timedelta
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils.exceptions import Throttled
import psycopg2
import urllib.parse as up
import os
from datetime import datetime, timedelta
from asyncio import sleep
from aiogram.dispatcher.filters.filters import BoundFilter, Filter
from aiogram.dispatcher import DEFAULT_RATE_LIMIT
from aiogram.dispatcher.handler import CancelHandler, current_handler
from psycopg2.extensions import AsIs
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.utils.exceptions import Throttled
from dotenv import load_dotenv
from aiogram.utils.markdown import *
load_dotenv()
global xxc
global zxc
zxc = os.getenv("API_TOKEN")
print(zxc)
xxc = os.getenv("DATABASE_URL")
logging.basicConfig(level=logging.INFO)
bot = Bot(token=zxc)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

up.uses_netloc.append("postgres")
url = up.urlparse(xxc)
conn = psycopg2.connect(database=url.path[1:],
                        user=url.username,
                        password=url.password,
                        host=url.hostname,
                        port=url.port
                        )
cursor = conn.cursor()

async def anti_flood(*args, **kwargs):
    m = args[0]
    await m.reply("Не спам хуйло. А точніше почекай 10 сек")
@dp.message_handler(commands=['xc'])
async def enable(message: types.Message):
    print(xxc)


@dp.message_handler(commands=['beb'])
async def add_money(message: types.Message):
    usrid = message.from_user.id
    name = message.from_user.first_name
    nameuser = message.from_user.username
    cursor.execute("SELECT date_game FROM mone_game WHERE user_id = %s", [usrid])
    resultgamedate = cursor.fetchone()
    g = [0, 1, 2, 3, 1, 2, 3]
    l = ''
    resultdate = datetime.now().replace(hour = 0, minute= 0,second=0, microsecond=0)
    v = ''
    add_bebra = random.choice(g)
    cursor.execute('SELECT money_quantity FROM mone_game WHERE user_id = %s',(usrid, ))
    result_money = cursor.fetchone()
    if random.randint(0,100) < 8:
        add_bebra = add_bebra + 10
    try:
        for gamedate in resultgamedate:
            if add_bebra == 1:
                v = 'бебрy.'
            else:
                v = 'бебр.'
            if resultdate == gamedate:
                await message.reply("🏪🏪🏪 Ви вже отримали свої бебри на сьогодні, зверніться завтра")
            else:
                cursor.execute('INSERT into mone_game (user_id, name, nameuser, money_quantity, date_game) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (user_id) DO UPDATE SET (money_quantity, date_game) = (mone_game.money_quantity + %s, %s) WHERE mone_game.user_id = %s  ;', (usrid, name, nameuser, add_bebra, resultdate, add_bebra, resultdate, usrid ))
                conn.commit()
                cursor.execute('SELECT money_quantity FROM mone_game WHERE user_id = %s', (usrid, ))
                result_money = cursor.fetchone()
                for money in result_money:
                    if money == 1:
                        l = 'бебра.'
                    elif money <= 4:
                        l = 'бебри.'
                    else:
                        l = 'бебр.'
                    if add_bebra == 0:
                        await message.reply( "🏪⛓ Вітаємо вас в Бебробанкі! Ви нічим не прислужилися альянсу. Бебробанк вам нічого платити не буде. На вашому рахунку " + str(money) + ' '+ str(l) + " Повертайтесь завтра!")
                    elif add_bebra > 3:
                        await message.reply("🏪 🆘🆘🆘 Вітаємо вас в Бебробанкі! Вам сьогодні щастить! Ви отримуєте виплату в "   + str(add_bebra) +' ' + str(v) +' Тепер на вашому рахунку ' + str(money) + ' ' + str(l)+ " До завтра!")
                    else:
                        await message.reply("🏪 Вітаємо вас в Бебробанкі! У вас на " + str(add_bebra) + ' більше ' + ' '+ str(v) +' Тепер на вашому рахунку ' + str(money) + ' '+ str(l) + ' До завтра!')
    except:
        cursor.execute('INSERT into mone_game (user_id, name, nameuser, money_quantity, date_game) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (user_id) DO UPDATE SET (money_quantity, date_game) = (mone_game.money_quantity + %s, %s) WHERE mone_game.user_id = %s  ;', (usrid, name, nameuser, add_bebra, resultdate, add_bebra, resultdate, usrid ))
        conn.commit()
        cursor.execute('SELECT money_quantity FROM mone_game WHERE user_id = %s', (usrid, ))
        result_money = cursor.fetchone()
        for money in result_money:
            if money == 1:
                l = 'бебра.'
            elif money <= 4:
                l = 'бебри.'
            else:
                l = 'бебр.'
            if add_bebra == 1:
                v = 'бебрy.'
            else:
                v = 'бебр.'
            if add_bebra == 0:
                await message.reply( "🏪⛓ Вітаємо вас в Бебробанкі! Ви нічим не прислужилися альянсу. Бебробанк вам нічого платити не буде. На вашому рахунку " + str(money) + ' '+ str(l) + " Повертайтесь завтра!")
            elif add_bebra > 3:
                await message.reply("🏪 🆘🆘🆘 Вітаємо вас в Бебробанкі! Вам сьогодні щастить! Ви отримуєте виплату в "   + str(add_bebra) +' ' + str(v) +'. Тепер на вашому рахунку ' + str(money) + ' ' + str(l)+ " До завтра!")
            else:
                await message.reply("🏪 Вітаємо вас в Бебробанкі! У вас на " + str(add_bebra) + ' більше ' + ' '+ str(v) +' Тепер на вашому рахунку ' + str(money) + ' '+ str(l) + ' До завтра!')
        
        
        
@dp.message_handler(commands=['bebry'])
async def add_mone(message: types.Message):
    usrid = message.from_user.id
    name = message.from_user.first_name
    nameuser = message.from_user.username
    
    try:
        cursor.execute('SELECT money_quantity FROM mone_game WHERE user_id = %s', (usrid,))
        result_money = cursor.fetchone()
        l = ''
        for money in result_money:
            if money == 1:
                l = 'бебра.'
            elif money <= 4:
                l = 'бебри.'
            else:
                l = 'бебр.'

            await message.reply("🏪🏪🏪 Вітаємо вас в Бебробанкі! На вашому рахунку " + str(money) + ' ' + str(l))
    except TypeError:
        await message.reply('Ти не в грі, пропиши /beb')


@dp.message_handler(commands=['top_bebr'])
async def top_money(message: types.Message):
    usrid = message.from_user.id
    name = message.from_user.first_name
    nameuser = message.from_user.username
    baa = ['Багачі Бебробанку:\n']
    cursor.execute('SELECT name, money_quantity FROM mone_game ORDER BY money_quantity DESC LIMIT 15')
    result_money = cursor.fetchall()
    n = 1
    for money in result_money:
        bal = (str(n) + ' - ' + str(money[0]) + " має " + str(money[1]) + ' бебр.')
        baa.append(bal)
        n += 1
    await message.reply('\n'.join(baa))
    

@dp.message_handler(regexp=r"базик збір")
async def top(message: types.Message):
    usrid = message.from_user.id
    chat_id = message.chat.id
    cursor.execute("SELECT usr_id FROM whitelist WHERE usr_id = %s", (usrid,))
    user = cursor.fetchone()
    try:
        for us in user:
            if usrid == us:
                x = await bot.get_chat_member(chat_id=chat_id)
                print(x)
    except:
        None


@dp.message_handler(regexp=r"базик дупа|базик срака")
@dp.throttled(anti_flood, rate=10)
async def send(message: types.Message):
    up.uses_netloc.append("postgres")
    url = up.urlparse(xxc)
    cursor.execute('SELECT photka FROM zhopu ORDER BY random() LIMIT 1')
    result_photo = cursor.fetchone()
    usrid = message.from_user.id
    
    await message.reply('Пару секунд')
    await sleep(3)
    cursor.execute("SELECT usr_id FROM whitelist WHERE usr_id = %s", (usrid,))
    idq = cursor.fetchone()
    global q 
    q = 15

    try:
        for idqі in idq:
            print(str(usrid) + ' ' + str(idqі))
            if usrid == int(idqі):
                q += 100
                print('ok')
    except:
        print('cock')
    if random.randint(0, 100) < q:
        print('кинув: ' + result_photo[0])
        await message.reply_photo(photo=result_photo[0], protect_content=True)
    else:
        await message.reply('А знаєш, пішов ти нахуй')
    


@dp.message_handler(regexp=r"базик оплачена срака|базик оплачена дупа")
@dp.throttled(anti_flood, rate=10)
async def send(message: types.Message):
    cursor.execute('SELECT photka FROM zhopu ORDER BY random() LIMIT 1')
    result_photo = cursor.fetchone()
    usrid = message.from_user.id
    
    await message.reply('Пару секунд')
    await sleep(3)
    cursor.execute("SELECT usr_id FROM whitelist WHERE usr_id = %s", (usrid,))
    idq = cursor.fetchone()
    global q
    q = 40

    try:
        for idqі in idq:
            print(usrid + ' ' + idqі)
            if usrid == int(idqі):
                q += 100
                await message.reply('Дебіл ти в вайтлісті. Але якшо ти так хочеш потратити бебри, то прошу')
                print('ok')

    except:
        None
    cursor.execute("SELECT money_quantity FROM mone_game WHERE user_id = %s", (usrid,))
    fromUSR = cursor.fetchone()    
    for fr in fromUSR:
        if fr[0] < 5:
            await message.reply('Треба мати на рахунку 5 бебр. У вас їх менше.')
        else:
            xs = fr[0] - 5
            cursor.execute("UPDATE mone_game SET money_quantity = %s WHERE user_id = %s;", (xs, usrid,))
            conn.commit()
            await message.reply('Cплачено 5 бебр')
            print('кинув: ' + result_photo[0])
            await message.reply_photo(photo=result_photo[0], protect_content=True)
    

@dp.callback_query_handler(text='btn1')
async def redact(call: types.CallbackQuery):
    callid = call.from_user.id
    if usrid == callid:
        result_money = cursor.execute("SELECT money_quantity from mone_game WHERE user_id = %s;", (callid,))
        result_money = cursor.fetchone()
        vb = random.randint(5, 10)
        try:
            for money in result_money:
                if money < 5:
                    await call.message.edit_text('Бомжам в БеброКазино не раді. На вихід.')
                    return
                else:
                    await bot.answer_callback_query(call.id)
                    await call.message.edit_text('Поставлено 5 бебр')
                    await sleep(4)
                    if random.randint(1, 100) < 50:

                        vg = money + vb
                        cursor.execute("UPDATE mone_game SET money_quantity = %s WHERE user_id = %s;", (vg, callid,))
                        conn.commit()
                        await call.message.edit_text('Тобі щастить випав Червоний🔴. Начислено +' + str(vb) + ' бебр')
                    else:
                        vs = money - 5
                        cursor.execute("UPDATE mone_game SET money_quantity = %s WHERE user_id = %s;", (vs, callid,))
                        conn.commit()
                        await call.message.edit_text('Тобі не пощастило випав Чорний⚫. Чекаємо через 6 годин')
        except TypeError:
            await call.message.edit_text("Ви не в грі пропишіть '/beb'. І спробуйте щастя через 6 годин")                
    else:
        await call.answer('Не ти викликав БеброКазино, на вихід', show_alert=True)
    
        


@dp.callback_query_handler(text='btn2')
async def redct(call: types.CallbackQuery):
    callid = call.from_user.id
    if usrid == callid:
        cursor.execute("SELECT money_quantity from mone_game WHERE user_id = %s;", (callid,))
        result_money = cursor.fetchone()
        await bot.answer_callback_query(call.id)

        vb = random.randint(5, 10)
        try:
            for money in result_money:
                if money < 5:
                    await call.message.edit_text('Бомжам в БеброКазино не раді. На вихід.')
                    return
                else:
                    await call.message.edit_text('Поставлено 5 бебр')
                    await sleep(4)
                    if random.randint(1, 100) < 50:

                        vg = money + vb
                        cursor.execute("UPDATE mone_game SET money_quantity = %s WHERE user_id = %s;", (vg, callid,))
                        conn.commit()
                        await call.message.edit_text('Тобі щастить випав Чорний⚫️. Начислено +' + str(vb) + ' бебр')
                    else:

                        vs = money - 5
                        cursor.execute("UPDATE mone_game SET money_quantity = %s WHERE user_id = %s;", (vs, callid,))
                        conn.commit()
                        await call.message.edit_text('Тобі не пощастило випав Червоний🔴. Чекаємо через 6 годин')
        except TypeError:
            await call.message.edit_text("Ви не в грі пропишіть '/beb'. І спробуйте щастя через 6 годин")                

    else:
        await call.answer('Не ти викликав БеброКазино, на вихід', show_alert=True)
   


@dp.message_handler(regexp=r"базик казино")
async def kazino(message: types.Message):
    resultdate = datetime.now().replace(minute=0, second=0, microsecond=0)
    global usrid
    usrid = message.from_user.id
    global q
    cursor.execute("SELECT game_time FROM kazino WHERE usr_id = %s", [usrid])
    resultgamedate = cursor.fetchone()
    try:
        for date in resultgamedate:
            final_time = date + timedelta(hours=6)
            print(final_time > date)
            print(final_time)
            
            if final_time > resultdate:    
                await message.reply("Залишилося 6 годин. Спробуйте пізніше")
            else:
                q = random.randint(1, 2)
                sx = InlineKeyboardButton('Червоний🔴', callback_data='btn1')
                sw = InlineKeyboardButton('Чорний⚫️', callback_data='btn2')
                okk = InlineKeyboardMarkup(row_width=1, resize_keyboard=True, ).add(sw, sx)
                sa = 'Вітаємо в БеброКазино'
                print(q)
                await message.reply(sa, reply_markup=okk)
                cursor.execute('INSERT into kazino (usr_id, game_time) VALUES (%s, %s) ON CONFLICT (usr_id) DO UPDATE SET game_time = %s WHERE kazino.usr_id = %s;', (usrid, resultdate, resultdate, usrid, ))
                conn.commit()
    except:
        q = random.randint(1, 2)
        sx = InlineKeyboardButton('Червоний🔴', callback_data='btn1')
        sw = InlineKeyboardButton('Чорний⚫️', callback_data='btn2')
        okk = InlineKeyboardMarkup(row_width=1, resize_keyboard=True, ).add(sw, sx)
        sa = 'Вітаємо в БеброКазино'
        print(q)
        await message.reply(sa, reply_markup=okk)       
        cursor.execute('INSERT into kazino (usr_id, game_time) VALUES (%s, %s) ON CONFLICT (usr_id) DO UPDATE SET game_time = %s WHERE kazino.usr_id = %s;', (usrid, resultdate, resultdate, usrid, ))
        conn.commit()
@dp.message_handler(commands='add_photo')
async def scan_message(message: types.Message):
    usrid = message.from_user.id
    ff = message.reply_to_message.photo[-1].file_id

    if usrid == 578408714:
        print('додав: ' + ff)
        cursor.execute("INSERT into zhopu (photka) VALUES (%s);", (ff,))
        conn.commit()
        await message.reply('Успішно додано')
        
    else:
        await message.reply(':| 0===3\n:() 0===3\n:()==3\n:()=3 \n:3')


@dp.message_handler(commands='add_white')
async def add_white(message: types.Message):
    usrid = message.from_user.id
    usreid = message.reply_to_message.from_user.id
    nameuser = message.reply_to_message.from_user.first_name
    if usrid == 578408714:
        cursor.execute("INSERT into whitelist (usr_id, username) VALUES (%s, %s);", (usreid, nameuser,))
        conn.commit()
        await message.reply('Успішно додано')
        
    else:
        await message.reply(':| 0===3\n:() 0===3\n:()==3\n:()=3 \n:3')


@dp.message_handler(commands='whites')
async def white(message: types.Message):
    usrid = message.from_user.id
    cursor.execute("SELECT usr_id FROM whitelist WHERE usr_id = %s", (usrid, ))
    idq = cursor.fetchone()
    for idqi in idq:
        print(str(usrid) +  ' ' + idqi)
        if usrid == int(idqi):
            cursor.execute("SELECT username FROM whitelist ORDER BY usr_id DESC")
            ids = cursor.fetchall()
            baa = ['🕍🕍🕍 Легенди:\n']
            for idiy in ids:
                k = idiy[0]
                print(k)
                bal = (' - ' + str(idiy[0]))
                baa.append(bal)
            print(*baa)
            await message.reply('\n'.join(baa))
            conn.commit()

        else:
            await message.reply('йди нахуй')

    


@dp.message_handler(commands='add_chmo')
async def rusak(message: types.Message):
    usrid = message.from_user.id
    texts = message.reply_to_message.text
    if usrid == 578408714:

        print(texts)
        cursor.execute("INSERT into rusaku (texts) VALUES (%s);", (texts,))
        conn.commit()
        await message.reply('Успішно додано')
        
    else:
        await message.reply(':| 0===3\n:() 0===3\n:()==3\n:()=3 \n:3')

@dp.message_handler(commands='pay')
async def whit(message: types.Message):
    usrid = message.from_user.id
    userid = message.from_user.username
    usreid = message.reply_to_message.from_user.id
    nameuser = message.reply_to_message.from_user.first_name
    username = message.from_user.first_name
    try:
        cursor = conn.cursor()
        a = message.text.split()
        b = a[1]
        cursor.execute("SELECT money_quantity, name FROM mone_game WHERE user_id = %s", (usrid,))
        fromUSR = cursor.fetchall()
        cursor.execute("SELECT money_quantity, name FROM mone_game WHERE user_id = %s", (usreid,))
        toUSR = cursor.fetchall()
        cursor.execute("SELECT user_id  FROM mone_game WHERE name = %s", (nameuser,))
        xUS = cursor.fetchall()
        print(xUS)
        for money in fromUSR:
            for groshi in toUSR:
                for gx in xUS:
                    sa = money[0] - int(a[1])
                    asa = groshi[0] + int(a[1])
                    print(str(gx[0]) + ' ' + str(money[1]) + ' ' + str(groshi[1]))
                    if sa < 0 or money[0] < 0:
                        await message.reply("🕍 Іди нахуй жид")
                    elif int(gx[0]) == int(usrid):
                        xo = ['Стань перед зеркалом і подрочи на себе, зрозуміло пояснив? 🕍',
                              "Ти дебіл чи тільки прикидаєшся? ⚡️"]
                        await message.reply(random.choice(xo))
                    elif int(a[1]) <= 0:
                        await message.reply("🕍🕍🕍 Йди в пезду жид тупий")
                    else:
                        cursor.execute("UPDATE mone_game SET money_quantity = %s WHERE user_id = %s;", (sa, usrid,))
                        conn.commit()
                        cursor.execute("UPDATE mone_game SET money_quantity = %s WHERE user_id = %s;", (asa, usreid,))
                        conn.commit()

                        if int(a[1]) == 1:
                            await message.reply('🏧⚡️ ' + money[1] + " перевів " + groshi[1] + ' ' + a[1] + ' бебрy.')
                        elif int(a[1]) <= 4:
                            await message.reply('🏧⚡️ ' + money[1] + " перевів " + groshi[1] + ' ' + a[1] + ' бебри.')
                        else:
                            await message.reply('🏧⚡️ ' + money[1] + " перевів " + groshi[1] + ' ' + a[1] + ' бебр.')
    except TypeError:
        await message.reply('Ти не в грі, пропиши /beb')


@dp.message_handler()
async def send_welcome(message: types.Message):
    
    if random.randint(0, 100) < 2:
        baza = ['Трушно', 'Не трушно', 'База', 'Хуяза']
        await message.reply(random.choice(baza))

    baz = ['CAACAgIAAxkBAAEEGq9iKgNHYU0xMkuKXtChybqa_WRWOwACxhUAAr8KGEuTt1d3LkE_vyME',
           'CAACAgIAAxkBAAEEGrBiKgNIUltzuUglZYcUaEbfvv9oJwACqAADfpo8IFurssjtFkOIIwQ',
           'CAACAgIAAxkBAAEEGrFiKgNIvhsNe4cDChsZFWfK8pjOeAACAgADEYgpK9WpgMrSMMByIwQ']

    if random.randint(0, 100) < 2:
        await message.reply_sticker(sticker=random.choice(baz))

    if "хуяза" in message.text or "Хуяза" in message.text:
        await message.reply("Пшов нахуй хлоп")

    oo = ["Хуяза", "Азову?"]
    if "База" in message.text or "база" in message.text:
        await message.reply(random.choice(oo))

    if "в✡️ва" in message.text:
        await message.reply("так він підар")

    if message.text == "да" or message.text == "Да":
        await message.reply("Пізда")
    op = ['В жопі огірок', 'В пизді брусок', 'В носі носок', 'Хуйок', 'В шлунку колобок', 'Сала шматок',
          'Насри в мішок', 'Пупок', 'Лисий підарок', 'Ти мій підарок']
    if message.text == "Ок" or message.text == "ок":
        await message.reply(random.choice(op))
    if 'Базик русня' in message.text or 'базик русня' in message.text:
        usrid = message.from_user.id
        txt = message.reply_to_message
        ok = False
        cursor.execute("SELECT usr_id FROM whitelist WHERE usr_id = %s", (usrid,))
        dq = cursor.fetchone()
        try:
            for idq in dq:
                print(str(usrid) + ' ' + str(idq))
                if str(usrid) == str(idq):
                    ok = True
        except:
            None
        if ok == True:
            xz = cursor.execute("SELECT texts FROM rusaku ORDER BY random() LIMIT 1")
            xz = cursor.fetchone()
            for xx in xz:
                await txt.reply(xx)
        else:
            await message.reply(':| 0===3\n:() 0===3\n:()==3\n:()=3 \n:3')
        


if __name__ == '__main__':
    
    executor.start_polling(dp, skip_updates=True)
