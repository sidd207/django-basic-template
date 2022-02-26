from django.urls import path
from . import views

urlpatterns = [
    path('', views.view),
    path('add', views.add),
    path('delete/<int:code_id>', views.delete),
    path('edit/<int:code_id>', views.edit)
] 