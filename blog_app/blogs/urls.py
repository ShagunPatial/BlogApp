from django.urls import path

from . import views

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogViewSet, CommentViewSet, ReactionViewSet

router = DefaultRouter()
router.register(r'blogs', BlogViewSet, basename='blog')
router.register(r'comments', CommentViewSet, basename='comment')
router.register(r'reactions', ReactionViewSet, basename='reaction')

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('api/', include(router.urls)),
]
