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
    specialist_education01 = specialist01.spec_education.all()
    specialist_skills01 = specialist01.skills.all()
    content = {
        'title': 'специалисты',
        'links_menu': get_links_menu(),
        'specialist01': specialist01,
        'specialist_education': specialist_education01,
        'specialist_skills': specialist_skills01,
    }
    return render(request, 'mainapp/specialists.html', content)


def specialist(request, pk=None):
    specialist = Specialist.objects.get(pk=pk)
    specialist_education = specialist.spec_education.all()
    specialist_skills = specialist.skills.all()
    content = {
        'title': f'специалист {specialist.short_name}',
        'links_menu': get_links_menu(),
        'specialist': specialist,
        'specialist_education': specialist_education,
        'specialist_skills': specialist_skills,
    }
    return render(request, 'mainapp/specialist.html', content)


def contacts(request):
    content = {
        'title': 'контакты'
    }
    return render(request, 'mainapp/contact.html', content)
