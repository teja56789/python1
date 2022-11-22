from rest_framework import routers
from .views import ItemViewSet,offerViewSet

router = routers.DefaultRouter()
router.register(r'item',ItemViewSet)
router.register(r'offer',offerViewSet)

urlpatterns = router.urls
