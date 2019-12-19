from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from .models import User, Tweet, Follower, AllData


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'username', 'password',
                  'first_name', 'last_name')


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
        field = [
            'id',
            'profile_id',
            'first_name',
            'last_name',
            'username',
            'tweet_text',
            'created_on',
            'followed_id'
        ]
