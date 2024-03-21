from django.db import models

class Exercise(models.Model):
    BACK_TRAINING = 'back_training'
    CHEST_TRAINING = 'chest_training'
    BICEPS_TRAINING = 'biceps_training'
    TRICEPS_TRAINING = 'triceps_training'
    LEG_TRAINING = 'leg_training'
    GLUTE_TRAINING = 'glute_training'
    SHOULDER_TRAINING = 'shoulder_training'

    TRAINING_TYPES_CHOICES = [
        (BACK_TRAINING, 'back_training'),
        (CHEST_TRAINING, 'chest_training'),
        (BICEPS_TRAINING, 'biceps_training'),
        (TRICEPS_TRAINING, 'triceps_training'),
        (LEG_TRAINING, 'leg_training'),
        (GLUTE_TRAINING, 'glute_training'),
        (SHOULDER_TRAINING, 'shoulder_training')
    ]

    title = models.CharField(max_length=50, null=False, blank=False)
    title2 = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    image = models.ImageField(upload_to="photos/", blank=True)
    training_type = models.CharField(max_length=20, choices=TRAINING_TYPES_CHOICES,  default=BACK_TRAINING)

    def __str__(self):
        return f'Exercises [title={self.title}]'