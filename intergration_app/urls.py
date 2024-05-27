from django.urls import path, include
from rest_framework import routers

from intergration_app.views import UserIntergrationAppView

router = routers.DefaultRouter()
router.register(r'intergration-app-vset', UserIntergrationAppView)

from chat_app.settings import API_VERSION

urlpatterns = [
        path(f'api/{API_VERSION}/', include(router.urls)),
]
