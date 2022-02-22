from django.db import models
from django.contrib.auth.models import User
from patients.models import Image
# Create your models here.


class Grading(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    grader = models.ForeignKey(User, on_delete=models.CASCADE)
    result = models.TextField(null=True, blank=True)
    done_date = models.DateTimeField(null=True)

    class Meta:
        unique_together = ['image', 'grader']
