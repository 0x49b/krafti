from django.contrib import admin
from .models import Visits


# Register your models here.
class VisitsAdmin(admin.ModelAdmin):
    list_display = ['added', 'current_loggedin', 'current_free']
    sortable_by = ('added', 'current_loggedin')
    search_fields = ('added', )


admin.site.register(Visits, VisitsAdmin)
