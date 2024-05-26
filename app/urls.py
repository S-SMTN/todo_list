from django.urls import path

from app.views import (
    IndexView,
    TagListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TaskListToggleStatus
)


urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("task/create", TaskCreateView.as_view(), name="task-create"),
    path(
        "task/<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task-update"
    ),
    path(
        "task/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete"
    ),
    path(
        "task/<int:pk>/toggle/",
        TaskListToggleStatus.as_view(),
        name="task-toggle"
    ),
    path("tags/", TagListView.as_view(), name="tag-list"),
]

app_name = "app"
