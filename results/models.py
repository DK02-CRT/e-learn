from django.db import models
from django.conf import settings
from quizes.models import Quiz

class Results(models.Model):
    users = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="results"
    )
    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE,
        related_name='results'
    )
    score = models.IntegerField(default=0)
    max_score = models.IntegerField(default=0)

    started_at = models.DateTimeField()
    finished_at = models.DateTimeField()

    duration = models.DurationField()

    class Meta:
        ordering = [
            "-score",
            "duration"
        ]

    def __str__(self):
        return f"{self.users} - {self.quiz}"