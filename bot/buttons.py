from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from .gblobal import BUTTONS, Admins
from .models import Category, Products


def key_butt(type, lang='en', ctg: Category = None):
    btn = []
    if type == 'Contact':
        btn = [
            [KeyboardButton(f"📞{BUTTONS['CONTACT'][lang]}", request_contact=True)]
        ]
    elif type == 'Menu':
        btn = [
            [KeyboardButton(f"{BUTTONS['MENU']['menu'][lang]}")],
            [KeyboardButton(f"{BUTTONS['MENU']['cart'][lang]}"),
             KeyboardButton(f"{BUTTONS['MENU']['settings'][lang]}")],
            [KeyboardButton(f"{BUTTONS['MENU']['help'][lang]}"),
             KeyboardButton(f"{BUTTONS['MENU']['feedback'][lang]}")],
        ]
    elif type == 'ctg':
        category = Category.objects.all()
        btn = []
        for i in range(1, len(category), 2):
            btn.append([
                KeyboardButton(category[i - 1].name),
                KeyboardButton(category[i].name),
            ])
        if len(category) % 2:
            btn.append([KeyboardButton(category[len(category) - 1].name)]),
        btn.append([KeyboardButton(f"{BUTTONS['MENU']['back'][lang]}"),
                    KeyboardButton(f"{BUTTONS['MENU']['MainMenu'][lang]}")], )
    elif type == 'prods':
        roots = Products.objects.filter(ctg=ctg)
        btn = []
        for i in range(1, len(roots), 2):
            btn.append([
                KeyboardButton(roots[i - 1].name),
                KeyboardButton(roots[i].name),
            ])
        if len(roots) % 2:
            btn.append([KeyboardButton(roots[len(roots) - 1].name)]),
        btn.append([KeyboardButton(f"{BUTTONS['MENU']['back'][lang]}"),
                    KeyboardButton(f"{BUTTONS['MENU']['MainMenu'][lang]}")], )

    elif type == 'prod':
        btn = [
            [KeyboardButton(f"{BUTTONS['MENU']['back'][lang]}"),
             KeyboardButton(f"{BUTTONS['MENU']['MainMenu'][lang]}")],
        ]

    elif type == 'admin':
        btn = [
            [KeyboardButton(Admins['Monitoring'][lang]),
             KeyboardButton(Admins['List_Users'][lang])],
            [KeyboardButton(Admins['Logout'][lang])],
        ]

    return ReplyKeyboardMarkup(btn, resize_keyboard=True)


def inline_butt(type, product_id=None, count=1, all=0):
    btn = []

    if type == 'lang':
        btn = [[
            InlineKeyboardButton('🇺🇿uz', callback_data='uz'),
            InlineKeyboardButton('🇷🇺ru', callback_data='ru'),
            InlineKeyboardButton('🇺🇸en', callback_data='en')
        ]]

    elif type == 'prod':
        btn = [
            [
                InlineKeyboardButton('-', callback_data=f'minus_{product_id}_{count}'),
                InlineKeyboardButton(f'{count}', callback_data='nothing'),
                InlineKeyboardButton('+', callback_data=f'plus_{product_id}_{count}')
            ],
            [
                InlineKeyboardButton('🛒add to Cart', callback_data=f'cart_{product_id}_{count}')

            ]
        ]

    return InlineKeyboardMarkup(btn)
