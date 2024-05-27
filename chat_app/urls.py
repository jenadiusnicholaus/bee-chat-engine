from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from chat_app.settings import API_VERSION
from rest_framework import routers



urlpatterns = [
    path('admin/', admin.site.urls),
    path(f'api/{API_VERSION}/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path(f'api/{API_VERSION}/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path(f'chat-engine/', include('chat.urls')),
    path(f'users/', include('users.urls')),
    path(f'intergration/', include('intergration_app.urls'))
]
