from django.shortcuts import render
from django.urls import resolve


def main(request):
    content = {
        'title': 'главная'
    }
    return render(request, 'mainapp/index.html', content)


def specialists(request):
    links_menu = [
        {'href': 'specialist_tatyana', 'name': 'Татьяна'},
        {'href': 'specialist_svetlana', 'name': 'Светлана'},
        {'href': 'specialist_mariya', 'name': 'Мария'},
        {'href': 'specialist_lidiya', 'name': 'Лидия'},
        {'href': 'specialist_anastasiya', 'name': 'Анастасия'},
    ]
    content = {
        'title': 'специалисты',
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/specialists.html', content)


def contacts(request):
    content = {
        'title': 'контакты'
    }
    return render(request, 'mainapp/contact.html', content)


def specialist_tatyana(request):
    links_menu = [
        {'href': 'specialist_tatyana', 'name': 'Татьяна'},
        {'href': 'specialist_svetlana', 'name': 'Светлана'},
        {'href': 'specialist_mariya', 'name': 'Мария'},
        {'href': 'specialist_lidiya', 'name': 'Лидия'},
        {'href': 'specialist_anastasiya', 'name': 'Анастасия'},
    ]
    content = {
        'title': 'специалисты',
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/specialist_tatyana.html', content)


def specialist_svetlana(request):
    links_menu = [
        {'href': 'specialist_tatyana', 'name': 'Татьяна'},
        {'href': 'specialist_svetlana', 'name': 'Светлана'},
        {'href': 'specialist_mariya', 'name': 'Мария'},
        {'href': 'specialist_lidiya', 'name': 'Лидия'},
        {'href': 'specialist_anastasiya', 'name': 'Анастасия'},
    ]
    content = {
        'title': 'специалисты',
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/specialist_svetlana.html', content)


def specialist_mariya(request):
    links_menu = [
        {'href': 'specialist_tatyana', 'name': 'Татьяна'},
        {'href': 'specialist_svetlana', 'name': 'Светлана'},
        {'href': 'specialist_mariya', 'name': 'Мария'},
        {'href': 'specialist_lidiya', 'name': 'Лидия'},
        {'href': 'specialist_anastasiya', 'name': 'Анастасия'},
    ]
    content = {
        'title': 'специалисты',
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/specialist_mariya.html', content)


def specialist_lidiya(request):
    links_menu = [
        {'href': 'specialist_tatyana', 'name': 'Татьяна'},
        {'href': 'specialist_svetlana', 'name': 'Светлана'},
        {'href': 'specialist_mariya', 'name': 'Мария'},
        {'href': 'specialist_lidiya', 'name': 'Лидия'},
        {'href': 'specialist_anastasiya', 'name': 'Анастасия'},
    ]
    content = {
        'title': 'специалисты',
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/specialist_lidiya.html', content)


def specialist_anastasiya(request):
    links_menu = [
        {'href': 'specialist_tatyana', 'name': 'Татьяна'},
        {'href': 'specialist_svetlana', 'name': 'Светлана'},
        {'href': 'specialist_mariya', 'name': 'Мария'},
        {'href': 'specialist_lidiya', 'name': 'Лидия'},
        {'href': 'specialist_anastasiya', 'name': 'Анастасия'},
    ]
    content = {
        'title': 'специалисты',
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/specialist_anastasiya.html', content)
