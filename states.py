from time import sleep

from bot_object import bot
from database import ADMINS
from languages import DICTIONARY
from keyboards import *


def main_menu_state(message, user, is_entry=False):
    if is_entry:
        if user.user_id not in ADMINS:
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
            user.save()
            return True, 'parents_state'
        elif message.text == DICTIONARY['ru']['add_referal_btn']:
            user.save()
            return True, 'teachers_state'
        elif message.text == DICTIONARY['ru']['delete_referal_btn']:
            user.save()
            return True, 'teachers_state'
        else:
            bot.send_message(message.chat.id,
                             DICTIONARY['ru']['no_button'])
    return False, ''


def set_main_account_state(message, user, is_entry=False):
    print('\n\n--- IN set_main_account_state STATE---\n')
    if is_entry:
        bot.send_message(message.from_user.id,
                         DICTIONARY['enter_product_name_msg'])
    else:
        product = session.query(Product).order_by(Product.id.desc()).first()
        if product is None:
            new_product = Product(id=1, name=message.text)
        else:
            new_product = Product(id=product.id+1, name=message.text)
        session.add(new_product)
        session.commit()
        return True, 'add_new_product_description_state'
    return False, ''
