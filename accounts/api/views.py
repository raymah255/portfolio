from rest_framework.response import Response
from .serializers import User, UserSerializers
from rest_framework.decorators import api_view


@api_view(["GET"])
def user_serilazers_views(request, *args, **kwargs):
    qs = User.objects.all()
    serializer = UserSerializers(qs, many=True)
    return Response(serializer.data, status=200)