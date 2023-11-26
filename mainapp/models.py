from django.db import models


class Skill(models.Model):
    skill = models.CharField(max_length=256, blank=True, verbose_name='навыки')

    def __str__(self):
        return f'{self.skill}'


class Education(models.Model):
    education = models.TextField(blank=True, verbose_name='образование')

    def __str__(self):
        return f'{self.education}'


class Specialist(models.Model):
    short_name = models.CharField(max_length=64, unique=True, verbose_name='имя')
    full_name = models.CharField(max_length=128, unique=True, verbose_name='полное имя')
    image = models.ImageField(upload_to='specialists_photos', blank=True, verbose_name='фото')
    tel = models.CharField(max_length=32, verbose_name='телефон')
    profession = models.CharField(max_length=128, blank=True, verbose_name='профессия')
    skills = models.ManyToManyField(Skill, blank=True, verbose_name='навык специалиста')
    spec_education = models.ManyToManyField(Education, verbose_name='образование специалиста', blank=True)
    is_active = models.BooleanField(default=True, verbose_name='позиция активна', db_index=True)

    def __str__(self):
        return f'{self.short_name}'
