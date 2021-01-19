from django.utils import timezone
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    pub_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))

    class Meta:
        ordering = ["-pub_date"] # Ordering by the pub date field
    def __str__(self):
        return self.title
