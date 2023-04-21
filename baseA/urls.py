from .views import ClienteViewSet
from rest_framework.routers import DefaultRouter

app_name = 'baseA'

router = DefaultRouter(trailing_slash=False)
router.register('', ClienteViewSet)

urlpatterns = router.urls