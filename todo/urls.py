from django.urls import path
from .views import All, Delete, Detail, Create, Update
urlpatterns = [
    path('api/', All.as_view(), name='home'),
    path('api/new/', Create.as_view(), name='new'),
    path('api/<int:id>', Detail.as_view(), name='detail'),
    path('api/<int:id>/delete', Delete.as_view(), name='delete'),
    path('api/<int:id>/update', Update.as_view(), name='update'),
]