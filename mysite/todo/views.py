import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from todo.models import Todo, Item

# 할일 목록, /todo/
def index(request):
    todoList = Todo.objects.order_by('id')
    context = {
        "todoList": todoList,
    }
    return render(request, "todo/index.html", context)

# 할일 등록, /todo/create/
def todoCreate(request):
    if request.method == "POST":
        # 받은 값
        body = json.loads(request.body)
        todo_text = body.get('todo_text')
        
        # 데이터베이스에 할일 추가하기
        Todo.objects.create(todo_text=todo_text)
        
        # Todo에서 마지막 데이터 가져오기
        todo = Todo.objects.order_by("id").last()
        
    # JSON 응답
    return JsonResponse({"id": todo.id, "todo_text": todo.todo_text}, status=200)

# 할일 보기, /todo/<todo_id>/
def todoDetail(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    context = {
        "todo": todo,
    }
    return render(request, "todo/detail.html", context)

# 할일 수정, /todo/<todo_id>/update/
def todoUpdate(request, todo_id):
    if request.method == "POST":
        # 받은 값
        body = json.loads(request.body)
        todo_text = body.get('todo_text')
        
        # 기존 할일 정보
        todo = get_object_or_404(Todo, pk=todo_id)
        
        # 할일 수정
        todo.todo_text = todo_text
        todo.save()
        
    # JSON 응답
    return JsonResponse({"id": todo.id, "todo_text": todo.todo_text}, status=200)

# 할일 삭제, /todo/<todo_id>/delete/
def todoDelete(request, todo_id):
    if request.method == "POST":
        # 기존 할일 정보
        todo = get_object_or_404(Todo, pk=todo_id)
        
        # 할일 삭제
        todo.delete()
        
    # JSON 응답
    return JsonResponse({}, status=200)

# 상세 항목 등록, /todo/<todo_id>/create/
def itemCreate(request, todo_id):
    return HttpResponse("todo, create")

# 상세 항목 수정, /todo/<todo_id>/<item_id>/update/ 
def itemUpdate(request, todo_id, item_id):
    return HttpResponse("todo, update")

# 상세 항목 삭제, /todo/<todo_id>/<item_id>/delete/
def itemDelete(request, todo_id, item_id):
    return HttpResponse("todo, delete")