from django.shortcuts import render


def home(request):
    user_name = 'gulci'

    return render(request, "base.html", {"user_name": user_name})
