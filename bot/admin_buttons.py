from contextlib import closing

from django.db import connection
from methodism import dictfetchone, dictfetchall
from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

from bot.gblobal import Admins, BUTTONS


def admini_btns(type, lang='en'):
    btn = []
    if type == 'conf':
        btn = [
            [KeyboardButton(Admins['Confirm-Yes'][lang]), KeyboardButton(Admins['Confirm-No'][lang])]
        ]
    elif type == 'menu':
        btn = [
            [KeyboardButton(Admins['AdminCategory'][lang]), KeyboardButton(Admins['AdminProducts'][lang])],
            [KeyboardButton(BUTTONS['MENU']['back'][lang])],
        ]
    return ReplyKeyboardMarkup(btn, resize_keyboard=True)


def admin_inline(type=None, page=1):
    btn = []
    if type == 'ctgs':
        offset = (page - 1) * 1
        sql = f"select * from bot_category limit 1 offset {offset}"
        cnt = "select count(*) as cnt from bot_category"
        with closing(connection.cursor()) as cursor:
            cursor.execute(sql)
            one = dictfetchone(cursor)
            cursor.execute(cnt)
            cnt = dictfetchall(cursor)


        btn = [
            [InlineKeyboardButton("<", callback_data=f"ctg_{one['id']}_{page}")],
            [InlineKeyboardButton(f"{page}/{cnt['cnt']}", callback_data=f"ctg_none")],
            [InlineKeyboardButton(">", callback_data=f"ctg_{one['id']}_{page}")],
        ]
    return InlineKeyboardMarkup(btn)

