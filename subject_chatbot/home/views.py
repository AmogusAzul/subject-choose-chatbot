from django.shortcuts import render

def landing_view(request):

    return render(request, 'home/landing.html')

def about_view(request):

    return render(request, 'home/about.html')

# Create your views here.
