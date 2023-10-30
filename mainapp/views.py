from django.shortcuts import render


def main(request):
    content = {
        'title': 'главная'
    }
    return render(request, 'mainapp/index.html', content)


def specialists(request):
    links_menu = [
        {'href': 'specialists_all', 'name': 'Все специалисты'},
        {'href': 'specialists_svetlana', 'name': 'Светлана'},
        {'href': 'specialists_mariya', 'name': 'Мария'},
        {'href': 'specialists_lidiya', 'name': 'Лидия'},
        {'href': 'specialists_anastasiya', 'name': 'Анастасия'},
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


def specialists_all(request):
    links_menu = [
        {'href': 'specialists_all', 'name': 'Все специалисты'},
        {'href': 'specialists_svetlana', 'name': 'Светлана'},
        {'href': 'specialists_mariya', 'name': 'Мария'},
        {'href': 'specialists_lidiya', 'name': 'Лидия'},
        {'href': 'specialists_anastasiya', 'name': 'Анастасия'},
    ]
    content = {
        'title': 'специалисты',
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/specialists.html', content)


def specialists_svetlana(request):
    links_menu = [
        {'href': 'specialists_all', 'name': 'Все специалисты'},
        {'href': 'specialists_svetlana', 'name': 'Светлана'},
        {'href': 'specialists_mariya', 'name': 'Мария'},
        {'href': 'specialists_lidiya', 'name': 'Лидия'},
        {'href': 'specialists_anastasiya', 'name': 'Анастасия'},
    ]
    content = {
        'title': 'специалисты',
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/specialists.html', content)


def specialists_mariya(request):
    links_menu = [
        {'href': 'specialists_all', 'name': 'Все специалисты'},
        {'href': 'specialists_svetlana', 'name': 'Светлана'},
        {'href': 'specialists_mariya', 'name': 'Мария'},
        {'href': 'specialists_lidiya', 'name': 'Лидия'},
        {'href': 'specialists_anastasiya', 'name': 'Анастасия'},
    ]
    content = {
        'title': 'специалисты',
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/specialists.html', content)


def specialists_lidiya(request):
    links_menu = [
        {'href': 'specialists_all', 'name': 'Все специалисты'},
        {'href': 'specialists_svetlana', 'name': 'Светлана'},
        {'href': 'specialists_mariya', 'name': 'Мария'},
        {'href': 'specialists_lidiya', 'name': 'Лидия'},
        {'href': 'specialists_anastasiya', 'name': 'Анастасия'},
    ]
    content = {
        'title': 'специалисты',
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/specialists.html', content)


def specialists_anastasiya(request):
    links_menu = [
        {'href': 'specialists_all', 'name': 'Все специалисты'},
        {'href': 'specialists_svetlana', 'name': 'Светлана'},
        {'href': 'specialists_mariya', 'name': 'Мария'},
        {'href': 'specialists_lidiya', 'name': 'Лидия'},
        {'href': 'specialists_anastasiya', 'name': 'Анастасия'},
    ]
    content = {
        'title': 'специалисты',
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/specialists.html', content)
