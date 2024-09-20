from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.registro.models import Post
from apps.registro.api.serializers import RegistroSerializer


class RegistroApiView(APIView):
    def get(self, request):
        serializer = RegistroSerializer(Post.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data,)

    def post(self, request):
        serializer = RegistroSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(status=status.HTTP_201_CREATED, data=serializer.data)

# Create your views here.