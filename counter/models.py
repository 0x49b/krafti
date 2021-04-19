from django.db import models


class Visits(models.Model):
    class Meta:
        verbose_name = 'Visit'
        verbose_name_plural = 'Visits'
        indexes = [
            models.Index(fields=['id', 'added'])
        ]

    current_loggedin = models.BigIntegerField()
    current_free = models.BigIntegerField()
    added = models.DateTimeField(auto_now_add=True)
