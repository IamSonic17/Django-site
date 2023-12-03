from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Book2(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField('Тема сообщения', max_length=150)
    full_text = models.TextField('Текст сообщения', max_length=1000)
    objects = models.Manager()

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"


class Book3(models.Model):
    author = models.CharField('Автор', max_length=50)
    subject = models.CharField('Тема сообщения', max_length=150)
    full_text = models.TextField('Текст сообщения', max_length=1000)
    date = models.DateTimeField('Дата', default=timezone.now)  # timezone.datetime.today()
    objects = models.Manager()

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
