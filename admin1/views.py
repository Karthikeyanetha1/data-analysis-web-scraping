from builtins import next
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
import csv
import io
import xlrd
import xlwt
from io import TextIOWrapper

from requests import get
from requests.exceptions import RequestException
from bs4 import BeautifulSoup

# ------------------------------------
# ✅ HOME PAGE VIEW (FIXES YOUR ERROR)
# ------------------------------------
def index(request):
    return render(request, "index.html")

# ------------------------------------
# ADMIN LOGIN
# ------------------------------------
def adminlogin(request):
    print("hello admin")
    return render(request, "admin/adminlogin.html")

# ------------------------------------
# LOGOUT
# ------------------------------------
def logout(request):
    return render(request, "index.html")

# ------------------------------------
# ADMIN LOGIN ENTERED
# ------------------------------------
def adminloginentered(request):
    if request.method == "POST":
        uname = request.POST['name']
        passwd = request.POST['pwd']
        if uname == 'admin' and passwd == 'admin':
            return render(request, "admin/adminloginentered.html")
        else:
            return HttpResponse("Invalid credentials")
    return render(request, "admin/adminloginentered.html")

# ------------------------------------
# ACTIVATE USER
# ------------------------------------
def activateuser(request):
    if request.method == "GET":
        pid = request.GET.get("pid")
        status = request.GET.get("status")
        from user.models import userdetails
        userdetails.objects.filter(id=pid).update(status=status)
        return render(request, "admin/userdetails.html", {"qs": userdetails.objects.all()})

# ------------------------------------
# USER DETAILS
# ------------------------------------
def userdetails(request):
    from user.models import userdetails
    qs = userdetails.objects.all()
    return render(request, "admin/userdetails.html", {"qs": qs})

# ------------------------------------
# STORE CSV DATA
# ------------------------------------
def storecsvdata(request):
    if request.method == "POST":
        name = request.POST.get('name')
        csvfile = TextIOWrapper(request.FILES['file'], encoding='utf-8')
        reader = csv.reader(csvfile)

        for row in reader:
            data = {
                "Date": row[0],
                "Codeword": row[1],
                "Temp": row[2],
                "Weather": row[3],
                "Traffic": row[4],
            }
            print(data)

    return render(request, "admin/storecsvdata.html")

# ------------------------------------
# SCRAPING PAGE
# ------------------------------------
def scrapping(request):
    return render(request, "admin/scrapping.html")













