from telegram_django_bot.td_viewset import TelegramViewSet
from telegram_django_bot.user_viewset import UserViewSet as TGUserViewSet, UserForm
from telegram_django_bot.models import BotMenuElem
from telegram_django_bot.utils import handler_decor
from telegram_django_bot.telegram_lib_redefinition import InlineKeyboardButtonDJ

from django.conf import settings
from django.utils.translation import gettext as _, gettext_lazy
from telegram_django_bot.routing import telegram_reverse
from telegram_django_bot.tg_dj_bot import TG_DJ_Bot
from telegram import Update
from .forms import BotMenuElemForm, QuizForm
from .models import Quiz, User


@handler_decor()
def start(bot: TG_DJ_Bot, update: Update, user: User):
    message = _(f"Привет, добро пожаловать в IThub Quiz!") % {
        "name": user.first_name or user.telegram_username or user.id
    }

    buttons = [
        [InlineKeyboardButtonDJ(text=("Quiz"), callback_data="quizes_list")],
    ]

    return bot.edit_or_send(update, message, buttons)


@handler_decor()
def quizes(bot: TG_DJ_Bot, update: Update, user: User):
    # the message is written in Django notation for translation (with compiling language you can easy translate text)
    message = "Выберите интересный для вас квиз %(user)s" % {"user": user}
    quizes = Quiz.objects.all()
    buttons = []
    for quiz in quizes:
        callback = f"quiz{quiz.pk}"
        buttons.append(
            [
                InlineKeyboardButtonDJ(
                    text=f"quiz{quiz.pk}",
                    callback_data=callback,
                )
            ]
        )
    return bot.edit_or_send(update, message, buttons)


@handler_decor()
def quiz1(bot: TG_DJ_Bot, update: Update, user: User):
    # the message is written in Django notation for translation (with compiling language you can easy translate text)
    message = "Добро пожаловать в квиз %(user)s" % {"user": user}

    buttons = []

    return bot.edit_or_send(update, message, buttons)
