from django.urls import path
from . import views

urlpatterns = [
    path('create', views.ProjectCreateView.as_view(), name='create-project'),
    path('list/', views.ProjectListView.as_view(), name='list-project'), 
    path('update/<int:pk>/', views.ProjectUpdateView.as_view(), name='update-project'),
]