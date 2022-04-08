from pyexpat import model
from rest_framework import serializers
from django.contrib.auth import get_user_model
from profiles.api.serializers import PublicProfileSerializer


User = get_user_model()

class UserSerializers(serializers.ModelSerializer):
    user_prof = PublicProfileSerializer(source="user.profile", read_only=True)
    class Meta:
        model = User
        fields = ["user_prof"]