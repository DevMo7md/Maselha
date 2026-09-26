from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Word(models.Model):
    text = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class SuggestedWord(models.Model):
    text = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.text

class DifficultyLevel(models.Model):
    name = models.CharField(max_length=50)
    time_limit = models.IntegerField(help_text="Time limit in seconds")

    def __str__(self):
        return self.name