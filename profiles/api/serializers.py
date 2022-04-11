import email
from rest_framework import serializers
from profiles.models import Profile

class PublicProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.SerializerMethodField(read_only=True)
    last_name = serializers.SerializerMethodField(read_only=True)
    username = serializers.SerializerMethodField(read_only=True)
    email = serializers.SerializerMethodField(read_only=True)
    image = serializers.SerializerMethodField(read_only=True)
    is_following = serializers.SerializerMethodField(read_only=True)
    followers_count = serializers.SerializerMethodField(read_only=True)
    following_count = serializers.SerializerMethodField(read_only=True)
    is_request_user = serializers.SerializerMethodField(read_only=True)


    class Meta:
        model = Profile
        fields = ["image", "first_name", "is_request_user", "last_name", "username", "email", "location", "is_profile_pic", "is_following", "followers_count", "following_count", "post_count"]

    def get_first_name(self, obj):
        return obj.user.first_name

    def get_last_name(self, obj):
        return obj.user.last_name

    def get_username(self, obj):
        return obj.user.username
    

    def get_email(self, obj):
        return obj.user.email
    
    def get_image(self, obj):
        return obj.profile_img.url

    def get_is_request_user(self, obj):
        context = self.context
        request = context.get("request")
        if request:
            user = request.user
            if str(user) == str(obj.user.username):
                return True
            return False
    
    def get_is_following(self, obj):
        is_following = False
        context = self.context
        request = context.get("request")
        if request:
            user = request.user
            is_following =  user in obj.followers.all()
        return is_following
    
    def get_followers_count(self, obj):
        return obj.followers.count()
    
    def get_following_count(self, obj):
        return obj.user.following.count()
    
    def get_post_count(self, obj):
        return obj.post_count()

    