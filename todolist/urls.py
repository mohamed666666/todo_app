
from django.urls import path
from . import views

urlpatterns = [

    path("", views.Home, name="home"),
    path("add", views.addtask, name="addtask"),
    path("done/<taskid>",views.MarkasCompleted,name="finished"),
    path('deletecompleted',views.deleteCompleted,name='deleteCompleted')
]