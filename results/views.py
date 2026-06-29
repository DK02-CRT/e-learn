from django.shortcuts import render
from .models import ResultsTopic, ResultsQuiz

# Create your views here.
def results(request):
    resultsTopic = ResultsTopic.objects.all()
    resultsQuiz = ResultsQuiz.objects.all()

    return render(request, "results/results.html", {
        "resultsTopic": resultsTopic,
        "resultsQuiz": resultsQuiz
    })