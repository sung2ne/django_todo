import json
from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import get_object_or_404, render
from todo.models import Todo, Item
from django.contrib.auth.decorators import login_required

# 할일 목록, /todo/
@login_required
def index(request):
    # 할일 목록 - 현재 사용자의 할일만 표시
    todoList = Todo.objects.filter(author=request.user).order_by('id')

    # 전달 내용
    context = {
        "todoList": todoList,
    }

    # 응답
    return render(request, "todo/index.html", context)

# 할일 등록, /todo/create/
@login_required
def todoCreate(request):
    if request.method == "POST":
        # 받은 값
        body = json.loads(request.body)
        todo_text = body.get('todo_text')
        
        # 데이터베이스에 할일 추가하기
        todo = Todo.objects.create(todo_text=todo_text, author=request.user)
        
        context = {
            "id": todo.id, 
            "todo_text": todo.todo_text, 
            "username": todo.author.username
        }
        
    # JSON 응답
    return JsonResponse(context, status=200)

# 할일 보기, /todo/<todo_id>/
@login_required
def todoDetail(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id, author=request.user)
    context = {
        "todo": todo,
    }
    return render(request, "todo/detail.html", context)

# 할일 수정, /todo/<todo_id>/update/
@login_required
def todoUpdate(request, todo_id):
    if request.method == "POST":
        try:
            # 받은 값
            body = json.loads(request.body)
            todo_text = body.get('todo_text')
            todo_hidden = body.get('todo_hidden')
            
            # 기존 할일 정보 - 소유자 검증 포함
            todo = get_object_or_404(Todo, pk=todo_id, author=request.user)
            
            # 할일 수정
            if todo_text:
                todo.todo_text = todo_text
            elif todo_hidden is not None:
                # 'Y'/'N' 문자열을 boolean으로 변환
                todo.hidden = (todo_hidden == 'Y')
                
            todo.save()
            
            # JSON 응답
            return JsonResponse({"id": todo.id, "todo_text": todo.todo_text}, status=200)
            
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    
    return JsonResponse({"error": "Method not allowed"}, status=405)

# 할일 삭제, /todo/<todo_id>/delete/
@login_required
def todoDelete(request, todo_id):
    if request.method == "POST":
        # 기존 할일 정보 - 소유자 검증 포함
        todo = get_object_or_404(Todo, pk=todo_id, author=request.user)
        
        # 할일 삭제
        todo.delete()
        
        # JSON 응답
        return JsonResponse({}, status=200)
        
    return JsonResponse({"error": "Method not allowed"}, status=405)

# 상세 항목 등록, /todo/<todo_id>/create/
@login_required
def itemCreate(request, todo_id):
    if request.method == "POST":
        try:
            # 받은 값
            body = json.loads(request.body)
            item_text = body.get('item_text')
            
            # 할일 소유자 검증
            todo = get_object_or_404(Todo, pk=todo_id, author=request.user)
            
            # 데이터베이스에 항목 추가하기 - author 필드 추가
            item = Item.objects.create(todo=todo, item_text=item_text, author=request.user)
            
            # JSON 응답
            return JsonResponse({"id": item.id, "item_text": item.item_text}, status=200)
            
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    
    return JsonResponse({"error": "Method not allowed"}, status=405)

# 상세 항목 수정, /todo/<todo_id>/<item_id>/update/ 
@login_required
def itemUpdate(request, todo_id, item_id):
    if request.method == "POST":
        try:
            # 받은 값
            body = json.loads(request.body)
            item_text = body.get('item_text')
            
            # 기존 상세 항목 정보 - 소유자 검증 포함
            item = get_object_or_404(Item, pk=item_id, author=request.user, todo__author=request.user)
            
            # 상세 항목 수정
            item.item_text = item_text
            item.save()
            
            # JSON 응답
            return JsonResponse({"id": item.id, "item_text": item.item_text}, status=200)
            
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    
    return JsonResponse({"error": "Method not allowed"}, status=405)

# 상세 항목 삭제, /todo/<todo_id>/<item_id>/delete/
@login_required
def itemDelete(request, todo_id, item_id):
    if request.method == "POST":
        # 기존 상세 항목 정보 - 소유자 검증 포함
        item = get_object_or_404(Item, pk=item_id, author=request.user, todo__author=request.user)
        
        # 상세 항목 삭제
        item.delete()
        
        # JSON 응답
        return JsonResponse({}, status=200)
        
    return JsonResponse({"error": "Method not allowed"}, status=405)
