from django.shortcuts import render, get_object_or_404
from .models import Course, Topic

def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug)
    topic = course.topics.all()

    return render(request, 'coureses/course_detail.html', {
        'topics': topic,
        'course':course
    })

def topic_detail(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    tasks = topic.questions.all()

    return render(request, 'coureses/topic.html', {
        'topics': topic,
        'tasks': tasks
    })