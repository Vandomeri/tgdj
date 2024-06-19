from django.db import models
from telegram_django_bot.models import TelegramUser


class User(TelegramUser):
    pass


# add here other models


class Quiz(models.Model):
    name = models.CharField(max_length=30, verbose_name="Название теста")

    def __str__(self) -> str:
        return self.name


class Question(models.Model):
    title = models.CharField(max_length=100, verbose_name="Текст вопроса")
    quiz = models.ForeignKey(Quiz, null=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title


class Answer(models.Model):
    title = models.CharField(max_length=100, verbose_name="Вариант ответа")
    question = models.ForeignKey(Question, null=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
