from django_tgbot.decorators import processor
from django_tgbot.state_manager import message_types, update_types, state_types
from django_tgbot.types.keyboardbutton import KeyboardButton
from django_tgbot.types.replykeyboardmarkup import ReplyKeyboardMarkup
from django_tgbot.types.update import Update
from .bot import state_manager
from .models import TelegramState
from .bot import TelegramBot
import random


state_manager.set_default_update_types(update_types.Message)


@processor(state_manager, from_states=state_types.Reset, message_types=[message_types.Text])
def send_keyboards(bot: TelegramBot, update: Update, state: TelegramState):
    chat_id = update.get_chat().get_id()
    text = str(update.get_message().get_text())
    count = TelegramState.objects.get(telegram_chat__telegram_id=chat_id)
    jokes = {
             'stupid': ["""Yo' Mama is so stupid, she needs a recipe to make ice cubes.""",
                        """Yo' Mama is so stupid, she thinks DNA is the National Dyslexics Association."""],
             'fat':    ["""Yo' Mama is so fat, when she goes to a restaurant, instead of a menu, she gets an estimate.""",
                        """ Yo' Mama is so fat, when the cops see her on a street corner, they yell, "Hey you guys, break it up!" """],
             'dumb':   ["""THis is fun""",
                        """THis isn't fun"""]
        }
    if text == 'stupid':
        txt = random.choice(jokes['stupid'])
        count.stupid = count.stupid + 1
    elif text == 'fat':
        txt = random.choice(jokes['fat'])
        count.fat = count.fat + 1
    elif text == 'dumb':
        txt = random.choice(jokes['dumb'])
        count.dumb = count.dumb + 1
    else:
        txt = 'please select a choice'

    count.save()

    bot.sendMessage(
        chat_id,
        text=txt,
        reply_markup=ReplyKeyboardMarkup.a(
            one_time_keyboard=False,
            resize_keyboard=True,
            keyboard=[
                [KeyboardButton.a('fat'), KeyboardButton.a('stupid')],
                [KeyboardButton.a('dumb')]
            ],
    )
    )

