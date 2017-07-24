from rest_framework import routers
from post_rest.viewsets import PostViewSet, ImageViewSet

router = routers.DefaultRouter()
router.register('posts', PostViewSet, 'posts')
router.register('images', ImageViewSet, 'images')

urlpatterns = router.urls



