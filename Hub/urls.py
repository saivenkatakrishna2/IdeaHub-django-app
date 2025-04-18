from django.urls import path
from .views import Home, DetailedIdeaView, AddPostView, UpdatePostView, DeletePostView

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('detailidea/<int:pk>', DetailedIdeaView.as_view(), name='detailidea'),
    path('add_post', AddPostView.as_view(), name = 'add_post'),
    path('detailidea/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('detailidea/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'),
]
