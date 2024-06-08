from django.urls import path
from .views import oauth_authorize, oauth_callback, get_games_from_igdb, TopicListCreateView, TopicDetailView, PostListCreateView, PostDetailView, CommentListCreateView, CommentDetailView, api_index

urlpatterns = [
    path('oauth/authorize/', oauth_authorize, name='oauth_authorize'),
    path('oauth/callback/', oauth_callback, name='oauth_callback'),
    path('games/', get_games_from_igdb, name='get_games_from_igdb'),
    path('topics/', TopicListCreateView.as_view(), name='topic-list'),
    path('topics/<int:pk>/', TopicDetailView.as_view(), name='topic-detail'),
    path('posts/', PostListCreateView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('comments/', CommentListCreateView.as_view(), name='comment-list'),
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
    path('', api_index, name='api_index'),  # Ajoutez cette ligne pour l'index de l'API
]
