from django.db import models


class Bio(models.Model):
    title = models.CharField('Название', max_length=50)
    description = models.CharField('Описание', max_length=250)
    full_text = models.TextField('Текст', max_length=5500)
    date = models.DateField('Дата Публикации')
    objects = models.Manager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Биография"
        verbose_name_plural = "Биографии"