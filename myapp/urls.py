from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from .views import CategoryViewSet,ProductViewSet,CartViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'product', ProductViewSet, basename='product')
router.register(r'cart', CartViewSet, basename='cart')

urlpatterns = [
    path('', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)