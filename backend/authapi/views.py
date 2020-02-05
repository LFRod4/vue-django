from django.shortcuts import render
from django.contrib.auth.mixins import UserPassesTestMixin
from django.db import connection
from django.views.generic.edit import DeleteView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics, mixins
from django_filters import rest_framework as filters
from rest_framework.views import APIView
from urllib import parse


from .models import Tweet, User, Follower
from .serializers import TweetSerializer, FollowerSerializer, AllDataSerializer
from .permissions import IsOwnerOrReadOnly

# Create your views here.


class TweetAPIView(generics.CreateAPIView, mixins.CreateModelMixin, generics.GenericAPIView):
    lookup_field = 'pk'
    serializer_class = TweetSerializer

    def get(self, request, author=None):
        if author != None:
            tweets = Tweet.objects.filter(
                author=author).order_by('-created_on')
        else:
            tweets = Tweet.objects.all()
        data = TweetSerializer(tweets, many=True).data
        return Response(data)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class Followers(generics.CreateAPIView, mixins.CreateModelMixin, generics.GenericAPIView, DeleteView):
    serializer_class = FollowerSerializer

    def get(self, request, follower_id=None):
        if follower_id != None:
            followers = Follower.objects.filter(follower_id=follower_id)
        else:
            followers = Follower.objects.all()
        data = FollowerSerializer(followers, many=True).data
        return Response(data)

    def delete(self, request, *args, **kwargs):
        print(self.get('followers'))
        # unfollow = Follower.objects.filter(
        #     follower_id=follower_id, followed_id=followed_id)
        # unfollow.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request):
        return self.create(request)


class AllData(APIView):

    def get(self, request, ids=None):
        followers = self.request.GET
        follower_ids = []
        if(len(followers) == 1):
            follower_ids = int(followers['0'])
        else:
            for x in followers:
                follower_ids.append(int(followers[x]))
            follower_ids = tuple(follower_ids)

        with connection.cursor() as cursor:

            if(len(followers) == 1):
                print('1')
                sql = """SELECT authapi_user.id, authapi_user.first_name, authapi_user.last_name, authapi_user.username, authapi_tweet.tweet_text, authapi_tweet.created_on FROM authapi_tweet INNER JOIN authapi_user ON authapi_user.id = authapi_tweet.author_id WHERE authapi_tweet.author_id = {} ORDER BY created_on DESC"""
            elif (len(followers) > 1):
                print('greater')
                sql = """SELECT authapi_user.id, authapi_user.first_name, authapi_user.last_name, authapi_user.username, authapi_tweet.tweet_text, authapi_tweet.created_on FROM authapi_tweet INNER JOIN authapi_user ON authapi_user.id = authapi_tweet.author_id WHERE authapi_tweet.author_id IN {} ORDER BY created_on DESC"""
            else:
                print('else')
                sql = """SELECT authapi_user.id, authapi_user.first_name, authapi_user.last_name, authapi_user.username, authapi_tweet.tweet_text, authapi_tweet.created_on FROM authapi_tweet INNER JOIN authapi_user ON authapi_user.id = authapi_tweet.author_id WHERE authapi_tweet.author_id IN {} ORDER BY created_on DESC"""

            sql = sql.format(follower_ids)
            cursor.execute(sql)
            table = cursor.fetchall()
            return Response(table)


class UserProfiles(APIView):

    def get(self, request, ids=None):
        profiles = self.request.GET
        profile_ids = []
        if (len(profiles) == 1):
            profile_ids = int(profiles['0'])
        else:
            for x in profiles:
                profile_ids.append(int(profiles[x]))
            profile_ids = tuple(profile_ids)

        with connection.cursor() as cursor:
            if(len(profiles) == 1):
                sql = """SELECT authapi_user.id, authapi_user.first_name, authapi_user.last_name, authapi_user.about_me, authapi_user.username FROM authapi_user WHERE authapi_user.id = {} """
            elif (len(profiles) > 1):
                sql = """SELECT authapi_user.id, authapi_user.first_name, authapi_user.last_name, authapi_user.about_me, authapi_user.username FROM authapi_user WHERE authapi_user.id IN {}"""
            else:
                sql = """SELECT authapi_user.id, authapi_user.first_name, authapi_user.last_name, authapi_user.about_me, authapi_user.username FROM authapi_user WHERE authapi_user.id"""

            sql = sql.format(profile_ids)
            cursor.execute(sql)
            table = cursor.fetchall()
            return Response(table)


class DeleteFollower(APIView):

    def post(self, request):
        followerr_id = request.data['follower_id']
        followedd_id = request.data['followed_id']
        removeFollow = Follower.objects.filter(
            follower_id=followerr_id, followed_id=followedd_id)
        removeFollow.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
