from django.db import models
from tinymce.models import HTMLField


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


class ModalInfo(models.Model):
    class Meta:
        verbose_name = "Modal Info"
        verbose_name_plural = "Modal info"

    type = models.CharField(max_length=25, blank=False, null=False)
    info = HTMLField(null=False, blank=False)
