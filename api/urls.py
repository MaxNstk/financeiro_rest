from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import ObtainAuthToken

from api.viewsets.category_viewset import CategoryViewSet
from api.viewsets.transaction_viewset import TransactionViewSet

router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'transaction', TransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', ObtainAuthToken.as_view(), name='auth'),
]
