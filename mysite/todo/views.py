from django.http import HttpResponse

# 할일 목록, /todo/
def index(request):
    return HttpResponse("todo, index")

# 할일 등록, /todo/create/
def todoCreate(request):
    return HttpResponse("todo, create")

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
