from django.shortcuts import render, redirect
from todo_list.models import TodoModel
def home(request):
    if request.user.is_authenticated:
        data = TodoModel.objects.filter(user = request.user)
        return render(request, 'home.html', {'data': data})
    else:
        return render(request, 'home.html')

def complete(request, id):
    item = TodoModel.objects.get(id=id)
    item.is_complete = True
    item.save()
    return redirect('home_page')

def delete(request, id):
    item = TodoModel.objects.get(id=id)
    item.delete()
    return redirect('home_page')