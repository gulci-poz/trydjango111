import datetime

from django.shortcuts import render


def home(request):
    user_name = 'gulci'
    title = 'hello'
    friends = ['karolcia', 'wiki', 'mela', 'emilka']
    context = {'user_name': user_name, 'title': title, 'friends': friends}

    return render(request, 'base.html', context)


def page(request):
    title = 'a page'
    day = datetime.datetime.now
    context = {'title': title, 'day': day}

    return render(request, 'page.html', context)
