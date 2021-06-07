from django.urls import path
from . import views

urlpatterns = [
    # TODO add
    path('users/', views.UserListView.as_view()),
    path('users/<int:pk>/', views.UserDetailView.as_view()),
    path('posts/create/', views.PostCreateView.as_view()),
    path('posts/', views.PostListView.as_view()),
    path('posts/<int:pk>/', views.PostDetailView.as_view()),
    path('posts/update/<int:pk>/', views.PostUpdateView.as_view()),
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view()),
    path('like/', views.LikeCreateView.as_view()),
    path('dislike/', views.DisLikeCreateView.as_view()),
]