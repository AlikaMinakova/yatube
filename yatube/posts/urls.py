# после ключевого слова в url переход на какие обработчики
from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    # Главная страница
    path('', views.index, name='index'),
    path('group/<slug:slug>/', views.group_posts, name='group_posts'),
# Профайл пользователя
    path('profile/<str:username>/', views.profile, name='profile'),
    # Просмотр записи
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('create/', views.post_create, name='post_create'),
    path('posts/<int:id_post>/edit/', views.post_edit, name='post_edit')
]
