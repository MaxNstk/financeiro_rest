from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import ObtainAuthToken

from api.viewsets.category_viewset import CategoryViewSet
from api.viewsets.sub_category_viewset import SubCategoryViewSet
from api.viewsets.transaction_viewset import TransactionViewSet
from api.viewsets.user_viewset import UserViewSet
from api.viewsets.objetive_viewset import ObjectiveViewSet

router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'transaction', TransactionViewSet)
router.register(r'user', UserViewSet)
router.register(r'objetive', ObjectiveViewSet)
router.register(r'sub_category', SubCategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', ObtainAuthToken.as_view(), name='auth'),
]