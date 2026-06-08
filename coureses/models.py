from django.db import models
from ckeditor.fields import RichTextField

# model przedmiotu
class Course(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField(max_length=150)
    # slug = models.SlugField(unique=True)
    slug = models.SlugField(blank=True, null=True)

    image = models.ImageField(
        upload_to='coureses/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title

# model tematu przedmiotu
class Topic(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='topics'
    )
    title = models.CharField(max_length=100)
    content = RichTextField()

    def __str__(self):
        return self.title
    
# model pytania
class Question(models.Model):
    question = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        related_name='questions'
    )
    content = models.TextField()

    def __str__(self):
        return self.content
    
# model odpowiedzi
class Answer(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='answers'
    )
    content = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.content