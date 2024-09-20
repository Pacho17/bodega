from rest_framework.serializers import ModelSerializer
from apps.registro.models import Post


class RegistroSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = 'nombre','categoria','cantidad','create_at'
