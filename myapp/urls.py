from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('task/', views.task, name="task"),
    path('deletetask/<int:id>', views.deletetask, name="delete"),
    path('update/<int:id>', views.update, name="update"),
]
