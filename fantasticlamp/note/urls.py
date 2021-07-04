from django.urls import path
from . import views
app_name = 'note'
urlpatterns = [
    path("", views.index, name="index"),
    path("inscription/<id>", views.inscription, name="inscription"),
    path("add", views.add, name="add"),
    path("update/<id>", views.update, name="update"),
    path("delete/<id>", views.delete, name="delete"),

    # path("search", views.search, name="search")
]
