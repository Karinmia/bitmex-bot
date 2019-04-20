from bot_object import bot
from database import User
from state_handler import get_state_and_process
from languages import DICTIONARY


@bot.message_handler(commands=['start'])
def send_welcome(message):
    try:
        user = User.objects(user_id=message.from_user.id).first()
        if user is None:
            user = User(user_id=message.from_user.id,
                        username=message.from_user.username,
                        first_name=message.from_user.first_name,
                        last_name=message.from_user.last_name,
                        state='main_menu_state'
                        )
            user.save()
        else:
            user.state = 'main_menu_state'
            user.save()
            # user.update(state='main_menu_state')
        get_state_and_process(message, user, True)
    except Exception as e:
        print(e)


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        user = User.objects(user_id=message.from_user.id).first()
        if user is None:
            user = User(user_id=message.from_user.id,
                        username=message.from_user.username,
                        first_name=message.from_user.first_name,
                        last_name=message.from_user.last_name,
                        state='main_menu_state'
                        )
            user.save()
        get_state_and_process(message, user)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    bot.remove_webhook()
    bot.polling(none_stop=True)
