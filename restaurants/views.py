from django.shortcuts import render
from django.views import View


def home(request):
    title = 'home page'
    context = {'title': title}

    return render(request, 'base.html', context)


def about(request):
    title = 'about'
    context = {'title': title}

    return render(request, 'about.html', context)


class ContactView(View):
    def get(self, request, *args, **kwargs):
        title = 'contact'
        context = {'title': title, 'id': kwargs['id_contact']}
        return render(request, 'contact.html', context)
