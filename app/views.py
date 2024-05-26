from django.views import generic
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect

from app.forms import TaskForm
from app.models import Task, Tag


class IndexView(generic.ListView):
    model = Task
    paginate_by = 10
    template_name = "app/index.html"


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("app:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("app:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("app:index")


class TaskListToggleStatus(generic.View):
    def get(self, *_, pk: int) -> HttpResponse:
        task = Task.objects.get(id=pk)
        task.is_completed = not task.is_completed
        task.save()
        return HttpResponseRedirect(reverse_lazy("app:index"))


class TagListView(generic.ListView):
    model = Tag
    paginate_by = 10


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("app:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("app:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("app:tag-list")
