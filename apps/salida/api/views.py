from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.salida.models import Post
from apps.salida.api.serializers import SalidaSerializer


class SalidaApiView(APIView):
    def get(self, request):
        serializer = SalidaSerializer(Post.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data,)

    def post(self, request):
        serializer = SalidaSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(status=status.HTTP_201_CREATED, data=serializer.data)

# Create your views here.