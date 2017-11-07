from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='base.html')),
    url(r'^contact/$', TemplateView.as_view(template_name='contact.html')),
    url(r'^about/$', TemplateView.as_view(template_name='about.html')),
]
