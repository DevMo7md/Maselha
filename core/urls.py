from django.urls import path
from .views import *
urlpatterns = [
    path('random-word/', RandomWordView.as_view(), name='get_random_word'),
    path('random-word/<int:category_id>/', RandomWordByCategoryView.as_view(), name='get_random_word_by_category'),
    path('add-suggested-word/', AddSuggestedWordView.as_view(), name='add_suggested_word'),
    path('suggested-words/<int:pk>/approve/', ApproveSuggestedWordView.as_view(), name='approve_suggested_word'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('difficulty-levels/', DifficultyLevelListView.as_view(), name='difficulty_level_list'),
]