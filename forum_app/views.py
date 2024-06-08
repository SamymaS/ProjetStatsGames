from rest_framework import generics
from .models import Topic, Post, Comment
from .serializers import TopicSerializer, PostSerializer, CommentSerializer
from django.shortcuts import render, redirect
from django.conf import settings
import urllib.parse
import requests

# Vues existantes
class TopicListCreateView(generics.ListCreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

class TopicDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

# Vue pour gérer la réponse OAuth
def oauth_callback(request):
    code = request.GET.get('code')
    if not code:
        return redirect('/')

    # Échanger le code contre un jeton d'accès
    token_url = 'https://id.twitch.tv/oauth2/token'
    data = {
        'client_id': settings.IGDB_CLIENT_ID,
        'client_secret': settings.IGDB_CLIENT_SECRET,
        'code': code,
        'grant_type': 'authorization_code',
        'redirect_uri': settings.IGDB_REDIRECT_URI
    }
    response = requests.post(token_url, data=data)
    response_data = response.json()

    access_token = response_data.get('access_token')
    if not access_token:
        return redirect('/')

    # Stocker le jeton d'accès dans la session (ou base de données)
    request.session['access_token'] = access_token

    return redirect('/games/')

# Rediriger l'utilisateur vers l'URL d'autorisation
def oauth_authorize(request):
    auth_url = 'https://id.twitch.tv/oauth2/authorize'
    params = {
        'client_id': settings.IGDB_CLIENT_ID,
        'redirect_uri': settings.IGDB_REDIRECT_URI,
        'response_type': 'code',
        'scope': 'user:read:email'
    }
    url = f"{auth_url}?{urllib.parse.urlencode(params)}"
    return redirect(url)

# Vue pour récupérer les données de jeux depuis IGDB
def get_games_from_igdb(request):
    access_token = request.session.get('access_token')
    if not access_token:
        return redirect('/oauth/authorize/')

    url = 'https://api.igdb.com/v4/games'
    headers = {
        'Client-ID': settings.IGDB_CLIENT_ID,
        'Authorization': f'Bearer {access_token}',
    }
    data = 'fields name, genres, platforms, rating; limit 10;'
    response = requests.post(url, headers=headers, data=data)
    games = response.json()
    return render(request, 'forum_app/games.html', {'games': games})
