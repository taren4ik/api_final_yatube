from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)
from rest_framework.routers import SimpleRouter

from api.views import CommentViewSet
from api.views import GroupViewSet
from api.views import PostViewSet
from api.views import FollowViewSet

router = SimpleRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register('follow', FollowViewSet,  basename='follow')
router.register(
    r'^posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='post')


urlpatterns = [
    path('v1/', include(router.urls)),
   # path('v1/auth/', include('djoser.urls')),
    path('v1/auth/', include('djoser.urls.jwt')),
    path('v1/token/', TokenObtainPairView.as_view(), name='token_pair'),
    path('v1/token/refresh/', TokenRefreshView.as_view, name='token_refresh')
]