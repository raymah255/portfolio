from urllib import request
from attr import fields
from chat.models import Message
from rest_framework import serializers



class MessageSerializers(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Message
        fields = ["user", "sender", "receiver", "seen", "message"]

    def get_user(self, obj):
        context = self.context
        request = context.get("request")
        return request.user.id

class CreateMessageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ["sender", "receiver", "message"]
