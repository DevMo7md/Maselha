from rest_framework import serializers
from .models import Word, SuggestedWord, Category, DifficultyLevel

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class WordSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Word
        fields = ['id', 'text', 'category']

class SuggestedWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuggestedWord
        fields = ['id', 'text', 'category']


class DifficultyLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DifficultyLevel
        fields = '__all__'