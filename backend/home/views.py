from django.shortcuts import render


# Create your views here.
def home_logged(request):
    return render(request, 'home/home_logged.html')


def home_not_logged(request):
    return render(request, 'home/home_not_logged.html')
