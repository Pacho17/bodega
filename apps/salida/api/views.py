from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from apps.salida.models import Post
from apps.salida.api.serializers import SalidaSerializer


class SalidaViewSet(ViewSet):
    def list(self, request):
        serializer = SalidaSerializer(Post.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data,)
    def retrieve(self, request, pk=int):
        serializer = SalidaSerializer(Post.objects.get(pk=pk))
        return Response(status=status.HTTP_200_OK, data=serializer.data,)

    def create(self, request):
        serializer = SalidaSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(status=status.HTTP_201_CREATED, data=serializer.data)
    def update(self, request, pk=int):
        try:

            serializer = Post.objects.get(pk=pk)
            serializer=SalidaSerializer(serializer, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(status=status. HTTP_200_OK, data=serializer.data)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"Registro no enctontrado"})

    def partial_update(self, request, pk=int):
        try:
            post=Post.objects.get(pk=pk)
            serializer=SalidaSerializer(post, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        except Post.DoesNotExist:
            return Response(status= status.HTTP_400_BAD_REQUEST, data={"Registro no encontrado"})
    def destroy(self, request, pk=int):
            serializer=Post.objects.get(pk=pk)
            serializer.delete()
            return Response(status=status.HTTP_200_OK)

    def create(self, request):
        serializer=SalidaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK, data=serializer.data)

# Create your views here.

# Create your views here.