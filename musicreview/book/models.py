from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField('Тема сообщения', max_length=150)
    full_text = models.TextField('Текст сообщения', max_length=1000)
    date = models.DateTimeField('Дата публикации')
    objects = models.Manager()

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"

