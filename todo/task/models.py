from datetime import date

from django.db import models
from django.utils.timezone import now

PRIORITY = (
    ('1', '중요'),
    ('2', '보통'),
    ('3', '사소'),
)


class Todo(models.Model):
    title = models.CharField(max_length=100)
    note = models.TextField(blank=True)
    deadline = models.DateTimeField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=1, choices=PRIORITY, default='2')

    created_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.title

    def date_now(self):
        return date.today()

    class Meta:
        ordering = ["priority", 'deadline']
