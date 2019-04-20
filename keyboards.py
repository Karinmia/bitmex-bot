from telebot import types
from languages import DICTIONARY


def get_main_menu_keyboard(language='ru'):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(DICTIONARY[language]['add_main_account_btn'])
    keyboard.add(DICTIONARY[language]['add_referal_btn'])
    keyboard.add(DICTIONARY[language]['delete_referal_btn'])
    return keyboard


def get_set_main_account_keyboard(language='ru'):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(DICTIONARY[language]['is_children_button'])
    keyboard.add(DICTIONARY[language]['no_children_button'])
    return keyboard


def get_add_account_keyboard(language='ru'):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(DICTIONARY[language]['olympiads_button'])
    keyboard.add(DICTIONARY[language]['ask_mon_question_btn'])
    keyboard.add(DICTIONARY[language]['rating_mon_question_btn'])
    keyboard.add(DICTIONARY[language]['back_button'])
    return keyboard


def get_delete_account_keyboard(language='ru'):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(DICTIONARY[language]['excursion_button'])
    keyboard.add(DICTIONARY[language]['all_about_nush_btn'])
    keyboard.add(DICTIONARY[language]['back_button'])
    return keyboard


def get_back_button_keyboard(language='ru'):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(DICTIONARY[language]['back_button'])
    return keyboard
