from django.db import models
from coureses.models import Course

class Quiz(models.Model):
    course = models.OneToOneField(
        Course,
        on_delete=models.CASCADE,
        related_name='quizes'
    )
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Quiz_Task(models.Model):
    task = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE,
        related_name='quizTasks'
    )
    context = models.CharField(max_length=200)

    def __str__(self):
        return self.context
    
class Quiz_Answer(models.Model):
    answer = models.ForeignKey(
        Quiz_Task,
        on_delete=models.CASCADE,
        related_name='quizAnswers'
    )
    option = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.option