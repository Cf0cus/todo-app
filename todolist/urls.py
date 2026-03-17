from django.urls import path,include

from . import views

app_name = "todolist" #use app_name when you need to add it to the namespace to make use of the "url" cmd

urlpatterns = [
    path("view/", views.todo, name="todoview"),
    path("add/",views.add_task_page, name="todoadd"),
    path("save/", views.save_task, name="save"),
    path("update/",views.update_task,name='todoupdate'),
]