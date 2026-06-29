from django.db import models
from django.conf import settings
from quizes.models import Quiz
from coureses.models import Topic

class ResultsQuiz(models.Model):
    users = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="quiz_results"
    )
    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE,
        related_name='quiz_results'
    )
    score = models.IntegerField(default=0)
    max_score = models.IntegerField(default=0)

    started_at = models.DateTimeField()

    duration = models.DurationField()

    class Meta:
        ordering = [
            "-score",
            "duration"
        ]

    def __str__(self):
        return f"{self.users} - {self.quiz}"

class ResultsTopic(models.Model):
    users = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="topic_results"
    )
    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        related_name='topic_results'
    )
    score = models.IntegerField(default=0)
    max_score = models.IntegerField(default=0)

    started_at = models.DateTimeField()

    duration = models.DurationField()

    class Meta:
        ordering = [
            "-score",
            "duration"
        ]

    def __str__(self):
        return f"{self.users} - {self.topic}"