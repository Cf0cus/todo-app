from django.urls import path,include

from . import views

app_name = "todolist" #use app_name when you need to add it to the namespace to make use of the "url" cmd

urlpatterns = [
    path("view/", views.todo, name="todoview"),
    path("add/",views.add_task_page, name="todoadd"),
    path("save/", views.save_task, name="save"),
    path("update/",views.update_task,name='todoupdate'),
    path("edit/",views.edit_page,name="edit"),
    path("<int:task_id>/edit/", views.edit_task,name="taskedit"),
    path("<int:task_id>/save/",views.save_edit,name="editsave"),
    path("<int:task_id>/delete/",views.delete_task,name="delete"),
]