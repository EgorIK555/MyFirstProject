from django.contrib import admin
from django.urls import path

from initialapp import views as initialviews
from dataapp import views as enemyviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', initialviews.HomePage),
    path('enemy/<str:name>', enemyviews.EnemyPage, name="enemy"),
    path('allEnemies/', enemyviews.AllEnemiesPage, name='allenemies')
]
