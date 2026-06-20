from django.shortcuts import render, get_object_or_404
from .models import Course, Module, Topic, Quest, Question, Answer

def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug)
    module = course.modules.all()

    return render(request, 'coureses/course_detail.html', {
        'modules': module,
        'course':course
    })

def topic_detail(request, pk):
    module = get_object_or_404(Module, pk=pk)
    topic = module.topics.all()

    return render(request, 'coureses/topic.html', {
        'topics': topic,
        'module': module,
        'course': module.course
    })