from django.urls import include, path
from rest_framework import routers
from restApi import views
from rest_framework.authtoken import views as auth_views
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'files', views.FileViewSet)
router.register(r'posts', views.PostViewSet)

urlpatterns = [
    path(r'^api/', include(router.urls)),
    path('api/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/api-token-auth/', views.ExtendedAuthToken.as_view()),
]