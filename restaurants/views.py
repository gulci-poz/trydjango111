from django.db.models import Q
from django.views.generic import ListView

from .models import RestaurantLocation


class RestaurantListView(ListView):
    def get_queryset(self):
        slug = self.kwargs.get('slug')

        if slug:
            queryset = RestaurantLocation.objects.filter(
                Q(category__iexact=slug) |
                Q(category__icontains=slug)
            )
        else:
            queryset = RestaurantLocation.objects.all()

        return queryset
