from django.dispatch import receiver
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from .models import Message, User
from django.db.models import Q
import json

# Create your views here.
def chat_room(request, username, *args, **kwargs):
    other_user = get_object_or_404(User, username=username)
    message = Message.objects.filter(
        Q(receiver=other_user, sender=request.user) | Q(receiver=request.user, sender=other_user)
    )
    other_user_following = request.user.following.all()
    message.update(seen=True)
    message_list = [{"message": x.message} for x in message]
    context = {
        "messages":message_list,
        "other_user": other_user,
        "user": request.user,
        "others":other_user_following,
    }
    return render(request, "pages/chat.html", context)

def list_chat_room(request, *args, **kwargs):
    other_user_following = request.user.following.all()
    print(other_user_following)
    context = {
        "others":other_user_following
    }
    return render(request, "pages/chat_list.html", context)



