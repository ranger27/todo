from django.db import models

# Create your models here.
class Todo(models.Model):
    text = models.CharField(verbose_name = "Your Todo", max_length=30)
    completed =  models.BooleanField(default=False)

    def __str__(self):
        return self.text