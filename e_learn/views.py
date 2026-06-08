from django.shortcuts import render
from .models import Course
from django.http import HttpResponse

def home (request):
    courses = Course.objects.all()

    return render(request, "e_learn/strona.html", {
        "courses": courses
    })