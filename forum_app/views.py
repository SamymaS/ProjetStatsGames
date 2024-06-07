# from django.shortcuts import render

# Create your views here.


from rest_framework import generics
from .models import Topic, Post, Comment
from .serializers import TopicSerializer, PostSerializer, CommentSerializer


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

# Vue pour Gérer la Réponse OAuth 
# Cette vue recevra un code de l'API qui sera utilisé pour obtenir un jeton d'accès.

import requests
from django.conf import settings
from django.shortcuts import redirect

def oauth_callback(request):
    code = request.GET.get('code')
    if not code:
        return redirect('/')

    # Échanger le code contre un jeton d'accès
    token_url = 'https://api.igdb.com/v4/token'
    data = {
        'client_id': settings.IGDB_CLIENT_ID,
        'client_secret': settings.IGDB_CLIENT_SECRET,
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': 'http://localhost:8000/oauth/callback/'
    }
    response = requests.post(token_url, data=data)
    response_data = response.json()

    access_token = response_data.get('access_token')
    if not access_token:
        return redirect('/')

    # Stocker le jeton d'accès dans la session (ou base de données)
    request.session['access_token'] = access_token

    return redirect('/')



# Redirige l'utilisateur vers l'URL d'autorisation 

def oauth_authorize(request):
    auth_url = 'https://api.igdb.com/v4/authorize'
    params = {
        'client_id': settings.IGDB_CLIENT_ID,
        'redirect_uri': 'http://localhost:8000/oauth/callback/',
        'response_type': 'code',
        'scope': 'user_info'
    }
    url = f"{auth_url}?{urllib.parse.urlencode(params)}"
    return redirect(url)

