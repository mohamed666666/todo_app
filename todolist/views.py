from django.shortcuts import render ,redirect
from django.views.decorators.http import require_POST

from todolist.models import task


from .forms import TodoForm
# Create your views here.


def Home(request):
    tasks=task.objects.order_by('id')
    form=TodoForm()
    context={'tasks':tasks,'form':form}
    return render(request,'todolist/index.html',context)

@require_POST
def addtask(request):
    form =TodoForm(request.POST)

    new_task=task(describtion=request.POST['text'])
    new_task.save()

    return redirect('home')

def MarkasCompleted(request ,taskid):
    new_task=task.objects.get(pk=taskid)
    new_task.done=True
    new_task.save()
    return redirect('home')



def deleteCompleted(request):
    task.objects.filter(done=True).delete()

    return redirect('home')