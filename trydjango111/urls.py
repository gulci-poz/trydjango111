from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView

from restaurants.views import HomeView, AboutView, ContactView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view()),
    url(r'^contact/$', ContactView.as_view()),
    url(r'^about/$', AboutView.as_view()),
    # if we don't add anything to the context,
    # we don't have define the view explicite in views.py
    url(r'^test/$', TemplateView.as_view(template_name='test.html'))
]
