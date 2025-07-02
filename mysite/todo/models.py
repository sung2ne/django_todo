from django.db import models
from django.contrib.auth.models import User

# 할일
class Todo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    todo_text = models.CharField(max_length=200)
    hidden = models.BooleanField(default=False)
    

# 상세 항목
class Item(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    item_text = models.CharField(max_length=200)
    