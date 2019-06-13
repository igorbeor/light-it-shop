from rest_framework.routers import DefaultRouter
from catalog import views

router = DefaultRouter()
router.register(r'categories', views.CategoryViewSet, base_name='categories')
router.register(r'items', views.ItemViewSet, base_name='items')

urlpatterns = router.urls

