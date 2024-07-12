from django.conf import settings
from django.core.management import BaseCommand
from telegram.ext import Updater, MessageHandler, CommandHandler, CallbackQueryHandler, Filters
from bot.views import start, lang_change, msg_handler, inline_handler, contact_handler, make_admin


class Command(BaseCommand):
    def handle(self, *args, **options):
        updater = Updater(settings.TOKEN)
        updater.dispatcher.add_handler(CommandHandler('start', start))
        updater.dispatcher.add_handler(CommandHandler('lang', lang_change))
        updater.dispatcher.add_handler(CommandHandler('admin', make_admin))

        updater.dispatcher.add_handler(CallbackQueryHandler(inline_handler))
        updater.dispatcher.add_handler(MessageHandler(Filters.text, msg_handler))
        updater.dispatcher.add_handler(MessageHandler(Filters.contact, contact_handler))

        print('your bot is running')
        updater.start_polling()
        updater.idle()
