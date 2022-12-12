from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, RatingViewSet

router = DefaultRouter()
router.register('coments', CommentViewSet)
router.register('ratings', RatingViewSet)


urlpatterns = [
    path('', include(router.urls)),

]

from django.contrib import admin

"""=============Swagger docs============="""
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

swagger_view = get_schema_view(
    openapi.Info(
        title="Auth API",
        default_version='v1',
        description="auth API"
    ),
    public=True
)
"""======================================"""


urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', swagger_view.with_ui('swagger', cache_timeout=0)),
    path('account/', include('account.urls')),
    path('', include('main.urls')),
]