from django.conf.urls import url, include
from rest_framework import routers

from .views import TodoViewSet, UserViewSet

router = routers.DefaultRouter()

router.register(r'todos', TodoViewSet, base_name='todo-list')
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]