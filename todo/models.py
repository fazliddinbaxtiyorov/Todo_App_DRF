from django.db import models


# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(blank=True, default='')
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
