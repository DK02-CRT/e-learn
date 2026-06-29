from django.shortcuts import render
from .models import ResultsTopic, ResultsQuiz

# Create your views here.
def results(request):
    resultsTopic = ResultsTopic
    resultsQuiz = ResultsQuiz

    return render(request, "results/results.html", {
        "resultsTopic": resultsTopic,
        "resultsQuiz": resultsQuiz
    })