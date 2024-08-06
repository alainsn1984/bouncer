from django.shortcuts import render


def landing(request):
    """Rending the landing page"""
    return render(request, 'bouncer/index.html')