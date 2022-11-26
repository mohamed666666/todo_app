from django.shortcuts import render

from todolist.models import task


# Create your views here.


def Home(request):
    tasks=task.objects.order_by('id')
    context={'tasks':tasks}
    return render(request,'todolist/index.html',context)