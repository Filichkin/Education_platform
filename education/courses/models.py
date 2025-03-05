from django.contrib.auth.models import User
from django.db import models

from .constants import MAX_LENGTH


class Subject(models.Model):
    title = models.CharField(
        max_length=MAX_LENGTH,
        verbose_name='Название предмета'
    )
    slug = models.SlugField(
        max_length=MAX_LENGTH,
        unique=True,
        verbose_name='Слаг предмета'
    )

    class Meta:
        ordering = ['title']
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

    def __str__(self):
        return self.title


class Course(models.Model):
    owner = models.ForeignKey(
        User,
        related_name='courses_created',
        on_delete=models.CASCADE,
        verbose_name='Автор курса'
    )
    subject = models.ForeignKey(
        Subject,
        related_name='courses',
        on_delete=models.CASCADE,
        verbose_name='Предмет курса'
    )
    title = models.CharField(
        max_length=MAX_LENGTH,
        verbose_name='Название курса'
    )
    slug = models.SlugField(
        max_length=MAX_LENGTH,
        unique=True,
        verbose_name='Слаг курса'
    )
    overview = models.TextField(
        verbose_name='Краткий обзор'
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата и время создания'
        )

    class Meta:
        ordering = ['-created']
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return self.title
    

class Module(models.Model):
    course = models.ForeignKey(
        Course,
        related_name='modules',
        on_delete=models.CASCADE,
        verbose_name='Курс модуля'
    )
    title = models.CharField(
        max_length=MAX_LENGTH,
        verbose_name='Название модуля'
    )
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Модуль'
        verbose_name_plural = 'Модули'

    def __str__(self):
        return self.title
    

