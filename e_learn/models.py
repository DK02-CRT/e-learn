from django.db import models

class Mode(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(
        upload_to='e_learn/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name