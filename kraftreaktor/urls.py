from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from counter import views as counter
from routes import views as routes
from meta import views as meta
from trophy import views as trophy

schema_view = get_schema_view(
    openapi.Info(
        title="Climbswiss API",
        default_version='v1',
        description="Climbswiss API Documentation",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register(r'routes', routes.RouteViewSet)
router.register(r'categories', routes.CategoryViewSet)
router.register(r'grades', routes.GradeScaleViewSet)
router.register(r'visits', counter.LastCounterViewSet)
router.register(r'opening-hours', meta.OpeningHoursViewSet)
router.register(r'current-grades', routes.CurrentGradesViewSet)
router.register(r'trophy-routes', trophy.TrophyRouteViewSet)
router.register(r'trophy-categories', trophy.TrophyCategoryViewSet)

urlpatterns = [
    path('trophy/', include('trophy.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include(router.urls)),
    path('', counter.index, name='counter-index'),
    path('get-daydata/', counter.get_daydata, name='counter-daydata'),

    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('tinymce/', include('tinymce.urls')),
]
