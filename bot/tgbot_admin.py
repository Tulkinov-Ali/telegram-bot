from contextlib import closing

from django.db import connection
from methodism import dictfetchone, dictfetchall
from telegram import KeyboardButton, ReplyKeyboardMarkup


from bot.admin_buttons import admini_btns
from bot.buttons import key_butt
from bot.gblobal import Text, Admins, BUTTONS


def admin_msg_handler(update, context, user, msg, log):
    if msg == BUTTONS['MENU']['back'][user.lang]:
        if log['state'] == 32:
            update.message.reply_text(BUTTONS['MENU']['back'][user.lang],
                                      reply_markup=key_butt('admin', lang=user.lang))
            user.log = {'state': 30}
            user.save()
            return 0

        elif log['state'] == 31:
            update.message.reply_text(BUTTONS['MENU']['back'][user.lang],
                                      reply_markup=key_butt('admin', lang=user.lang))
            user.log = {'state': 30}
            user.save()
            return 0


    elif msg == Admins['List_Users'][user.lang]:
        users = "select user_id, name, surname, username from bot_tg_user limit 10"
        cnt = "SELECT COUNT(*) as cnt from bot_tg_user"
        with closing(connection.cursor()) as cursor:
            cursor.execute(users)
            all = dictfetchall(cursor)

            cursor.execute(cnt)
            cnt = dictfetchone(cursor)

        s = f"{Admins['Overall-list'][user.lang]} {cnt['cnt']} {Admins['Overall-info'][user.lang]}\n\n"
        for i in all:
            s += f'ID: {i["user_id"]} \n{Admins["List-name"][user.lang]} {i["name"]}\n{Admins["List-surname"][user.lang]} {i["surname"]}\n\n'

        update.message.reply_text(s)

    elif msg == Admins['Logout'][user.lang]:
        update.message.reply_text(Admins['Logout-conf'][user.lang], reply_markup=admini_btns('conf', lang=user.lang))
        user.log = {'state': 31}
        user.save()
        return 0

    elif msg == Admins['Monitoring'][user.lang]:
        update.message.reply_text(Admins['Monitoring-info'][user.lang],
                                  reply_markup=admini_btns('menu', lang=user.lang))
        user.log = {'state': 32}
        user.save()
        return 0

    if log['state'] == 31:
        if msg == Admins['Confirm-Yes'][user.lang]:
            update.message.reply_text(Text['MENU'][user.lang], reply_markup=key_butt("Menu", lang=user.lang))
            user.log = {'state': 10}
            user.is_admin = False
            user.save()
            return 0

        elif msg == Admins['Confirm-No'][user.lang]:
            update.message.reply_text(Admins['No-pressed'][user.lang], reply_markup=key_butt("admin", lang=user.lang))
            user.log = {'state': 30}
            user.save()
            return 0
