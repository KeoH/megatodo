from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include('api.urls', namespace='api')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', obtain_jwt_token),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
