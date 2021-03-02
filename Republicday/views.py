from django.shortcuts import render
import datetime
from django.http import HttpResponse


# Create your views here.

def index(request):
    now = datetime.datetime.now()
    return render(request, "Republicday/index.html", {
        "Republicday": now.month == 7 and now.day == 1
    })
