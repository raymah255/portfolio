from pyexpat import model
from attr import fields
from rest_framework import serializers
from portifolio.models import Comment, Post, Notifacation
from profiles.api.serializers import PublicProfileSerializer


class ChildCommentSerializers(serializers.ModelSerializer):
    user = PublicProfileSerializer(source="user.profile", read_only=True)
    class Meta:
        model = Comment
        fields=["id", "user", "content", "parent", "is_parent"]
 

class CommentCreateSerializers(serializers.ModelSerializer):
    user = PublicProfileSerializer(source="user.profile", read_only=True)
    class Meta:
        model = Comment
        fields=["post", "user", "content", "parent"]
    
    

class CommentSerializers(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()
    user = PublicProfileSerializer(source="user.profile", read_only=True)
    count = serializers.SerializerMethodField(read_only=True)
    

    class Meta:
        model = Comment
        fields=["id", "post", "user",  "content", "is_parent", "count",  "replies",]
    
    def get_replies(self, obj):
        if obj.is_parent:
            return ChildCommentSerializers(obj.children(), many=True).data
        return None
    
    def get_count(self, obj):
        return obj.comments().count()
    

class PostCreateSerializer(serializers.ModelSerializer):
    user = PublicProfileSerializer(source="user.profile", read_only=True)
    class Meta:
        model = Post
        fields=["id", "title","user", "content", "image", ]
    
    
class PostSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()
    user = PublicProfileSerializer(source="user.profile", read_only=True)
    count = serializers.SerializerMethodField(read_only=True)
    likes = serializers.SerializerMethodField(read_only=True)
    is_like = serializers.SerializerMethodField(read_only=True)
    image = serializers.SerializerMethodField(read_only=True)
    request_user = serializers.SerializerMethodField(read_only=True)
   
    class Meta:
        model = Post
        fields=["id", "request_user", "title", "likes", "is_like", "user", "content", "image", "count", "comments", "slug"]
    
    def get_comments(self, obj):
        return CommentSerializers(Comment.objects.filter(parent=None, post=obj.id), many=True).data
    

    def get_count(self, obj):
        return Comment.objects.filter(post=obj.id).count()
    
    def get_likes(self, obj):
        return obj.like.count()

    def get_image(self, obj):
        return obj.image.url
    
    def get_request_user(self, obj):
        context = self.context
        request = context.get("request")
        return request.user.username
        
    def get_is_like(self, obj):
        is_like = False
        context = self.context
        request = context.get("request")
        if request:
            user = request.user
            is_like = user in obj.like.all()
        return is_like


class LikePostSerializer(serializers.Serializer):
    id = serializers.IntegerField()


class NotificationSerializers(serializers.ModelSerializer):
    to_user = PublicProfileSerializer(source="to_user.profile", read_only=True)
    from_user = PublicProfileSerializer(source="from_user.profile", read_only=True)
    class Meta:
        model=Notifacation
        fields=["id", "notification_type", "to_user", "from_user", "post", "comment", "user_has_seen"]

class CreateNotificationSerializers(serializers.ModelSerializer):
    to_user = PublicProfileSerializer(source="to_user.profile", read_only=True)
    from_user = PublicProfileSerializer(source="from_user.profile", read_only=True)
    class Meta:
        model=Notifacation
        fields=["id", "notification_type", "to_user", "from_user", "post", "comment", "user_has_seen"]