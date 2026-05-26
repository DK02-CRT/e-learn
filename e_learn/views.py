from django.shortcuts import render

def home(request):
    return render(request, 'e_learn/strona.html')