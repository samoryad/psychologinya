from django.db import models


class Specialist(models.Model):
    short_name = models.CharField(max_length=64, unique=True, verbose_name='имя')
    full_name = models.CharField(max_length=64, unique=True, verbose_name='полное имя')
    image = models.ImageField(upload_to='specialists_photos', blank=True, verbose_name='фото')
    tel = models.CharField(max_length=32, verbose_name='телефон')
    profession = models.CharField(max_length=128, blank=True, verbose_name='профессия')
    skills01 = models.CharField(max_length=128, blank=True, verbose_name='навыки01')
    skills02 = models.CharField(max_length=128, blank=True, verbose_name='навыки02')
    skills03 = models.CharField(max_length=128, blank=True, verbose_name='навыки03')
    skills04 = models.CharField(max_length=128, blank=True, verbose_name='навыки04')
    skills05 = models.CharField(max_length=128, blank=True, verbose_name='навыки05')
    skills06 = models.CharField(max_length=128, blank=True, verbose_name='навыки06')
    skills07 = models.CharField(max_length=128, blank=True, verbose_name='навыки07')
    skills08 = models.CharField(max_length=128, blank=True, verbose_name='навыки08')
    skills09 = models.CharField(max_length=128, blank=True, verbose_name='навыки09')
    skills10 = models.CharField(max_length=128, blank=True, verbose_name='навыки10')
    education01 = models.TextField(verbose_name='образование01', blank=True)
    education02 = models.TextField(verbose_name='образование02', blank=True)
    education03 = models.TextField(verbose_name='образование03', blank=True)
    education04 = models.TextField(verbose_name='образование04', blank=True)
    education05 = models.TextField(verbose_name='образование05', blank=True)
    education06 = models.TextField(verbose_name='образование06', blank=True)
    education07 = models.TextField(verbose_name='образование07', blank=True)
    education08 = models.TextField(verbose_name='образование08', blank=True)
    education09 = models.TextField(verbose_name='образование09', blank=True)
    education10 = models.TextField(verbose_name='образование10', blank=True)
    is_active = models.BooleanField(default=True, verbose_name='позиция активна', db_index=True)

    def __str__(self):
        return f'{self.short_name}'
