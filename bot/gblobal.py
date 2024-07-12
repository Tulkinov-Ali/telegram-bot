from telegram import Update

Text = {

    "STEP-1": "Please choose the language\n\nПожалуйста выберите язык\n\nIltimos tilni tanlang",
    "STEP-2": {
        "en": "Please enter your name",
        "ru": "Пожалуйста введите своё имя",
        "uz": "Iltimos ismingizni kiriting"
    },
    "STEP-2_Errors": {
        "en": "Occured error",
        "ru": "Произошла ошибка",
        "uz": "Hatolik yuz berdi"
    },
    "STEP-3": {
        "en": "Please enter your surnaname",
        "ru": "Пожалуйста введите свою фамилию",
        "uz": "Iltimos familiyangizni kiriting"
    },
    "STEP-3_Errors": {
        "en": "Occured error",
        "ru": "Произошла ошибка",
        "uz": "Hatolik yuz berdi"
    },
    "STEP-4": {
        "en": "Please enter your contact",
        "ru": "Пожалуйста введите свой контакт",
        "uz": "Iltimos kontantingizni kiriting"
    },
    "STEP-4_Errors": {
        "en": "Occured error",
        "ru": "Произошла ошибка",
        "uz": "Hatolik yuz berdi"
    },
    "MENU": {
        "en": "Welcome, please select from Menu",
        "ru": "Добро пожаловать, пожалуйста выберите из Меню",
        "uz": "Xush kelibsiz, iltimos menudan tanlang"
    },
    "LANGUAGE": {
        "en": "Language has been changed",
        "ru": "Язык изменён",
        "uz": "Til ozgardi"
    },
    "CTG": {
        "en": "Choose from Categories",
        "ru": "Выберите Категорию",
        "uz": "Kategoriyani tanlang"
    },
    "CTG-Errors": {
        "en": "Category not Exists",
        "ru": "Категория не существует",
        "uz": "Kategoriya mavjud emas"
    },
    "Products": {
        "en": "Select the Product",
        "ru": "Выберите продукт",
        "uz": "Maxsulotni tanlang"
    },
    "Products-CTG-Error": {
        "en": "Sorry there is nothing in this category",
        "ru": "Извените категория пустая",
        "uz": "Kechirasiz bu kategoriyaga tegishli hechnarsa yoq"
    },
    "Products-Errors": {
        "en": "Product is not found",
        "ru": "Продукт не найден",
        "uz": "Maxsulot topilmadi"
    },
    "Food": {
        "en": "Foods:",
        "ru": "Еда:",
        "uz": "Ovqatlar:"
    },
    "Delivery": {
        "en": "🚚Delivery:",
        "ru": "🚚Доставка:",
        "uz": "🚚Yetkazib berish:"
    },
    "Overall": {
        "en": "💰Overall Cost:",
        "ru": "💰Общая ценa:",
        "uz": "💰Ummumiy narx:"
    },
    "Minus": {
        "en": "Your choice is minimal",
        "ru": "Это минимальное количество",
        "uz": "Bu minimal tanlov"
    },
    "Nothing": {
        "en": "You have chosen nothing",
        "ru": "Вы ничего не выбрали",
        "uz": "Siz hechnarsa tanlamadingiz"
    },
    "Cart": {
        "en": "Added to Cart",
        "ru": "Добавлен в Корзину",
        "uz": "Savatchaga qoshildi"
    },
    "Product-Info": {
        "name": {
            "en": "Name:",
            "ru": "Названия:",
            "uz": "Nomi:"
        },
        "descript": {
            "en": "Contains:",
            "ru": "Содержит:",
            "uz": "Tarkibi:"
        },
        "price": {
            "en": "Price:",
            "ru": "Цена:",
            "uz": "Narxi:"
        }
    }
}
BUTTONS = {
    "MENU": {
        'menu': {
            "en": "📖Menu",
            "ru": "📖Меню",
            "uz": "📖Menu"
        },
        'settings': {
            "en": "⚙️Settings",
            "ru": "⚙️Настройки",
            "uz": "⚙️Sozlamalar"
        },
        'cart': {
            "en": "🛒Cart",
            "ru": "🛒Корзинка",
            "uz": "🛒Savatcha"
        },
        'help': {
            "en": "🆘Help",
            "ru": "🆘Помощь",
            "uz": "🆘Yordam"
        },
        'feedback': {
            "en": "💬Feedback",
            "ru": "💬Отзывы",
            "uz": "💬Fikrlar"
        },
        'back': {
            "en": "⬅️Back",
            "ru": "⬅️Назад",
            "uz": "⬅️Orqaga"
        },
        'MainMenu': {
            "en": "🏠Main menu",
            "ru": "🏠Главное меню",
            "uz": "🏠Bo'sh menu"
        }
    },
    'CONTACT': {
        "en": "📞Contact",
        "ru": "📞Контакт",
        "uz": "📞Kontakt"
    }
}

Admins = {
    "password": {
        "en": "🔐Enter the password",
        "ru": "🔐Введите пароль",
        "uz": "🔐Parolni kiriting"
    },
    "password-error": {
        "en": "🔐Wrong password",
        "ru": "🔐Неправельный пароль",
        "uz": "🔐Notog'ri parol"
    },
    "Welcome": {
        "en": "👨‍💻Welcome to Admin panel",
        "ru": "👨‍💻Добро пожаловать в Админ панель",
        "uz": "👨‍💻Admin panelga xush kelibsiz"
    },
    "Confirm-Yes": {
        "en": "😤Yes",
        "ru": "😤Да",
        "uz": "😤Ha"
    },
    "Confirm-No": {
        "en": "No😉",
        "ru": "Нет😉",
        "uz": "Yo'q😉"
    },
    "No-pressed": {
        "en": "🥹We are glad to see you again",
        "ru": "🥹Мы рады вас видеть снова",
        "uz": "🥹Qaytganingizdan hursandmiz"
    },
    "List_Users": {
        "en": "📜List of Users",
        "ru": "📜Лист пользователей",
        "uz": "📜ishlatuvchilar ro'yxati"
    },
    "Monitoring": {
        "en": "📝Monitoring",
        "ru": "📝Мониторинг",
        "uz": "📝Monitoring"
    },
    "Monitoring-info": {
        "en": "💾Database",
        "ru": "💾База данных",
        "uz": "💾Malumotlar ombori"
    },
    "Logout": {
        "en": "🔓Logout",
        "ru": "🔓Выйти",
        "uz": "🔓Chiqish"
    },
    "Logout-conf": {
        "en": "Are you sure🧐",
        "ru": "Вы уверенны🧐",
        "uz": "Aniqmi🧐"
    },
    "Overall-list": {
        "en": "Overall:",
        "ru": "Общий:",
        "uz": "Umummiy:"
    },
    "List-name": {
        "en": "Name:",
        "ru": "Имя:",
        "uz": "Ismi:"
    },
    "List-surname": {
        "en": "Surname:",
        "ru": "Фамилия:",
        "uz": "Familiyasi:"
    },
    "Overall-info": {
        "en": "Users",
        "ru": "Пользователя",
        "uz": "ta Foydalanuchi"
    },
    "AdminCategory": {
        "en": "🗄Categories",
        "ru": "🗄Категории",
        "uz": "🗄Kategoriyalar"
    },
    "AdminProducts": {
        "en": "🛍Products",
        "ru": "🛍Продукты",
        "uz": "🛍Maxsulotlar"
    }

}
