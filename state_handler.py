from database import User
from states import *

states = {'main_menu_state': main_menu_state,
          'set_main_api_key_state': set_main_api_key_state,
          'set_main_api_secret_state': set_main_api_secret_state,
          # 'add_referal_state': add_referal_state,
          # 'delete_referal_state': delete_referal_state,
          }


# def get_state_and_process_callback_query(reply, user: User, is_entry=False):
#     universal_callback_query_handler(reply, user)


def get_state_and_process(message, user: User, is_entry=False):
    if user.state in states:
        change_state, state_to_change_name = states[user.state](message, user, is_entry)
    else:
        user.state = 'choose_status_state'
        user.save()
        change_state, state_to_change_name = states[user.state](message, user, is_entry)
    if change_state:
        go_to_state(message, state_to_change_name, user)


def go_to_state(message, state_name: str, user: User):
    user.state = state_name
    user.save()
    get_state_and_process(message, user, is_entry=True)
