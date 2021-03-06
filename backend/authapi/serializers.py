from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from .models import User, Tweet, Follower, AllData


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'username', 'password',
                  'first_name', 'last_name', 'about_me')


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = [
            'id',
            'pk',
            'author',
            'tweet_text',
            'created_on'
        ]


class FollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = [
            'id',
            'follower_id',
            'followed_id'
        ]


class AllDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllData
        fields = [
            'id',
            'profile_id',
            'first_name',
            'last_name',
            'tweet_text'
        ]
