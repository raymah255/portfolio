from django.http import Http404
from django.shortcuts import redirect, render
from .serializers import CommentCreateSerializers, NotificationSerializers, PostCreateSerializer, CommentSerializers, PostSerializer, LikePostSerializer
from portifolio.models import Comment, Post, Notifacation
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


@api_view(["GET"])
def post_list_views(request, *args, **kwargs):
    qs = Post.objects.all()
    serializers = PostSerializer(qs, many=True, context={"request": request})
    return Response(serializers.data)

@api_view(["GET"])
def feed_list_views(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("/accounts/login")

    me = request.user
    profile = me.following.all() 
    other_user_following_id = []
    if profile.exists():
        other_user_following_id = [x.id for x in profile]
    other_user_following_id.append(me.id)
    qs = Post.objects.filter(user__id__in=other_user_following_id)
    serializers = PostSerializer(qs, many=True, context={"request": request})
    return Response(serializers.data)

@api_view(["GET"])
def comment_list_views(request,  *args, **kwargs):
    qs = Comment.objects.all()
    serializers = CommentSerializers(qs, many=True, context={"request": request})
    return Response(serializers.data)

@api_view(["GET"])
def post_detail_views(request, slug,  *args, **kwargs):
    qs = Post.objects.filter(slug=slug)
    if not qs.exists():
        return Response({"detal": "Post not found"}, status=404)
    post_obj = qs.first()
    data = PostSerializer(instance=post_obj, context={"request": request})
    return Response(data.data, status=200)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def post_create_view(request, *args, **kwargs):
    serializer = PostCreateSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data, status=201)
    return Response({}, status=400)


@api_view(["POST", "GET"])
@permission_classes([IsAuthenticated])
def create_comment_views(request, *args, **kwargs):
    serializer = CommentCreateSerializers(data=request.data)
    
    if serializer.is_valid(raise_exception=True):
        instance = serializer.save(user=request.user)
        # print(instance)
        Notifacation.objects.create(notification_type=2, to_user=request.user, from_user=serializer.validated_data.get("post").user, comment=instance)
        print(serializer.initial_data)
        return Response(serializer.data)
    return Response({}, status=404)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def post_like_views(request, *args, **kwargs):
    serializers = LikePostSerializer(data=request.data)
    if serializers.is_valid():
        data = serializers.validated_data
        post_id = data.get("id")
    qs = Post.objects.filter(id=post_id)
    if not qs.exists():
        return Response({}, status=400)
    qs = qs.first()
    if request.user in qs.like.all():
        qs.like.remove(request.user)
        Notifacation.objects.create(notification_type=4, to_user=request.user, from_user=qs.user, post=qs)
    elif request.user not in qs.like.all():
        qs.like.add(request.user)
        Notifacation.objects.create(notification_type=1, to_user=request.user, from_user=qs.user, post=qs)
    serializers = PostSerializer(qs, context={"request": request})
    return Response(serializers.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def notifacation_views(request, *args, **kwargs):
    qs = Notifacation.objects.filter(from_user=request.user).exclude(user_has_seen=True)
    serializer = NotificationSerializers(qs, many=True, context={"request": request})
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def create_post_notifacation_views(request, *args, **kwargs):
    qs = Notifacation.objects.all()
    serializer = NotificationSerializers(qs, many=True)
    return Response(serializer.data)



  