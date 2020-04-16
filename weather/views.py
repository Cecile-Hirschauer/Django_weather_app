from django.shortcuts import render

def index(request):
    """return the index.html template"""
    return render(request, 'weather/index.html')
