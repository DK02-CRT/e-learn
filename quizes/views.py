from django.shortcuts import render, get_object_or_404
from .models import Quiz, Quiz_Task, Quiz_Answer

def quizes (request):
    quizes = Quiz.objects.all()

    return render(request, "quizes/quizes.html", {
        "quizes": quizes
    })

def quiz_detail (request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    tasks = quiz.quizTasks.all()
    
    score = None
    max_score = 0

    if request.method == "POST":
        print(request.POST)
        print(request.POST.getlist("answers"))

        selected_answers = request.POST.getlist("answers")
        print(selected_answers)
        selected_answers = [int(i) for i in selected_answers]
        print(selected_answers)

        # wszystkie poprawne odpowiedzi w tym topicu
        correct_answers = Quiz_Answer.objects.filter(
            answer__task=quiz,
            is_correct=True
        )
        print(correct_answers)

        max_score = correct_answers.count()

        score = Quiz_Answer.objects.filter(
            id__in=selected_answers,
            answer__task=quiz,
            is_correct=True
        ).count

        print(correct_answers.count())
        print(list(correct_answers.values("id", "option")))

    return render(request, "quizes/quiz.html", {
        "max_score": max_score,
        "score": score,
        "quiz": quiz,
        "tasks": tasks
    })