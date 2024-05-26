from django.views import generic

from app.models import Task, Tag


class IndexView(generic.ListView):
    model = Task
    paginate_by = 10
    template_name = "app/index.html"


class TagListView(generic.ListView):
    model = Tag
    paginate_by = 10
