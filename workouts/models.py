from django.db import models

class Exercise(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    title2 = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    image = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return f'Exercises [title={self.title}]'