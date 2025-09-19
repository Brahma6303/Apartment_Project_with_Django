from django.db import models
from DBapp.models import Owner
# Create your models here.

class Meeting(models.Model):
    title=models.CharField(max_length=50)
    duration=models.SmallIntegerField()
    invitees=models.ManyToManyField(Owner)
    mom=models.FileField(upload_to='pdf/',null=True)

    def __str__(self):
        return f"{self.title} ({self.duration} hrs)"