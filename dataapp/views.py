from django.shortcuts import render
from dataapp.models import Enemy

def AllEnemiesPage(request):
    allEnemies = Enemy.objects.all()
    pageParams = {"enemies":allEnemies}
    return render(request, "allEnemies.html", pageParams)

def EnemyPage(request, name):
    print(name)
    params = {"name":"Some name","avatar":"someurl"}
    return render(request, 'enemy.html')