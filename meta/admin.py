from django.contrib import admin
from .models import OpeningHours


# Register your models here.
class OpeningHoursAdmin(admin.ModelAdmin):
    list_display = ("day", "open_from", "close_at")


admin.site.register(OpeningHours, OpeningHoursAdmin)
