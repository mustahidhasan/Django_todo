from django.db import models

# Create your models here.

class task(models.Model):
    task_name = models.TextField()
    task_date = models.DateField()
    task_time = models.TimeField()
    task_des = models.TextField()
    work_done = models.TextField()

