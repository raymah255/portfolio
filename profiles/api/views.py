from profiles.models import User
from .serializers import PublicProfileSerializer
from profiles.models import Profile
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated



@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def profile_views(request, username, *args, **kwargs):
    me = request.user
    qs = Profile.objects.filter(user__username=username)
    if not qs.exists():
        return Response({}, status=404)
    profile = qs.first()
    data = request.data or {}
    action = data.get("action")

    if profile.user != request.user:
        if action == "follow":
            profile.followers.add(me)
        elif action == "unfollow":
            profile.followers.remove(me)
        else:
            pass
    seralizer = PublicProfileSerializer(instance=profile, context={"request":request})
    return Response(seralizer.data)


# @api_view(['POST', 'GET'])
# @permission_classes([IsAuthenticated])
# def user_follow_view(request, username, *args, **kwargs):
#     me = request.user
#     other_user =  User.objects.filter(username=username)
#     if not other_user.exists():
#         return Response({}, status=404)
#     other_user = other_user.first().profile

#     return Response(seralizer.data, status=200)
