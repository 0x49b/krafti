from django.contrib import admin
from .models import Route, RouteArchive

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
    )

    list_filter = ('grade', 'length', 'categorie')
    search_fields = ('name', 'grade', 'length', 'date')


class RouteArchiveAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'grade',
        'color',
        'setter',
        'date',
        'length',
        'route_num',
        'categorie',
    )

    list_filter = ('grade', 'length', 'categorie')
    search_fields = ('name', 'grade', 'length', 'date')


admin.site.register(Route, RouteAdmin)
admin.site.register(RouteArchive, RouteArchiveAdmin)
