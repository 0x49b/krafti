from django.contrib import admin
from django.urls import path, include
from counter import views as counter
from routes import views as routes
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'routes', routes.RouteViewSet)
router.register(r'routes-archive', routes.RouteArchiveViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include(router.urls)),
    path('', counter.index, name='counter-index'),
    path('get-daydata/', counter.get_daydata, name='counter-daydata'),
    path('route-test/', routes.testRouteList, name='routes-test')
]
