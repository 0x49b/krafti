from django.contrib import admin
from django.urls import path
from counter import views as counter

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', counter.index, name='counter-index'),
    path('get-daydata/', counter.get_daydata, name='counter-daydata')
]
