import uuid as uuid
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from routes.models import GradeScale
from django.db import models
from location_field.models.plain import PlainLocationField
from .choices import LANGUAGE, SEX


class Profile(models.Model):
    class Meta:
        verbose_name = "Profil"
        verbose_name_plural = "Profile"

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=255)
    location = PlainLocationField(based_fields=['city'], zoom=7, blank=True, null=True)
    avatar = models.ImageField(null=True, blank=True)
    private = models.BooleanField(default=False)
    sex = models.CharField(max_length=1, choices=SEX, default="o")
    language = models.CharField(max_length=3, choices=LANGUAGE, null=True, blank=True, default=None)
    preferred_gradescale = models.ForeignKey(GradeScale, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return "Profile %s" % self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
