from django.contrib.auth import get_user_model
from django.test import TestCase, Client

from posts.models import Group, Post

User = get_user_model()


class TaskURLTests(TestCase):
    @classmethod
    def setUpClass(cls):
        # Создадим запись в БД для проверки доступности адреса task/test-slug/
        super().setUpClass()
        cls.user = User.objects.create_user(username='leo')
        cls.group = Group.objects.create(
            title='Тестовая группа',
            slug='test',
            description='Тестовое описание',
        )
        cls.post = Post.objects.create(
            id=1,
            author=cls.user,
            group=cls.group,
            text='Текст поста',
        )

    def setUp(self):
        # Создаем неавторизованный клиент
        self.guest_client = Client()
        # Создаем авторизованый клиент
        self.user = User.objects.create_user(username='StasBasov')
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    # Проверяем общедоступные страницы
    def test_home_url_exists_at_desired_location(self):
        """Страница / доступна любому пользователю."""
        response = self.guest_client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_task_added_url_exists_at_desired_location(self):
        """Страница /added/ доступна любому пользователю."""
        response = self.guest_client.get('/group/test')
        self.assertEqual(response.status_code, 200)

    def test_task_added_url_exists_at_desired_location2(self):
        """Страница доступна любому пользователю."""
        response = self.authorized_client.get('/justpage/')
        self.assertEqual(response.status_code, 200)

    def test_task_list_url_exists_at_desired_location(self):
        response = self.guest_client.get('/profile/StasBasov/')
        self.assertEqual(response.status_code, 200)

    def test_task_list_url_exists_at_desired_location2(self):
        response = self.guest_client.get('/posts/1/')
        self.assertEqual(response.status_code, 200)

    # Проверяем доступность страниц для авторизованного пользователя

    def test_task_list_url_exists_at_desired_location4(self):
        """Страница  доступна только авторизованному пользователю."""
        response = self.guest_client.get('/create/')
        self.assertEqual(response.status_code, 302)

    def test_task_list_url_exists_at_desired_location5(self):
        """Страница  доступна только авторизованному пользователю."""
        response = self.authorized_client.get('/create/')
        self.assertEqual(response.status_code, 200)

    def test_task_list_url_exists_at_desired_location3(self):
        """Страница  доступна только авторизованному автору этого поста."""
        response = self.authorized_client.get('/posts/1/edit/')
        self.assertEqual(response.status_code, 302)

    def test_task_list_url_exists_at_desired_location7(self):
        """Страница  доступна только авторизованному автору этого поста."""
        response = self.guest_client.get('/posts/1/edit/')
        self.assertEqual(response.status_code, 302)

    def test_post_edit_available_for_author(self):
        """Страница /posts/1/edit/ доступна автору поста."""
        # Автор — тот, кто создал пост в setUpClass
        author_client = Client()
        author_client.force_login(self.post.author)
        response = author_client.get('/posts/1/edit/')
        self.assertEqual(response.status_code, 200)

    # Проверка вызываемых шаблонов для каждого адреса
    def test_urls_uses_correct_template(self):
        """URL-адрес использует соответствующий шаблон."""
        templates_url_names = {
            'posts/index.html': '/',
            'posts/profile.html': '/profile/StasBasov/',
            'posts/group_list.html': '/group/test',
        }
        for template, url in templates_url_names.items():
            with self.subTest(url=url):
                response = self.authorized_client.get(url)
                self.assertTemplateUsed(response, template)
