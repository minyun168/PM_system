from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    month = models.CharField(max_length=100)
    day = models.CharField(max_length=100)
    finished_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
