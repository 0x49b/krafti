import uuid as uuid
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from routes.models import GradeScale

SEX = (('m', "Male"), ("f", "Female"), ("d", "Divers"), ("o", "Other"))


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uuid = models.UUIDField(default=uuid.uuid4)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    avatar = models.ImageField(null=True, blank=True)
    private = models.BooleanField(default=False)
    sex = models.CharField(max_length=1, choices=SEX, default="o")
    language = models.CharField(max_length=255, null=True,
                                blank=True)  # Todo add some language table and parse from there
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
