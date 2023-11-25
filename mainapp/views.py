from django.shortcuts import render
from mainapp.models import Specialist


def get_links_menu():
    return Specialist.objects.all()


def main(request):
    title = 'главная'
    specialists = Specialist.objects.all()
    content = {'title': title, 'specialists': specialists}
    return render(request, 'mainapp/index.html', content)


def specialists(request):
    specialist01 = Specialist.objects.get(pk=1)
    content = {
        'title': 'специалисты',
        'links_menu': get_links_menu(),
        'specialist01': specialist01,
    }
    return render(request, 'mainapp/specialists.html', content)


def specialist(request, pk=None):
    specialist = Specialist.objects.get(pk=pk)
    content = {
        'title': 'специалист',
        'links_menu': get_links_menu(),
        'specialist': specialist,
    }
    return render(request, 'mainapp/specialist.html', content)


def contacts(request):
    content = {
        'title': 'контакты'
    }
    return render(request, 'mainapp/contact.html', content)
