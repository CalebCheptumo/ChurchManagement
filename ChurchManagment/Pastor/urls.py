from django.urls import path
from .views import (
    PastorListView,
    PastorDetailView,
    PastorCreateView,
    PastorUpdateView,
    PastorDeleteView,
)

urlpatterns = [
    path('pastors/', PastorListView.as_view(), name='pastor_list'),
    path('pastors/<int:pk>/', PastorDetailView.as_view(), name='pastor_detail'),
    path('pastors/new/', PastorCreateView.as_view(), name='pastor_create'),
    path('pastors/<int:pk>/edit/', PastorUpdateView.as_view(), name='pastor_update'),
    path('pastors/<int:pk>/delete/', PastorDeleteView.as_view(), name='pastor_delete'),
]