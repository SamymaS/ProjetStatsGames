# forum_app/urls.py

# forum_app/urls.py

from django.urls import path
from .views import TopicListCreateView, TopicDetailView, PostListCreateView, PostDetailView, CommentListCreateView, CommentDetailView, oauth_callback, oauth_authorize 

urlpatterns = [
    path('topics/', TopicListCreateView.as_view(), name='topic-list-create'),
    path('topics/<int:pk>/', TopicDetailView.as_view(), name='topic-detail'),
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
    path('oauth/callback/', oauth_callback, name='oauth_callback'),
    path('oauth/authorize/', oauth_authorize, name='oauth_authorize'),
    path('oauth/callback/', oauth_callback, name='oauth_callback'),
]

