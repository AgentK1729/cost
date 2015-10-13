from geolocation.google_maps import GoogleMaps

address = "4804 Grenville Square Arbutus"

google_maps = GoogleMaps(api_key='AIzaSyC8hihi26xJqO77v4R2qJMii0cn6S2eW8w') 

location = google_maps.search(location=address) # sends search to Google Maps.

my_location = location.first() # returns only first location.
print(my_location.city)
print(my_location.route)
print(my_location.street_number)
print(my_location.postal_code)
