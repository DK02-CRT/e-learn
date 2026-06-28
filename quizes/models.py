from django.db import models
from coureses.models import Course
from django_ckeditor_5.fields import CKEditor5Field

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
    context = CKEditor5Field()

    def __str__(self):
        return self.context
    
class Quiz_Answer(models.Model):
    answer = models.ForeignKey(
        Quiz_Task,
        on_delete=models.CASCADE,
        related_name='quizAnswers'
    )
    option = CKEditor5Field()
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.option