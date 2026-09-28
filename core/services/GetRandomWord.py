import random
from core.models import *

used_words_id = set()

def get_random_word(categories_id=None):

    words_query = Word.objects.exclude(id__in=used_words_id)

    if categories_id is not None:
        if not isinstance(categories_id, list):
            categories_id = list(categories_id)

        words_query = words_query.filter(category_id__in=categories_id)

    words = list(words_query)

    if words:
        word = random.choice(words)
        used_words_id.add(word.id)
        return word
    else:
        used_words_id.clear()
        return None
