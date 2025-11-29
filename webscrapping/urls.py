from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from admin1 import views as admin1
from user import views as user
from newsApp import views as news
from core import views as weather

urlpatterns = [
    # Django Admin Panel
    path('admin/', admin.site.urls),

    # ---------- MAIN HOME URL ----------
    path('', admin1.index, name='home'),
    path('index/', admin1.index, name='index'),

    # ---------- ADMIN ----------
    path('admn1/', admin1.admn1, name='admn1'),
    path('userdetails/', admin1.userdetails, name='userdetails'),
    path('adminloginentered/', admin1.adminloginentered, name='adminloginentered'),
    path('activateuser/', admin1.activateuser, name='activateuser'),
    path('storecsvdata/', admin1.storecsvdata, name='storecsvdata'),
    path('scrapping/', admin1.scrapping, name='scrapping'),
    path('logout/', admin1.logout, name='logout'),

    # ---------- USER ----------
    path('user/', user.userlogin, name='user'),
    path('userpage/', user.userpage, name='userpage'),
    path('userregister/', user.userregister, name='userregister'),
    path('userlogincheck/', user.userlogincheck, name='userlogincheck'),
    path('search/', user.search, name='search'),
    path('searchresult/', user.searchresult, name='searchresult'),
    path('wbscrapp/', user.wbscrapp, name='wbscrapp'),
    path('fpkart/', user.fpkart, name='fpkart'),
    path('jobsearch/', user.jobsearch, name='jobsearch'),

    # ---------- NEWS ----------
    path('nnews/', news.nindex, name='nnews'),

    # ---------- WEATHER ----------
    path('weather/', weather.home, name='weather'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
