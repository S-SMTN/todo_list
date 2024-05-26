from django.views import generic

from app.models import Task


class IndexView(generic.ListView):
    model = Task
    paginate_by = 10
    template_name = "app/index.html"
