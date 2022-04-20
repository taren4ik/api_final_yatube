from django.urls import include, path
from django.contrib import admin
from rest_framework.routers import SimpleRouter

from api.views import CommentViewSet
from api.views import GroupViewSet
from api.views import PostViewSet
from api.views import  FollowViewSet

router = SimpleRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register('follow', FollowViewSet)
router.register(
    r'^posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='post')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]