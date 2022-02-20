from django.db import models


class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_completed= models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} - {self.is_completed}"
    