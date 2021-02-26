from django.contrib.auth.models import User, Group
from rest_framework import serializers
from restApi.models import File, Post, GardenInfo, GardenHistory

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'groups']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']


class GardenInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GardenInfo
        fields = ['id', 'name', 'value', 'type']


class GardenHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GardenHistory
        fields = ['id', 'name', 'value', 'type']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'start_date', 'end_date','created','side_nav']


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['id', 'file', 'type', 'name', 'module']