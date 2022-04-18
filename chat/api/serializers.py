from profiles.api.serializers import PublicProfileSerializer
from attr import fields
from chat.models import Message
from rest_framework import serializers



class MessageSerializers(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)
    sender = PublicProfileSerializer(source="sender.profile", read_only=True)
    receiver = PublicProfileSerializer(source="receiver.profile", read_only=True)
    class Meta:
        model = Message
        fields = ["user", "sender", "receiver", "seen", "message"]

    def get_user(self, obj):
        context = self.context
        request = context.get("request")
        return request.user.username

class CreateMessageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ["sender", "receiver", "message"]
