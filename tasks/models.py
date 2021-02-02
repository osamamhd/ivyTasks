from django.utils import timezone
from django.db import models
from django.conf import settings


class Task(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    pub_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    completed = models.BooleanField(default=False)
    completed_date = models.DateField(blank=True, null=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ["-pub_date"] # Ordering by the pub date field
    def __str__(self):
        return self.title
