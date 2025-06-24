from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from posts.models import Post, Group

User = get_user_model()


class PostFormTests(TestCase):
    def setUp(self):
        # Создаём пользователя и логинимся
        self.user = User.objects.create_user(username='TestUser')
        self.client.force_login(self.user)

        # Создаём группу, если она используется
        self.group = Group.objects.create(
            title='Test group',
            slug='test-group',
            description='Test description'
        )

    def test_create_post_valid_data(self):
        """Проверка создания поста при валидных данных."""
        posts_count = Post.objects.count()

        form_data = {
            'text': 'Текст нового поста',
            'group': self.group.id,
        }

        response = self.client.post(
            reverse('posts:post_create'),
            data=form_data,
            follow=True
        )

        self.assertRedirects(
            response,
            reverse('posts:profile', kwargs={'username': self.user.username})
        )
        self.assertEqual(Post.objects.count(), posts_count + 1)
        new_post = Post.objects.latest('pub_date')
        self.assertEqual(new_post.text, form_data['text'])
        self.assertEqual(new_post.group, self.group)
        self.assertEqual(new_post.author, self.user)