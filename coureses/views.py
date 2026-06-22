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

    return render(request, 'coureses/topic.html', {
        'topics': topics,
        'quests': quests,
        'module': topics.module,
        'course': topics.module.course
    })