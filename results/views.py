from django.shortcuts import render
from .models import ResultsTopic, ResultsQuiz
from django.db.models import Avg, Count


def results(request):
    resultsTopic = ResultsTopic.objects.select_related("users", "topic").order_by("started_at")
    resultsQuiz = ResultsQuiz.objects.select_related("users", "quiz").order_by("started_at")

    topDurationQuiz = ResultsQuiz.objects.filter(
        passed=True
    ).order_by("duration")
    topDurationTopic = ResultsTopic.objects.filter(
        passed=True
    ).order_by("duration")
    bestUsersR = ResultsTopic.objects.values("users__username").annotate(avg=Avg("score")).order_by("-avg")
    bestTimeR = ResultsTopic.objects.values("users__username").annotate(avg_time=Avg("duration")).order_by("-avg_time")
    bestActiveR = ResultsTopic.objects.values("users__username").annotate(total=Count("id")).order_by("-total")

    bestUsersQ = ResultsQuiz.objects.values("users__username").annotate(avg=Avg("score")).order_by("-avg")
    bestTimeQ = ResultsQuiz.objects.values("users__username").annotate(avg_time=Avg("duration")).order_by("-avg_time")
    bestActiveQ = ResultsQuiz.objects.values("users__username").annotate(total=Count("id")).order_by("-total")

    return render(request, "results/results.html", {
        "resultsTopic": resultsTopic,
        "resultsQuiz": resultsQuiz,
        "topDurationQuiz": topDurationQuiz,
        "topDurationTopic": topDurationTopic,
        "bestUsersR": bestUsersR,
        "bestTimeR": bestTimeR,
        "bestActiveR": bestActiveR,
        "bestUsersQ": bestUsersQ,
        "bestTimeQ": bestTimeQ,
        "bestActiveQ": bestActiveQ
    })
