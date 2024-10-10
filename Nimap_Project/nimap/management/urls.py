from django.urls import path
from .views import (
    ClientListView,
    ClientCreateView,
    ClientUpdateView,
    ClientDeleteView,
    ProjectCreateView,
    UserProjectsView
)

urlpatterns = [
    path('clients/', ClientListView.as_view(), name='client-list'),
    path('clients/create/', ClientCreateView.as_view(), name='client-create'),
    path('clients/<int:pk>/edit/', ClientUpdateView.as_view(), name='client-edit'),
    path('clients/<int:pk>/delete/', ClientDeleteView.as_view(), name='client-delete'),
    path('projects/create/', ProjectCreateView.as_view(), name='project-create'),
    path('my-projects/', UserProjectsView.as_view(), name='user-projects'),
]
