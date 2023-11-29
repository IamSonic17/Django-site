from django.db import models


class Reviews(models.Model):
    title = models.CharField('Название', max_length=50)
    description = models.CharField('Описание', max_length=250)
    full_text = models.TextField('Текст', max_length=5500)
    date = models.DateField('Дата Публикации')
    image = models.ImageField(upload_to='main/img/', null=True, blank=True)
    objects = models.Manager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Рецензия"
        verbose_name_plural = "Рецензии"