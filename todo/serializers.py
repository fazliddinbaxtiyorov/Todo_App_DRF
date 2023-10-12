from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'


class ChooseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'title']
