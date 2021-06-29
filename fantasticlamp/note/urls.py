from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("inscription/<title>", views.inscription, name="inscription"),
    # path("search", views.search, name="search")
]
