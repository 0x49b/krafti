from django.db import models


# Create your models here.
class JournalEntry(models.Model):
    class Meta:
        verbose_name = "Journal Entry"
        verbose_name_plural = "Journal Entries"


