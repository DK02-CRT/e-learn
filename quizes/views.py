from django.shortcuts import render, get_object_or_404
from .models import Quiz, Quiz_Task

def quizes (request):
    quizes = Quiz.objects.all()

    return render(request, "quizes/quizes.html", {
        "quizes": quizes
    })

def quiz_detail (request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    tasks = quiz.quizTasks.all()
    # answers = tasks.quizAnswers.all()

    return render(request, "quizes/quiz.html", {
        "quiz": quiz,
        "tasks": tasks,
        # "answers": answers
    })