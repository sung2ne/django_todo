from django.contrib import admin
from django.urls import path, include
from todo import views as todo_view

urlpatterns = [
    path('', todo_view.index),
    path('admin/', admin.site.urls),
    path('todo/', include('todo.urls')),
    path('common/', include('common.urls')),
]