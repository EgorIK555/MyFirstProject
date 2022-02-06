from django.contrib import admin
from django.urls import path

from initialapp import views as initialviews
from dataapp import views as enemyviews

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', initialviews.HomePage),
    path('enemy/<str:enemyName>', enemyviews.EnemyPage, name="enemy"),
    path('allEnemies/', enemyviews.AllEnemiesPage, name='allenemies')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
