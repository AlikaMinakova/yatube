import uuid

from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Group(models.Model):
    title = models.TextField()
    slug = models.SlugField()
    description = models.TextField()

    def __str__(self):
        return self.title


class Post(models.Model):
    id = models.IntegerField(primary_key=True)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    # 1. models.ForeignKey - ссылка на таблицу User
    # 2. models.CASCADE - если удалить пользователя, удалятся его посты
    # 3. related_name='posts': в каждом объекте модели User автоматически будет создано свойство
    # с таким же названием (posts), и в нём будут храниться ссылки на все объекты модели Post,
    # которые ссылаются на объект User в таблице User
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    image = models.ImageField(
        'Картинка',
        upload_to='posts/',  # media/posts
        blank=True
    )

    # Аргумент upload_to указывает директорию,
    # в которую будут загружаться пользовательские файлы.

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.text


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comment'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comment'
    )
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)


