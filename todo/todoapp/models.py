from django.db import models

# Create your models here.


class Todo(models.Model):
    todo = models.CharField(max_length=100, null=False)
    data = models.DateField()

    def __str__(self):
        return self.todo