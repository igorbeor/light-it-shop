from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view
from django.contrib import admin
from catalog import views

router = DefaultRouter()
router.register(r'categories', views.CategoryViewSet, base_name='categories')
router.register(r'items', views.ItemViewSet, base_name='items')

schema_view = get_swagger_view(title='API Documentation', patterns=router.urls)

urlpatterns = [
    re_path(r'swagger', schema_view),
    re_path(r'', include(router.urls)),
    path('admin/', admin.site.urls),
    path('auth/', include('rest_auth.urls')),
]
