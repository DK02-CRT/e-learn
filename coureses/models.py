from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.contrib.auth import get_user_model
from django.conf import settings

# model przedmiotu
class Course(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField(max_length=150)
    slug = models.SlugField(unique=True)

    image = models.ImageField(
        upload_to='coureses/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title
    
# model modułu
class Module(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='modules'
    )
    title = models.CharField(max_length=100)
    order = models.PositiveBigIntegerField(default=0)
    content = CKEditor5Field()

    def __str__(self):
        return self.title

# model tematu przedmiotu
class Topic(models.Model):
    module = models.ForeignKey(
        Module,
        on_delete=models.CASCADE,
        related_name='modules'
    )
    title = models.CharField(max_length=100)
    order = models.PositiveBigIntegerField(default=0)
    content = CKEditor5Field()

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title
    
# model pytania
class Quest(models.Model):
    quest = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        related_name='quests'
    )
    content = models.TextField()

    def __str__(self):
        return self.content

# model pytania
class Question(models.Model):
    question = models.ForeignKey(
        Quest,
        on_delete=models.CASCADE,
        related_name='questions'
    )
    content = CKEditor5Field()
    order = models.PositiveBigIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

# model odpowiedzi
class Answer(models.Model):
    question = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE,
        related_name='answers'
    )
    content = CKEditor5Field()
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.content
    
# model procesu usera
class UserProgress(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='progress'
    )
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        related_name='progress'
    )

    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ("user", "lesson")

    def __str__(self):
        return f"{self.user} - {self.lesson} - {self.completed}"


class Result(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='quiz_results'
    )
    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE,
        related_name='results'
    )

    score = models.IntegerField()
    max_score = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)