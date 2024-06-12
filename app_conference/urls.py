from rest_framework import routers

from app_conference.views import LogoViewSet

router = routers.DefaultRouter()

router.register('logo', LogoViewSet, basename='logo')
router.register('conference', LogoViewSet, basename='conference')

urlpatterns = router.urls
