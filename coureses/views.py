from django.shortcuts import render, get_object_or_404
from .models import Course, Module, Topic, Quest, Question, Answer

def courses(request):
    courses = Course.objects.all()

    return render(request, 'coureses/courses.html', {
        'courses':courses
    })

def topic_detail(request, pk):
    module = get_object_or_404(Module, pk=pk)
    topic = module.topics.all()

    return render(request, 'coureses/topic.html', {
        'topics': topic,
        'module': module,
        'course': module.course
    })