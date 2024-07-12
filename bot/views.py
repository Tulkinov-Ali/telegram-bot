from contextlib import closing

from django.db import connection
from methodism import dictfetchall, dictfetchone
from telegram import Update, Bot
from .models import Tg_user, Category, Products, Cart
from .buttons import inline_butt, key_butt
from .gblobal import Text, BUTTONS, Admins
from .tgbot_admin import admin_msg_handler


def lang_change(update: Update, context: Bot):
    tg_user = update.message.from_user
    user = Tg_user.objects.get(user_id=tg_user.id)
    update.message.reply_text(Text['STEP-1'], reply_markup=inline_butt('lang'))
    user.log = {'state': 'lang'}
    user.save()
    return 0


def start(update: Update, context: Bot):
    tg_user = update.message.from_user
    user = Tg_user.objects.get_or_create(user_id=tg_user.id)[0]

    if user.is_admin:
        update.message.reply_text(Admins['Welcome'][user.lang], reply_markup=key_butt('admin', lang=user.lang))
        user.log = {"state": 30}
        user.save()
        return 0

    if user.log['state'] is int and user.log['state'] < 10:
        update.message.reply_text(Text['STEP-1'], reply_markup=inline_butt('lang'))
        user.log = {'state': 1}
        user.username = tg_user.username
        user.save()
        return 0
    else:
        update.message.reply_text(Text['MENU'][user.lang], reply_markup=key_butt("Menu", lang=user.lang))
        user.log = {'state': 10}
        user.save()
        return 0


def msg_handler(update, context):
    msg = update.message.text
    tg_user = update.message.from_user
    user = Tg_user.objects.get(user_id=tg_user.id)
    log = user.log
    if user.is_admin:
        admin_msg_handler(update, context, user, msg, log)
        return 0
    elif msg == 'admin':
        update.message.reply_text(Admins['password'][user.lang])
        user.log = {'state': 'password'}
        user.save()
        return 0
    elif log['state'] == 'password':
        if msg == 'secret':
            user.is_admin = True
            user.menu = 2
            user.log = {"state": 30}
            user.save()
            update.message.reply_text(Admins['Welcome'][user.lang], reply_markup=key_butt('admin', lang=user.lang))
        else:
            update.message.reply_text(Admins['password-error'][user.lang])
        return 0
    if msg == BUTTONS['MENU']['back'][user.lang]:
        if log['state'] == 13:
            ctg = Category.objects.filter(id=log['ctg']).first()
            if not ctg:
                update.message.reply_text(Text['CTG-Errors'][user.lang])
                return 0
            markup = key_butt('prods', ctg=ctg, lang=user.lang)
            if not markup.keyboard:
                update.message.reply_text(Text['Products-CTG-Error'][user.lang])
                return 0

            img = ctg.img.path
            update.message.reply_photo(open(img, 'rb'), caption=ctg.name, reply_markup=markup)
            log['state'] = 12
            log['ctg'] = ctg.id
            user.log = log
            user.save()
            return 0

        elif log['state'] == 12:
            update.message.reply_text(Text['CTG'][user.lang], reply_markup=key_butt('ctg', lang=user.lang))
            user.log = {'state': 11}
            user.save()
            return 0

        elif log['state'] == 11:
            update.message.reply_text(Text['MENU'][user.lang], reply_markup=key_butt("Menu", lang=user.lang))
            user.log = {'state': 10}
            user.save()
            return 0

    elif msg == BUTTONS['MENU']['MainMenu'][user.lang]:
        update.message.reply_text(Text['MENU'][user.lang], reply_markup=key_butt("Menu", lang=user.lang))
        user.log = {'state': 10}
        user.save()
        return 0


    elif msg in BUTTONS['MENU']['menu'].values():
        update.message.reply_text(Text['CTG'][user.lang], reply_markup=key_butt('ctg', lang=user.lang))
        user.log = {'state': 11}
        user.save()

    elif msg == BUTTONS['MENU']['cart'][user.lang]:
        s = f"{Text['Food'][user.lang]}\n"
        sql_all = f"""select cart.quant, cart.summ, pro.name from bot_cart cart
                    inner join bot_products pro on pro.id = cart.product_id
                    where cart.user_id = {tg_user.id}"""

        summa = f"SELECT sum(summ) as summa from bot_cart cart where cart.user_id = {tg_user.id}"
        with closing(connection.cursor()) as cursor:
            cursor.execute(sql_all)
            all = dictfetchall(cursor)
            if not all:
                update.message.reply_text('cart is empty')
                return 0
            cursor.execute(summa)
            summa = dictfetchone(cursor)
        for i in all:
            s += f'🍽{i["name"]}✖️{i["quant"]}🟰{i["summ"]}\n'
        s += f"{Text['Delivery'][user.lang]} 10$\n{Text['Overall'][user.lang]} {summa['summa'] + 12000} so'm"
        update.message.reply_text(s)
        return 0
    elif log['state'] == 1:
        update.message.reply_text(Text['STEP-1'], reply_markup=inline_butt('lang'))
        return 0

    elif log['state'] == 2:
        if msg.isalpha():
            user.name = msg
            user.log = {'state': 3}
            user.save()
            update.message.reply_text(Text['STEP-3'][user.lang])
        else:
            update.message.reply_text(Text['STEP-2_Errors'][user.lang])
        return 0

    elif log['state'] == 3:
        if msg.isalpha():
            user.surname = msg
            user.log = {'state': 4}
            user.save()
            update.message.reply_text(Text['STEP-4'][user.lang], reply_markup=key_butt('Contact', lang=user.lang))
        else:
            update.message.reply_text(Text['STEP-3_Errors'][user.lang])
        return 0
    elif log['state'] == 4:
        update.message.reply_text(Text['STEP-4_Errors'][user.lang])

    elif log['state'] == 11:
        ctg = Category.objects.filter(name=msg).first()
        if not ctg:
            update.message.reply_text(Text['CTG-Errors'][user.lang])
            return 0
        markup = key_butt('prods', ctg=ctg, lang=user.lang)
        if not markup.keyboard:
            update.message.reply_text(Text['Products-CTG-Error'][user.lang])
            return 0

        img = ctg.img.path
        update.message.reply_photo(open(img, 'rb'), caption=ctg.name, reply_markup=markup)
        log['state'] = 12
        log['ctg'] = ctg.id
        user.log = log
        user.save()
        return 0
        # update.message.reply_text(Text['Products'][user.lang])
    elif log['state'] == 12:
        prod = Products.objects.filter(name=msg).first()
        if not prod:
            update.message.reply_text(Text['Products-Errors'][user.lang])
            return 0
        s = f"""{Text['Product-Info']['name'][user.lang]}{prod.name}\n{Text['Product-Info']['descript'][user.lang]}{prod.desc}\n{Text['Product-Info']['price'][user.lang]}{prod.price}so'm"""
        update.message.reply_photo(open(prod.img.path, 'rb'), caption=s,
                                   reply_markup=inline_butt('prod', product_id=prod.id))
        log['state'] = 13
        log['ctg'] = prod.id
        user.log = log
        user.save()
        return 0
    else:
        update.message.reply_text(Text['STEP-2_Errors'][user.lang])


def inline_handler(update: Update, context: Bot):
    query = update.callback_query
    data = query.data
    tg_user = query.message.chat
    user = Tg_user.objects.get(user_id=tg_user.id)
    log = user.log
    data_sp = data.split('_')
    if data_sp[0] == 'plus':
        num = int(data_sp[2]) + 1
        prod = Products.objects.filter(id=int(data_sp[1])).first()
        s = f"""{Text['Product-Info']['name'][user.lang]}{prod.name}\n{Text['Product-Info']['descript'][user.lang]}{prod.desc}\n{Text['Product-Info']['price'][user.lang]}{prod.price * num}so'm"""
        query.message.edit_caption(caption=s, reply_markup=inline_butt('prod', product_id=prod.id, count=num))
        return 0

    elif data_sp[0] == 'minus':
        if int(data_sp[2]) == 1:
            query.answer(Text['Minus'][user.lang])
            return 0
        num = int(data_sp[2]) - 1
        prod = Products.objects.filter(id=int(data_sp[1])).first()
        s = f"""{Text['Product-Info']['name'][user.lang]}{prod.name}\n{Text['Product-Info']['descript'][user.lang]}{prod.desc}\n{Text['Product-Info']['price'][user.lang]}{prod.price * num}so'm"""
        query.message.edit_caption(caption=s, reply_markup=inline_butt('prod', product_id=prod.id, count=num))
        return 0

    elif data_sp[0] == 'nothing':
        query.answer(Text['Nothing'][user.lang])
        return 0

    elif data_sp[0] == 'cart':
        cart = Cart.objects.get_or_create(user_id=tg_user.id, product_id=int(data_sp[1]))[0]
        cart.quant = int(data_sp[2]) + cart.quant
        cart.save()
        query.message.delete()
        query.message.reply_text(Text['Cart'][user.lang], reply_markup=key_butt('menu', lang=user.lang))
        user.log = {'state': 10}
        user.save()
        return 0

    if log['state'] == 1:
        query.message.delete()
        user.lang = data
        query.message.reply_text(Text['STEP-2'][data])
        user.log = {'state': 2}
        user.save()
        return 0
    elif log['state'] == 'lang':
        query.message.delete()
        query.message.reply_text(Text['LANGUAGE'][data], reply_markup=key_butt('Menu', lang=data))
        user.lang = data
        user.log = {'state': 10}
        user.save()
        return 0
    elif log['state'] == 13:
        query.message.reply_text(Text['LANGUAGE'][data], reply_markup=key_butt('menu', lang=data))


def contact_handler(update: Update, context: Bot):
    contact = update.message.contact
    tg_user = update.message.from_user
    user = Tg_user.objects.get(user_id=tg_user.id)
    log = user.log
    if log['state'] == 4:
        update.message.reply_text(Text['MENU'][user.lang], reply_markup=key_butt("Menu", lang=user.lang))
        user.phone = contact.phone_number
        user.log = {'state': 10}
        user.save()
        return 0


def make_admin(update, context):
    tg_user = update.message.from_user
    user = Tg_user.objects.get_or_create(user_id=tg_user.id)[0]
