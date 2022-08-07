from rest_framework import authentication, permissions, status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


class CustomModelViewSet(ModelViewSet):
    model = None
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.model.objects.filter(wallet__user=self.request.user)

    # def list(self, request, *args, **kwargs):
    #     response = super(CustomModelViewSet, self).list(request, *args, **kwargs)
    #     for object in response.data:
    #         del object['user']
    #     return response

    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)
    #     response = serializer.data
    #     del response['user']
    #     return Response(response)

    # def create(self, request, *args, **kwargs):
    #     request.data['user'] = request.user.id
    #     response = super(CustomModelViewSet, self).create(request, *args, **kwargs)
    #     del response.data['user']
    #     return response

    # def update(self, request, *args, **kwargs):
    #     request.data['user'] = request.user.id
    #     partial = kwargs.pop('partial', False)
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data, partial=partial)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)
    #     response = serializer.data
    #     del response['user']
    #     if getattr(instance, '_prefetched_objects_cache', None):
    #         # If 'prefetch_related' has been applied to a queryset, we need to
    #         # forcibly invalidate the prefetch cache on the instance.
    #         instance._prefetched_objects_cache = {}
    #     return Response(response)