from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name = "index"),
    path('completed/<int:id>',views.completed,name="completed"),
    path('delete/<int:id>',views.delete,name="delete"),
    path('add',views.add,name="add"),
]