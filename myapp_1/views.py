from django.shortcuts import render

# Create your views here.

def main_page(request):
    return render(request, 'index.html')


def about_as(request):
    return render(request, 'about.html')

#можно добавить бизнес логику проекта


def contact(request):
    return render(request, 'contact.html')

def what(request):
    return render(request, 'what.html')