from rest_framework.serializers import ModelSerializer
from api.models import TodoModel


class TodoSerializer(ModelSerializer):
    class Meta:
        model = TodoModel
        fields = ('title', 'description', 'is_completed')
