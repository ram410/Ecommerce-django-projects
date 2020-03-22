from django.urls import path, include
from shop.api_views import ProductViewSet
from shop import views


from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('product', ProductViewSet, basename='product')

urlpatterns = [
    path("", views.index, name='index'),
    path("<int:id>/", views.detail, name='detail'),
    path("checkout/", views.checkout, name='checkout'),
    path('view/', include(router.urls)),
]