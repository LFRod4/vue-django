from django.shortcuts import render
from django.contrib.auth.mixins import UserPassesTestMixin
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics, mixins
from django_filters import rest_framework as filters
from rest_framework.views import APIView


from .models import Tweet, User, Follower
from .serializers import TweetSerializer, FollowerSerializer
from .permissions import IsOwnerOrReadOnly

# Create your views here.


class TweetAPIView(generics.CreateAPIView, mixins.CreateModelMixin):
    lookup_field = 'pk'
    serializer_class = TweetSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class AllTweets(APIView):
    permission_classes = [IsOwnerOrReadOnly]

    def get(self, request, author=None):
        if author != None:
            tweets = Tweet.objects.filter(
                author=author).order_by('-created_on')
        else:
            tweets = Tweet.objects.all()
        data = TweetSerializer(tweets, many=True).data
        return Response(data)


class Followers(APIView):
    permission_classes = [IsOwnerOrReadOnly]

    def get(self, request, follower_id=None):
        if follower_id != None:
            followers = Follower.objects.filter(follower_id=follower_id)
        else:
            followers = Follower.objects.all()
        data = FollowerSerializer(followers, many=True).data
        return Response(data)

    def post(self, request):
        serializer = FollowerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
