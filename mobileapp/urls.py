from django.urls import path
from .import views

urlpatterns = [
    path('',views.home),
    path('create/',views.create_product,name='create'),
    path('list/',views.list_Products,name='list'),
    path('delete/<int:id>/', views.deletepdt, name='delete'),
]
