from rest_framework import serializers

from posts.models import Comment, Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('text', 'pub_date', 'author')


# сериализатор для модели Comment для получения модели после API запроса
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        # Указываем поля модели, с которыми будет работать сериализатор;
        # поля модели, не указанные в перечне, сериализатор будет игнорировать.
        # Для перечисления полей можно использовать список или кортеж.
        fields = ('id', 'post', 'author', 'text', 'created')
