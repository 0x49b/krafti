from django.contrib import admin
from .models import TrophyCategory, TrophyRoute


# Register your models here.
class TrophyCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'color')


class TrophyRouteAdmin(admin.ModelAdmin):
    list_display = ('number', 'category', 'route')
    list_filter = ('category', )
    ordering = ('number',)


admin.site.register(TrophyCategory, TrophyCategoryAdmin)
admin.site.register(TrophyRoute, TrophyRouteAdmin)
