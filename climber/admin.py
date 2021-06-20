from django.contrib import admin
from .models import Profile


# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'user', 'bio', 'location', 'birth_date')

admin.site.register(Profile, ProfileAdmin)
