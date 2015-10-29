from django.conf.urls import patterns, url
import views

urlpatterns = patterns('shopping.views',

    url(r'^home/', views.home),

    url(r'^profile/', views.profile),

    url(r'^obtained/', views.obtained),

    url(r'^populate/', views.populate),

    url(r'^getthat/', views.getThat),
    
    url(r'^cantgetthat/', views.cantGetThat),
    
    url(r'^setlocation/', views.setLocation),
    
    url(r'^picture/', views.picture),
    
    url(r'^logout/', views.logout),
    
    url(r'^signup/', views.signup),
    
    url(r'^feedback/', views.feedback),

)
