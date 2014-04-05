from django.conf.urls import patterns, url, include
from rest_framework import routers
from slotting import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'vendor', views.VendorViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
)
