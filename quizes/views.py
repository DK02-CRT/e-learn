from django.shortcuts import render, get_object_or_404
from .models import Quiz, Quiz_Task, Quiz_Answer
from django.contrib.auth.decorators import login_required
from datetime import timedelta
from results.models import ResultsQuiz
from django.utils import timezone

@login_required
def quizes (request):
    quizes = Quiz.objects.all()

    return render(request, "quizes/quizes.html", {
        "quizes": quizes
    })

@login_required
def quiz_detail (request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    tasks = quiz.quizTasks.all()
    # request.session["quiz_start"] = timezone.now().isoformat()
    
    score = None
    result = ""
    max_score = 0
    time = 0

    if request.method == "POST":
        startTime = timezone.now()
        print(request.POST)
        print(request.POST.getlist("answers"))

        selected_answers = request.POST.getlist("answers")
        print(selected_answers)
        selected_answers = [int(i) for i in selected_answers]
        print(selected_answers)
        time = request.POST.get("time")

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
        ).count()
        if max_score > 0 and (score / max_score) >= 0.8:
            result = "Zaliczono quiz pomyślnie"
        
        else:
            result = "Quiz nie został zaliczony pomyślnie. Proszę spróbować jeszcze raz."

        print(correct_answers.count())
        print(list(correct_answers.values("id", "option")))

        ResultsQuiz.objects.create(
            users=request.user,
            quiz=quiz,
            score=score,
            max_score=max_score,
            started_at=startTime,
            duration=timedelta(seconds=int(time)),
            passed=(score / max_score >= 0.8)
)

    return render(request, "quizes/quiz.html", {
        "max_score": max_score,
        "score": score,
        "quiz": quiz,
        "tasks": tasks,
        "result": result, 
        "time": time
    })