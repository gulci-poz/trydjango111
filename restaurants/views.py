from django.http import HttpResponse


def home(request):
    user_name = 'gulci'

    html_template = f'''
    <!doctype html>
    <html>
    <head>
    <title>hello</title>
    </head>
    <body>
    <p>hello {user_name}</p>
    </body>
    </html>
    '''

    return HttpResponse(html_template)
