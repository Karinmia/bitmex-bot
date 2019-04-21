from time import sleep

from bot_object import bot
from database import ADMINS, BitmexAccount
from languages import DICTIONARY
from keyboards import *


def main_menu_state(message, user, is_entry=False):
    if is_entry:
        if user.user_id not in ADMINS == True:
            bot.send_message(message.chat.id,
                             'Чтобы воспользоваться этой функцией нужно быть админом :)')
            return False, ''
        else:
            bot.send_message(message.chat.id,
                             DICTIONARY['ru']['mainmenu_msg'])
            sleep(0.5)
            bot.send_message(message.chat.id,
                             DICTIONARY['ru']['help_msg'],
                             reply_markup=get_main_menu_keyboard('ru'))
    else:
        if message.text == DICTIONARY['ru']['add_main_account_btn']:
            return True, 'set_main_api_key_state'
        elif message.text == DICTIONARY['ru']['add_referal_btn']:
            return True, 'add_referal_state'
        elif message.text == DICTIONARY['ru']['delete_referal_btn']:
            return True, 'delete_referal_state'
        else:
            bot.send_message(message.chat.id,
                             DICTIONARY['ru']['no_button'])
    return False, ''


def set_main_api_key_state(message, user, is_entry=False):
    if is_entry:
        bot.send_message(message.chat.id,
                         DICTIONARY['ru']['set_api_key_msg'])
    else:
        bitmex_acc = BitmexAccount(api_key=message.text, is_main=True)
        bitmex_acc.save()
        return True, 'set_main_api_secret_state'
    return False, ''


def set_main_api_secret_state(message, user, is_entry=False):
    if is_entry:
        bot.send_message(message.chat.id,
                         DICTIONARY['ru']['set_api_secret_msg'])
    else:
        bitmex_acc = BitmexAccount.objects(is_main=True).first()
        bitmex_acc.api_secret = message.text
        bitmex_acc.save()
        bot.send_message(message.from_user.id,
                         DICTIONARY['add_account_success_btn'])
        return True, 'main_menu_state'
    return False, ''
