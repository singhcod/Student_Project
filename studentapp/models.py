
from django.db import models

class Student(models.Model):
    sname = models.CharField(max_length=50)
    subject1 = models.IntegerField()
    subject2 = models.IntegerField()
    subject3 = models.IntegerField()
    subject4 = models.IntegerField()
    subject5 = models.IntegerField()
    subject6 = models.IntegerField()

    def __str__(self):
        return self.sname


