from django.urls import path
from .views import Home, DetailedIdeaView, AddPostView, UpdatePostView, DeletePostView

urlpatterns = [
    path('', Home.as_view(), name="home"),
    
]
