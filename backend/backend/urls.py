from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view
from catalog import views

router = DefaultRouter()
router.register(r'categories', views.CategoryViewSet, base_name='categories')
router.register(r'items', views.ItemViewSet, base_name='items')

schema_view = get_swagger_view(title='API Documentation', patterns=router.urls)

urlpatterns = [
    url(r'swagger', schema_view),
    url(r'', include(router.urls))
]
