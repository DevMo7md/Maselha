from .models import Word, SuggestedWord, Category, DifficultyLevel
from .services.GetRandomWord import get_random_word
from rest_framework.views import APIView, Response
from .serializers import WordSerializer, SuggestedWordSerializer, CategorySerializer, DifficultyLevelSerializer
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAdminUser
# Create your views here.

class RandomWordView(APIView):
    def get(self, request):
    
        word = get_random_word()
        if word:
            serializer = WordSerializer(word)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "No words available."}, status=status.HTTP_404_NOT_FOUND)

class RandomWordByCategoryView(APIView):
    def get(self, request, category_id):
        word = get_random_word(category_id=category_id)
        if word:
            serializer = WordSerializer(word)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "No words available in this category."}, status=status.HTTP_404_NOT_FOUND)

class AddSuggestedWordView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = SuggestedWordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ApproveSuggestedWordView(APIView):
    permission_classes = [IsAdminUser]
    def post(self, request, pk):
        try:
            suggested_word = SuggestedWord.objects.get(pk=pk)
            if suggested_word.is_approved or Word.objects.filter(text=suggested_word.text, category=suggested_word.category).exists():
                return Response(
                    {"message": "Word already approved."},
                    status=status.HTTP_400_BAD_REQUEST
                )
            Word.objects.create(text=suggested_word.text, category=suggested_word.category)
            suggested_word.is_approved = True
            suggested_word.save()
            
            return Response({"message": "Word approved."}, status=status.HTTP_200_OK)
        except SuggestedWord.DoesNotExist:
            return Response({"message": "Word not found."}, status=status.HTTP_404_NOT_FOUND)

class CategoryListView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class DifficultyLevelListView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        difficulty_levels = DifficultyLevel.objects.all()
        serializer = DifficultyLevelSerializer(difficulty_levels, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

