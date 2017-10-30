from django.shortcuts import render


def home(request):
    user_name = 'gulci'
    friends = ['karolcia', 'wiki', 'mela', 'emilka']
    context = {"user_name": user_name, "friends": friends}

    return render(request, "base.html", context)
