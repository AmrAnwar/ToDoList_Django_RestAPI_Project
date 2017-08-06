from rest_framework import serializers

from ..models import Task, Sublist, Comment
from .sublist_serializer import SubListModelSerializer
from .comment_serializer import CommentModelSerializer


class TaskFullModelSerializer(serializers.ModelSerializer):
    sublist = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = ('id', 'user', 'title', 'timestamp', 'archived', 'sublist', 'comments')

    def get_sublist(self, obj):
        qs = Sublist.objects.filter(task=obj)
        qs_serializer = SubListModelSerializer(qs, many=True).data
        return qs_serializer

    def get_comments(self, obj):
        qs = Comment.objects.filter(task=obj)
        qs_serializer = CommentModelSerializer(qs, many=True).data
        return qs_serializer
