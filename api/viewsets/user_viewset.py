from rest_framework import status, authentication, permissions
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from account.models import User
from api.serializers.user_serializer import UserSerializer


class CustomAuthentication(permissions.IsAuthenticated):

    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        super(CustomAuthentication, self).has_permission(request, view)


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [CustomAuthentication]
    http_method_names = ['get', 'post', 'put']
    queryset = User.objects.all()


    def list(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return Response({"forbidden": "forbidden"}, status=status.HTTP_403_FORBIDDEN)
        super(UserViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        serializer.instance.set_password(serializer.data['password'])
        serializer.instance.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance != request.user and not request.user.is_superuser:
            return Response({"forbidden": "forbidden"}, status=status.HTTP_403_FORBIDDEN)
        partial = kwargs.pop('partial', False)
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        serializer.instance.set_password(request.data.password)
        serializer.save()
        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        if self.get_object() != request.user and not request.user.is_superuser:
            return Response({"forbidden": "forbidden"}, status=status.HTTP_403_FORBIDDEN)
        return super(UserViewSet, self).retrieve(request, *args, **kwargs)

