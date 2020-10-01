from django.db import models

# Create your models here.
class Todo(models.Model):
  added_date = models.DateTimeField()
  text = models.CharField(blank=False, null=False, max_length=200)
  
  def __str__(self):
    return self.text
