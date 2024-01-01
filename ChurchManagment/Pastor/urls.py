from django.urls import path
from .views import (
    PastorListView,
    PastorDetailView,
    PastorCreateView,
    PastorUpdateView,
    PastorDeleteView,
)

urlpatterns = [
    path('', PastorListView.as_view(), name='pastor_list'),
    path('<int:pk>/', PastorDetailView.as_view(), name='pastor_detail'),
    path('new/', PastorCreateView.as_view(), name='pastor_create'),
    path('<int:pk>/edit/', PastorUpdateView.as_view(), name='pastor_update'),
    path('<int:pk>/delete/', PastorDeleteView.as_view(), name='pastor_delete'),
]