from django.shortcuts import render
from django.contrib.auth.mixins import UserPassesTestMixin
from django.db import connection
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics, mixins
from django_filters import rest_framework as filters
from rest_framework.views import APIView


from .models import Tweet, User, Follower
from .serializers import TweetSerializer, FollowerSerializer, AllDataSerializer
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

    def delete(self, request, follower_id=None):

        unfollow = Follower.objects.filter(followed_id=follower_id)
        unfollow.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AllData(APIView):

    def get(self, *args):

        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT authapi_user.id AS profile_id, authapi_user.first_name, authapi_user.last_name, authapi_tweet.tweet_text, authapi_tweet.created_on FROM authapi_tweet INNER JOIN authapi_user ON authapi_user.id = authapi_tweet.author_id ORDER BY created_on DESC;")
            table = cursor.fetchall()
            return Response(table)
