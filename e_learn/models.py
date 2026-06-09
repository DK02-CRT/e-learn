from django.db import models
from coureses.models import Course
# from django.contrib.auth.models import Users

class Lesson(models.Model):
    title = models.CharField(max_length=200)
    # students = models.ManyToManyField(User)
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title