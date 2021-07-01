import uuid as uuid
from colorfield.fields import ColorField
from django.db import models
from django.template.defaultfilters import slugify


class GradeScaleCategory(models.Model):
    class Meta:
        verbose_name = "Grad Skala Kategorie"
        verbose_name_plural = "Grad Skala Kategorien"

    name = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.name


class RouteSetter(models.Model):
    class Meta:
        verbose_name = "Route Setter"
        verbose_name_plural = "Route Setters"

    lastname = models.CharField(max_length=255, blank=False, null=False)
    firstname = models.CharField(max_length=255, blank=False, null=False)
    nickname = models.ManyToManyField('RouteSetterNickname')
    img_url = models.URLField(blank=True, null=True)
    since = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return "%s %s" % (self.firstname, self.lastname)


class RouteSetterNickname(models.Model):
    class Meta:
        verbose_name = "Route Setter Nickname"
        verbose_name_plural = "Route Setter Nicknames"

    nickname = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nickname


class GradeScale(models.Model):
    class Meta:
        verbose_name = "Grad Skala"
        verbose_name_plural = "Grad Skalas"

    yds = models.CharField(max_length=10, verbose_name="YDS (USA)", null=True, blank=True)
    british_tech = models.CharField(max_length=10, verbose_name="British (UK) Tech", null=True, blank=True)
    british_adj = models.CharField(max_length=10, verbose_name="British (UK) Adj", null=True, blank=True)
    french = models.CharField(max_length=10, verbose_name="Französisch", null=True, blank=True)
    uiaa = models.CharField(max_length=10, verbose_name="UIAA (MiddleEurope)", null=True, blank=True)
    australia = models.CharField(max_length=10, verbose_name="Australia", null=True, blank=True)
    saxon = models.CharField(max_length=10, verbose_name="Sächisch (Sachsen/Nordböhmen)", null=True, blank=True)
    scandinavia = models.CharField(max_length=10, verbose_name="Scandinavia", null=True, blank=True)
    brasil = models.CharField(max_length=10, verbose_name="Brasil", null=True, blank=True)
    fontainebleu = models.CharField(max_length=10, verbose_name="Fontainebleu", null=True, blank=True)

    def __str__(self):
        return "%s" % self.french

    def save(self, *args, **kwargs):
        if not self.uuid or self.uuid is None:
            self.uuid = uuid.uuid4()
        return super().save(*args, **kwargs)


class Category(models.Model):
    class Meta:
        verbose_name = "Kategorie"
        verbose_name_plural = "Kategorien"

    name = models.CharField(max_length=50)
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Route(models.Model):
    class Meta:
        verbose_name = "Route"
        verbose_name_plural = "Routen"

    uuid = models.UUIDField(default=uuid.uuid4(), editable=False, null=True)
    grade = models.ForeignKey(GradeScale, null=True, on_delete=models.SET_NULL, verbose_name="Grade")
    color = ColorField(null=False, blank=False)
    name = models.CharField(max_length=250, null=False, blank=False)
    setter = models.CharField(max_length=25, null=False, blank=False)
    date = models.DateField(auto_now_add=False, auto_created=False, auto_now=False)
    length = models.IntegerField(null=False, blank=False)
    route_num = models.CharField(max_length=4, null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(null=True, blank=True)
    archived = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.uuid or self.uuid is None:
            self.uuid = uuid.uuid4()
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return "%s %s %s %s %s, %s, %s" % (
            self.color, self.name, self.setter, self.date, self.length, self.route_num, self.category.name)


class RouteArchive(models.Model):
    class Meta:
        verbose_name = "[Archiv] Route"
        verbose_name_plural = "[Archiv] Routen"

    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    grd = models.ForeignKey(GradeScale, null=True, on_delete=models.SET_NULL, verbose_name="Grade")
    color = ColorField(null=False, blank=False)
    name = models.CharField(max_length=250, null=False, blank=False)
    setter = models.CharField(max_length=25, null=False, blank=False)
    date = models.DateField(auto_now_add=False, auto_created=False, auto_now=False)
    length = models.IntegerField(null=False, blank=False)
    route_num = models.CharField(max_length=4, null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    archived = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return "%s %s %s %s %s %s, %s, %s" % (
            self.grd.french, self.color, self.name, self.setter, self.date, self.length, self.route_num,
            self.category.name)
