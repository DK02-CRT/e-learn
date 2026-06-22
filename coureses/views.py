from django.shortcuts import render, get_object_or_404
from .models import Course, Module, Topic, Quest, Question, Answer

def courses(request):
    courses = Course.objects.all()

    return render(request, 'coureses/courses.html', {
        'courses':courses
    })

def module_detail(request,slug, pk):
    module = get_object_or_404(Module, pk=pk)
    topic = module.topics.all()

    return render(request, 'coureses/module.html', {
        'topics': topic,
        'module': module,
        'course': module.course
    })

def topic_detail(request, slug, module_pk, topic_pk):
    topics = get_object_or_404(Topic, pk=topic_pk)
    quests = topics.quests.all()

    score = None
    max_score = 0

    if request.method == "POST":

        selected_answers = request.POST.getlist("answers")
        selected_answers = [int(i) for i in selected_answers]

        # wszystkie poprawne odpowiedzi w tym topicu
        correct_answers = Answer.objects.filter(
            question__question__quest=topics,
            is_correct=True
        )

        max_score = correct_answers.count()

        score = Answer.objects.filter(
            id__in=selected_answers,
            question__question__quest=topics,
            is_correct=True
        ).count()

    return render(request, 'coureses/topic.html', {
        'topics': topics,
        'quests': quests,
        'module': topics.module,
        'course': topics.module.course,
        'score': score,
        'max_score': max_score
    })