from django.urls import path
from . import views

app_name = 'courses'
urlpatterns = [
    path('subjects/', views.SubjectListView.as_view(), name='subject_list'),
    path('subjects/<pk>/', views.SubjectDetailView.as_view(), name="subject_detail"),
    path('clients/', views.ClientListView.as_view(), name="client_list"),
    path('clients/<pk>/', views.ClientDetailView.as_view(), name="client_detail")
]
