from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [

    path('admin/', views.AdminListView.as_view(), name='admin-list'),
    path('admin/<int:pk>/', views.AdminDetailView.as_view(), name='admin-detail'),
]
