from rest_framework.serializers import ModelSerializer
from apps.salida.models import Post


class SalidaSerializer(ModelSerializer):
    class Meta:
        model=Post
        fields =[ 'id','nombre','categoria','cantidad','create_at']