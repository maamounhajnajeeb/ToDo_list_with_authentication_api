from django.urls import path

from . import views

app_name = "todos"

urlpatterns = [
    # tasks [add task, read all]
    path("api/v1/tasks/", views.TasksView.as_view(), name="task-api"),
    path("create-task/", views.create_task, name="task-view"),
    
    # [Read, Delete, Update] specific task
    path("api/v1/task/<int:id>/", views.SpecificTask.as_view(), name="specifci-task-api"),
    # path("api/v1/task/<int:id>/", views.SpecificTask.as_view(), name="specifci-task-api"),
]
