from django.contrib import admin
from .models import Route


# Register your models here.

class RouteAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'grade',
        'color',
        'setter',
        'date',
        'length',
        'route_num',
        'categorie',
        'active',
    )

    list_filter = ('grade', 'length', 'categorie')

    search_fields = ('name', 'grade', 'length', 'date')


admin.site.register(Route, RouteAdmin)
