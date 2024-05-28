from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from users.serializers import UserSerializer
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from rest_framework.request import Request
from rest_framework.response import Response


class auth_check(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({'data': UserSerializer(request.user).data})


@api_view()
@permission_classes([IsAuthenticated])
@authentication_classes([BasicAuthentication])
def user(request: Request):
    return Response({'data': UserSerializer(request.user).data})
