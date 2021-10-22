from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post, Comment, Category

class CategorySerializer(serializers.ModelSerializer):
  owner = serializers.ReadOnlyField(source='owner.username')
  # if u not write above line then u will only get id of owner in api 
  post = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

  class Meta:
    model = Category
    fields = ['id','name', 'owner', 'post'] 
#     # one big bug is not using [] in field of serializers when writing individually

class CommentSerializer(serializers.ModelSerializer): 
  owner = serializers.ReadOnlyField(source='owner.username')
  class Meta: 
    model = Comment
    fields = ['id','body', 'owner', 'post']

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)


    class Meta:
        model = Post
        # fields = ['id', 'title', 'body', 'owner']
        fields = ['id', 'title', 'body', 'owner', 'comments', 'categories']

class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    categories = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        # fields = ['id', 'username', 'posts']
        fields = ['id', 'username', 'posts', 'comments', 'categories']


# there seems to be a pattern only for owner write custom serilizer field 
# ( if you don't then you have to choose ) others no
#  but if custom field come like many = true or read only = true then write else default 
# user /owner k liye u have to write coz each owner is associated with certain 
