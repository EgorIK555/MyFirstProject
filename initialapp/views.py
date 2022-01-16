from django.shortcuts import render

def HomePage(request):
    print("tst")
    return render(request, 'index.html')