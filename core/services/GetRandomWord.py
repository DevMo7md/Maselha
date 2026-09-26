import random
from core.models import *

used_words_id = set()
def get_random_word(category_id=None):

    if category_id is not None:
        words = list(Word.objects.filter(category_id=category_id).exclude(id__in=used_words_id))
    else:
        words = list(Word.objects.exclude(id__in=used_words_id))

    if words:
        word = random.choice(words)
        used_words_id.add(word.id)
        return word
    else:
        used_words_id.clear()
        return None
