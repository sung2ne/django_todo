from django.db import models

# 할일
class Todo(models.Model):
    todo_text = models.CharField(max_length=200)


# 상세 항목
class Item(models.Model):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    item_text = models.CharField(max_length=200)