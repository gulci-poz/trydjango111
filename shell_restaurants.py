from restaurants.models import RestaurantLocation

restaurants = RestaurantLocation.objects.all()

for restaurant in restaurants:
    print(restaurant)

restaurants.filter(category__iexact='italian')

restaurants.update(category='polish')

new_restaurant = RestaurantLocation()
new_restaurant.name = 'Forza'
new_restaurant.location = 'Poznań, Dworska'
new_restaurant.category = 'Italian'
new_restaurant.save()

print(new_restaurant.timestamp)
print(new_restaurant.updated)

restaurants_italian = RestaurantLocation.objects.filter(category__iexact='italian')

for restaurant in restaurants_italian:
    print(restaurant)

restaurants.exists()
restaurants.count()

restaurants_italian.exists()
restaurants_italian.count()

new_restaurant = RestaurantLocation.objects.create(name='Tivoli', location='Poznań, Naramowicka', category='Italian')
print(new_restaurant.timestamp)

restaurants_qs = RestaurantLocation.objects.filter(category__iexact='italian').exclude(name__icontains='ll')
