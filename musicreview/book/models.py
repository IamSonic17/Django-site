from django.db import models


class Book3(models.Model):
    author = models.CharField('Автор', max_length=50)
    subject = models.CharField('Тема сообщения', max_length=150)
    full_text = models.TextField('Текст сообщения', max_length=1000)
    date = models.DateTimeField(auto_now_add=True, help_text='Дата создания')
    objects = models.Manager()

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
