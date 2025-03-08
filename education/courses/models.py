from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from .constants import MAX_LENGTH
from .fields import OrderField


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
    order = OrderField(
        blank=True,
        for_fields=['course'],
        verbose_name='Порядковый номер'
    )
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Модуль'
        verbose_name_plural = 'Модули'
        ordering = ['order']

    def __str__(self):
        return f'{self.order}. {self.title}'


class Content(models.Model):
    module = models.ForeignKey(
        Module,
        related_name='contents',
        on_delete=models.CASCADE
    )
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to={
            'model__in': ('text', 'video', 'image', 'file')
        }
    )
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey(
        'content_type',
        'object_id'
    )
    order = OrderField(
        blank=True,
        for_fields=['module'],
        verbose_name='Порядковый номер'
    )

    class Meta:
        ordering = ['order']


class ItemBase(models.Model):
    owner = models.ForeignKey(
        User,
        related_name='%(class)s_related',
        on_delete=models.CASCADE,
        verbose_name='Автор курса'
    )
    title = models.CharField(
        max_length=MAX_LENGTH,
        verbose_name='Название'
        )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата и время создания'
        )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата и время обновления'
        )

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class Text(ItemBase):
    content = models.TextField()


class File(ItemBase):
    file = models.FileField(upload_to='files')


class Image(ItemBase):
    file = models.FileField(upload_to='images')
