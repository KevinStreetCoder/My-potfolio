from django.shortcuts import render


def geeks(request):
    return render(request, 'base.html')
