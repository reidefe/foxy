from django.conf.urls import url
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from .views import UserProfileDetailView, UserProfileListCreateView, NewsViewSet

router = routers.SimpleRouter()
router.register(r"news", NewsViewSet)
urlpatterns = [
    path("all-profiles", UserProfileListCreateView.as_view(), name="all-profiles"),
    path("profile/<int:pk>", UserProfileDetailView.as_view(), name="profile"),
]
urlpatterns += router.urls
