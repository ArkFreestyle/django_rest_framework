from django.urls import path, include
from snippets import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# The router takes care of all URL pattern configurations
urlpatterns = [
    path('', include(router.urls)),
]
