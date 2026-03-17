from django.db import models
from django.utils import timezone
import datetime


class Task(models.Model):
    task_desc = models.CharField(max_length=200)
    status = models.BooleanField()
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.task_desc

    def task_was_finished_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
