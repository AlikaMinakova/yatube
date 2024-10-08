# главные слова в url адресах после которых переходим в приложение

"""
URL configuration for yatube project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Дорогой Джанго, если запрошена главная страница (''),
    # перейди в файл urls приложения ice_cream и проверь там все пути
    path('', include('posts.urls', namespace='posts')),
    # Встроенная админка в Django подключена по этому адресу «из коробки»
    path('admin/', admin.site.urls),
    # Все адреса с префиксом /auth
    # будут прернаправлены в модуль django.contrib.auth
    path('auth/', include('users.urls', namespace='users')),
    path('auth/', include('django.contrib.auth.urls')),
    path('about/', include('about.urls', namespace='about')),
]

# обработчик страницы с ошибкой, для 403 - в settings.py
handler404 = 'core.views.page_not_found'

#При дефолтных настройках проекта в режиме
# разработчика Django не будет раздавать картинки,
# загруженные пользователями, настроим отображение:
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
