import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from todo.models import Todo, Item

# 할일 목록, /todo/
def index(request):
    context = {}
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
        todo = Todo.objects.order_by("-id").last()
        
    # JSON 응답
    return JsonResponse({"id": todo.id, "todo_text": todo.todo_text}, status=200)

# 할일 보기, /todo/<todo_id>/
def todoDetail(request):
    return HttpResponse("todo, detail")

# 할일 수정, /todo/<todo_id>/update/
def todoUpdate(request):
    return HttpResponse("todo, update")

# 할일 삭제, /todo/<todo_id>/delete/
def todoDelete(request):
    return HttpResponse("todo, delete")

# 상세 항목 등록, /todo/<todo_id>/create/
def itemCreate(request):
    return HttpResponse("todo, create")

# 상세 항목 수정, /todo/<todo_id>/<item_id>/update/ 
def itemUpdate(request):
    return HttpResponse("todo, update")

# 상세 항목 삭제, /todo/<todo_id>/<item_id>/delete/
def itemDelete(request):
    return HttpResponse("todo, delete")