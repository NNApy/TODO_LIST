from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Tasks(models.Model):
    task_name = models.CharField(max_length=100)
    done = models.CharField(max_length=1, default=0, null=False)
    position = models.CharField(max_length=4)