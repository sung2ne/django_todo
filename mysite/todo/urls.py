from django.urls import path

from todo import views

app_name = "todo"

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.todoCreate, name='todoCreate'),
    path('<int:todo_id>/', views.todoDetail, name='todoDetail'),
    path('<int:todo_id>/update/', views.todoUpdate, name='todoUpdate'),
    path('<int:todo_id>/delete/', views.todoDelete, name='todoDelete'),
    path('<int:todo_id>/create/', views.itemCreate, name='itemCreate'),
    path('<int:todo_id>/<int:item_id>/update/', views.itemUpdate, name='itemUpdate'),
    path('<int:todo_id>/<int:item_id>/delete/', views.itemDelete, name='itemDelete'),
]