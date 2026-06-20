from django.shortcuts import render
from .models import Mode

def home (request):
    modes = Mode.objects.all()

    return render(request, "e_learn/strona.html", {
        "modes": modes
    })