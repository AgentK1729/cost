from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from forms import *
from django.contrib.auth.models import User
from django.conf import settings
from geolocation.google_maps import GoogleMaps
from models import *
from django.conf import settings
import os
from django.core.mail import EmailMessage

class Wish(object):
    def __init__(self, user, item, store):
        self.user = user
        self.item = item
        self.store = store

def nothing(request):
	return HttpResponseRedirect("/shopping/home/")

def signup(request):
	if request.method == "GET":
		form = SignupForm()
		return render(request, "shopping_signup.html", {'form':form})
	else:
		try:
			u = User.objects.get(username=request.POST['username'])
			error = "User already exists. Please log in to continue"
			return render(request, "shopping_signup.html", {'error':error})
		except User.DoesNotExist:
			if request.POST['password'] == request.POST['confirm']:
							User(username=request.POST['username'], password=request.POST['password'], email=request.POST['email']).save()
							EmailMessage('Welcome to COST', 'Hey %s! Congratulations on joining COST! We hope to make your shopping experience more efficient. Welcome to the family!'%request.POST['username'], to=[request.POST['email']]).send()
							error = "Successfully signed up. Please log in to continue"
							return render(request, "shopping_signup.html", {'error':error})

def home(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, "shopping_home.html", {'form':form})
    elif request.method == "POST":
        u = User.objects.get(username = request.POST['username'])
        if u.password == request.POST['password']:
            request.session['user'] = request.POST['username']
            return HttpResponseRedirect("/shopping/profile")
        else:
            return render(request, "shopping_home.html", {'error':'Either the username or the password is incorrect', 'form':LoginForm(), 'STATIC_URL':settings.STATIC_URL})


def profile(request):
    u = User.objects.get(username=request.session['user'])
    wishlist = [Wish(u.username, i.item, i.store) for i in Item.objects.filter(user=u)]
    stores = ['Walmart', 'JCPenney']
    users = User.objects.all().exclude(username=request.session['user'])
    addsend = [a.address for a in PickupLocation.objects.filter(user=u)]
    google_maps = GoogleMaps(api_key='AIzaSyC8hihi26xJqO77v4R2qJMii0cn6S2eW8w')
    userwishlist = []
    for user in users:
    	addrec = []
    	addr = PickupLocation.objects.filter(user=user)
    	for a in addr:
    		addrec.append(a.address)
    	
    	items = google_maps.distance(addrec, addsend).all()
    	for item in items:
    		if item.distance.miles <= 10:
    			userwishlist.append(Wish(i.user, i.item, i.store) for i in Item.objects.filter(user=user))
    			break
    	
    userwishlist = [Wish(i.user, i.item, i.store) for i in Item.objects.all().exclude(user=u)]
    mywishlist = [Wish(i.receiver, i.item, i.store) for i in UserItem.objects.filter(buyer=u)]
    try:
    	locs = PickupLocation.objects.filter(user=u)
    except:
    	locs = []
    c = {'STATIC_URL':settings.STATIC_URL, 'user':request.session['user'], 'wishlist':wishlist, 'mywishlist':mywishlist, 'userwishlist':userwishlist, 'stores':stores, 'locs':locs}
    return render(request, "shopping_profile.html", c)

def populate(request):
    u = User.objects.get(username=request.session['user'])
    i = Item.objects.create(user=u, item=request.GET['item'], store=request.GET['store'])
    i.save()
    return HttpResponseRedirect("/shopping/profile")

def obtained(request):
    u = User.objects.get(username=request.session['user'])
    try:
    	Item.objects.get(user=u, item=request.GET['item'], store=request.GET['store']).delete()
    except:
    	UserItem.objects.get(buyer=u, item=request.GET['item'], store=request.GET['store']).delete()
    return HttpResponseRedirect("/shopping/profile")

def getThat(request):
    u = User.objects.get(username=request.session['user'])
    UserItem(buyer=u, receiver=request.GET['receiver'], item=request.GET['item'], store=request.GET['store']).save()
    return HttpResponseRedirect("/shopping/profile")
	
	
# AIzaSyC8hihi26xJqO77v4R2qJMii0cn6S2eW8w
def setLocation(request):
	if request.method == "GET":
		return render(request, "shopping_location.html")
	elif request.method == "POST":
		google_maps = GoogleMaps(api_key='AIzaSyC8hihi26xJqO77v4R2qJMii0cn6S2eW8w') 
		location = google_maps.search(location=request.POST['address'])
		my = location.first()
		u = User.objects.get(username=request.session['user'])
		PickupLocation(user=u, address="%s %s %s %s" % (my.street_number, my.route, my.city, my.postal_code)).save()
		return HttpResponseRedirect("/shopping/profile")


def picture(request):
	pic = open(os.path.join(settings.BASE_DIR, 'cost/static/%s.jpg'%request.session['user']), 'w')
	for i in request.FILES['pic']:	
		pic.write(i)
	return HttpResponseRedirect("/shopping/profile")
	
def logout(request):
	try:
		del request.session['user']
	except:
		pass
	return HttpResponseRedirect("/shopping/home/")
