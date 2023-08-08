from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from comment.models import Comment, User


class CommentCreateSerializer(ModelSerializer):
    class Meta:
        model = Comment
        exclude = ['created', ]

    def validate(self, attrs):

        if attrs["parent"]:
            if (attrs["parent"]).post != attrs["post"]:
                raise serializers.ValidationError("something went wrong")
        return attrs


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CommentListSerializer(ModelSerializer):
    replies = SerializerMethodField()
    user = UserSerializer()

    class Meta:
        model = Comment
        fields = '__all__'

    def get_replies(self, obj):
        if obj.any_children:
            return CommentListSerializer(obj.children(), many=True).data

    def validate(self, attrs):
        if attrs["parent"]:
            if (attrs["parent"]).post != attrs["post"]:
                raise serializers.ValidationError("something went wrong")
        return attrs


class CommentDeleteUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'content',
        ]
