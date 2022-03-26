from django.urls import path, include

import api

urlpatterns = [
    path('api/v1/', include('api.urls')),
]
