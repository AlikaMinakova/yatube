from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'posts'  # для namespace в yatube/urls.py

urlpatterns = [
    # Главная страница
    path('', views.index, name='index'),  # name - для доступа к адресам из шаблонов
    # Страница со списком сообществ,
    path('group/<slug:slug>', views.group_posts, name='group_list'),
    path('justpage/', views.AuthorPage.as_view(), name='author_page'),
    # Профайл пользователя
    path('profile/<str:username>/', views.profile, name='profile'),
    # Просмотр записи
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('create/', views.post_create, name='post_create'),
    path('posts/<int:post_id>/edit/', views.post_edit, name='post_edit'),

    path('posts/<int:post_id>/comment', views.add_comment, name='add_comment'),

    path('api/v1/posts/', views.api_get_post, name='api_get_post'),
    path('api/v1/posts/<int:post_id>', views.api_posts_details, name='api_posts_details'),
]

# в режиме DEBAG=True фото не отображаются, это условие поможет обойти это ограничение
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
