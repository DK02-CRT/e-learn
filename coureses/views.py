from django.shortcuts import render, get_object_or_404
from .models import Course, Module, Topic, Question
from django.contrib.auth.decorators import login_required
from results.models import ResultsTopic
from django.utils import timezone
from datetime import timedelta


@login_required
def courses(request):

    courses = Course.objects.all()

    return render(request, 'coureses/courses.html', {
        'courses': courses
    })


@login_required
def module_detail(request,  pk):
    module = get_object_or_404(Module, pk=pk)
    topic = module.topics.all()

    return render(request, 'coureses/module.html', {
        'topics': topic,
        'module': module,
        'course': module.course
    })


@login_required
def topic_detail(request, module_pk, topic_pk):
    print("🔥 WIDOK DZIAŁA", flush=True)
    topic = get_object_or_404(Topic, pk=topic_pk)
    quests = topic.quests.all()

    score = 0
    result = ""
    max_score = 0
    time = 0
    questions_data = []
    questions = Question.objects.filter(question__quest=topic)

    for question in questions:
        questions_data.append({
            "question": question,
            "answers": question.answers.order_by("?"),
        })

    if request.method == "POST":
        startTime = timezone.now()
        print("dane")
        print("POST:", request.POST)
        print("TIME:", request.POST.get("time"))
        time = request.POST.get("time")

        for question in questions:
            max_score = max_score + 1

            correct = set(
                question.answers.filter(is_correct=True)
                .values_list("id", flat=True)
            )

            selected = set(
                map(
                    int,
                    request.POST.getlist(f"question_{question.id}")
                )
            )
            print(correct)
            print(selected)
            if selected == correct:
                score = score + 1

            print(score)
        if max_score > 0 and (score / max_score) >= 0.75:
            result = "Zaliczono temat pomyślnie"

        else:
            result = "Temat nie został zaliczony pomyślnie. Proszę spróbować jeszcze raz."

        ResultsTopic.objects.create(
            users=request.user,
            topic=topic,
            score=score,
            max_score=max_score,
            started_at=startTime,
            duration=timedelta(seconds=int(time)),
            passed=(score / max_score >= 0.75)
        )
    return render(request, 'coureses/topic.html', {
        'topics': topic,
        'quests': quests,
        'module': topic.module,
        'course': topic.module.course,
        'score': score,
        'max_score': max_score,
        "result": result,
        "time": time,
        "questions_data": questions_data,
    })
