from django.shortcuts import render
from .models import Results

# Create your views here.
def results(request):
    result = Results
    # tasks = quiz.quizTasks.all()
    # answers = tasks.quizAnswers.all()

    return render(request, "results/results.html", {
        "results": result,
        # "tasks": tasks,
        # "answers": answers
    })