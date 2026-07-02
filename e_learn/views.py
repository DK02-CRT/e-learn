from django.shortcuts import render
from .models import Mode
from django.http import HttpResponse

def home (request):
    modes = Mode.objects.all()

    return render(request, "e_learn/strona.html", {
        "modes": modes
    })

def health_check (request):
    return HttpResponse("OK")