from django.db import models


class Mode(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(
        upload_to='e_learn/',
        blank=True,
        null=True
    )
    url = models.CharField(max_length=50)
    order = models.PositiveBigIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name
