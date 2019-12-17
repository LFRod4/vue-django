from django.shortcuts import render
from django.contrib.auth.mixins import UserPassesTestMixin
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics, mixins
from django_filters import rest_framework as filters
from rest_framework.views import APIView

# UserPassesMixin to check author


from .models import Tweet, User
from .serializers import TweetSerializer
from .permissions import IsOwnerOrReadOnly

# Create your views here.


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def restricted(request, *args, **kwargs):
    return Response(data='Only for logged in user', status=status.HTTP_200_OK)


class TweetAPIView(generics.CreateAPIView, mixins.CreateModelMixin):
    lookup_field = 'pk'
    serializer_class = TweetSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return Tweet.objects.all()

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
