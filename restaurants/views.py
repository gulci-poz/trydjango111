from django.shortcuts import render


def home(request):
    title = 'home page'
    context = {'title': title}

    return render(request, 'base.html', context)


def contact(request):
    title = 'contact'
    context = {'title': title}

    return render(request, 'contact.html', context)


def about(request):
    title = 'about'
    context = {'title': title}

    return render(request, 'about.html', context)
