from logging import exception
from multiprocessing import context
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from django.db.models import Q
from chat.models import Message
from chat.models import User
from .serializers import CreateMessageSerializers, MessageSerializers
from rest_framework.decorators import api_view



@api_view(['GET'])
def load_message_views(request, username, *args, **kwargs):
    other_user = get_object_or_404(User, username=username)
    message = Message.objects.filter(
        Q(receiver=other_user.id, sender=request.user.id) | Q(receiver=request.user.id, sender=other_user.id)
    )
    serializer = MessageSerializers(message, many=True, context={"request":request})
    return Response(serializer.data, status=200)

@api_view(['POST'])
def create_message_views(request, *args, **kwargs):
    user=User.objects.get(id=request.user.id)
    serializer = CreateMessageSerializers(data=request.data, context={"request":request})
    if serializer.is_valid(raise_exception=True):
        serializer.save(sender=user)
        return Response(serializer.data, status=201)
    return Response({}, status=400)