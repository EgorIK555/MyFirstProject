from django.shortcuts import render
from dataapp.models import Enemy

def AllEnemiesPage(request):
    allEnemies = Enemy.objects.all()
    pageParams = {"enemies":allEnemies}
    return render(request, "allEnemies.html", pageParams)

def EnemyPage(request):
    allEnemies = Enemy.objects.all()
    print(allEnemies)
    params = {"speed":12,"health":100, "damage":34}
    return render(request, 'enemy.html', params)