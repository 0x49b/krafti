from django.db import models
from .choices import DAYS


# Create your models here.
class OpeningHours(models.Model):
    class Meta:
        verbose_name = "Öffnungszeit"
        verbose_name_plural = "Öffnungszeiten"

    day = models.CharField(max_length=2, choices=DAYS, default="SP", unique=True)
    open_from = models.TimeField(null=False, blank=False)
    close_at = models.TimeField(null=False, blank=False)
    special = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.day
