from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path("", views.home, name="home"),
    path("api/me/", MeView.as_view(), name="api=me"),
    path("api/click/", ClickView.as_view(), name="api-click"),
]