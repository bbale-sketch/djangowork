from django.shortcuts import render
import datetime
from django.http import HttpResponse

# Create your views here.

def index(request):
    now = datetime.datetime.now()
    return render(request, "independence/index.html", {
        "independence": now.month == 3 and now.day == 6
    })