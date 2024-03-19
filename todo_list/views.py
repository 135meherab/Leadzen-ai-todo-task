from django.shortcuts import render, redirect
from .forms import TodoForm
# Create your views here.
def add_task(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.instance.user= request.user
            form.save()
            return redirect('home_page')
    else:
        form = TodoForm()

    return render(request, 'add_task.html', {'form': form})
        