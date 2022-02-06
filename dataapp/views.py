from django.shortcuts import render
from dataapp.models import Enemy

def AllEnemiesPage(request):
    allEnemies = Enemy.objects.all()
    pageParams = {"enemies":allEnemies}
    return render(request, "allEnemies.html", pageParams)

def EnemyPage(request, enemyName):
    allEnemies = Enemy.objects.all().filter(name=enemyName)
    print(enemyName)
    params = {"enemy":allEnemies[0]}
    return render(request, 'enemy.html',params)
     