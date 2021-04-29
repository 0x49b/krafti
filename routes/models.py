from django.db import models
from colorfield.fields import ColorField

CATEGORIES = (
    (0, 'Galerie Vorstieg'),
    (1, 'Turm Toprope'),
    (2, 'Turm Vorstieg'),
    (3, 'Hauptwand'),
    (4, 'Galerie Toprope'),
)


class Route(models.Model):
    class Meta:
        verbose_name = "Route"
        verbose_name_plural = "Routen"

    grade = models.CharField(max_length=3, null=False, blank=False)
    color = ColorField(null=False, blank=False)
    name = models.CharField(max_length=250, null=False, blank=False)
    setter = models.CharField(max_length=25, null=False, blank=False)
    date = models.DateField(auto_now_add=False, auto_created=False, auto_now=False)
    length = models.IntegerField(null=False, blank=False)
    route_num = models.CharField(max_length=4, null=False, blank=False)
    categorie = models.IntegerField(choices=CATEGORIES)
    active = models.BooleanField(default=True)

    def __str__(self):
        return "%s %s %s %s %s %s, %s, %d" % (
            self.grade, self.color, self.name, self.setter, self.date, self.length, self.route_num, self.categorie)
