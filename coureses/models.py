from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

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
        related_name='topics'
    )
    title = models.CharField(max_length=100)
    order = models.PositiveBigIntegerField(default=0)
    content = CKEditor5Field('Content', config_name='extends')

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
    content = CKEditor5Field('Content', config_name='extends')
    order = models.PositiveBigIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.content

# model odpowiedzi


class Answer(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='answers'
    )
    content = CKEditor5Field('Content', config_name='extends')
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.content
