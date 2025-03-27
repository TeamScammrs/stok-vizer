from django.urls import path
from . import views
urlpatterns = [
    path("chat/", views.index, name="chat"),
    path("stock/", views.stock, name="stock"),
]