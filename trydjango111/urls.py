from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView

from restaurants.views import (
    RestaurantListView,
    RestaurantDetailView,
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='base.html')),
    url(r'^contact/$', TemplateView.as_view(template_name='contact.html')),
    url(r'^about/$', TemplateView.as_view(template_name='about.html')),
    url(r'^restaurants/$', RestaurantListView.as_view()),
    url(r'^restaurants/(?P<rest_id>\w+)/$', RestaurantDetailView.as_view()),
    url(r'^restaurants/search/category/(?P<slug>\w+)/$', RestaurantListView.as_view()),
]
