from django.db import models
import uuid
from colorfield.fields import ColorField
from routes.models import Route


# Create your models here.
class TrophyCategory(models.Model):
    class Meta:
        verbose_name = 'Trophy Kategorie'
        verbose_name_plural = 'Trophy Kategorien'

    uuid = models.UUIDField(default=uuid.uuid4(), editable=False, null=True)
    name = models.CharField(max_length=50, null=False, blank=False, unique=True)
    color = ColorField(null=False, blank=False)

    def __str__(self):
        return self.name


class TrophyRoute(models.Model):
    class Meta:
        verbose_name = 'Trophy Route'
        verbose_name_plural = 'Trophy Routen'

    uuid = models.UUIDField(default=uuid.uuid4(), editable=False, null=True)
    number = models.IntegerField(null=False, blank=True)
    category = models.ForeignKey(TrophyCategory, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)

    def __str__(self):
        return "%s | %s" % (self.category.name, self.route.name)
