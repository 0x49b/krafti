from django.contrib import admin

from .models import Route, RouteArchive, Category, GradeScale, RouteSetter, RouteSetterNickname


class RouteSetterNicknameAdmin(admin.ModelAdmin):
    list_display = ('nickname',)


class RouteSetterAdmin(admin.ModelAdmin):
    list_display = ('lastname', 'firstname')


class GradeScaleAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'yds',
                    'british_tech',
                    'british_adj',
                    'french',
                    'uiaa',
                    'australia',
                    'saxon',
                    'scandinavia',
                    'brasil',
                    'fontainebleu',
                    )
    ordering = ['id']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')


class RouteAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'grade',
        'color',
        'setter',
        'date',
        'length',
        'route_num',
        'category',
        'slug',
    )

    list_filter = ('grade', 'length', 'category')
    search_fields = ('name', 'grade', 'length', 'date')


class RouteArchiveAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'grd',
        'color',
        'setter',
        'date',
        'length',
        'route_num',
        'category',
        'slug',
    )

    list_filter = ('grd', 'length', 'category')
    search_fields = ('name', 'grd', 'length', 'date')


admin.site.register(GradeScale, GradeScaleAdmin)
admin.site.register(Route, RouteAdmin)
admin.site.register(RouteArchive, RouteArchiveAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(RouteSetter, RouteSetterAdmin)
admin.site.register(RouteSetterNickname, RouteSetterNicknameAdmin)
