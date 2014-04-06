from django.conf.urls import patterns, url, include
from rest_framework import routers
from slotting import views
from rest_framework import routers

urlpatterns = []

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'vendor', views.VendorViewSet)
router.register(r'assignment', views.AssignmentViewSet)
router.register(r'stall', views.StallViewSet)

urlpatterns += patterns('',
    url(r'^', include(router.urls)),
)

from project.routers import SingletonRouter
router = SingletonRouter(trailing_slash=False)
router.register(r'market_day', views.MarketDayView)

urlpatterns += patterns('',
    url(r'^', include(router.urls)),
)

