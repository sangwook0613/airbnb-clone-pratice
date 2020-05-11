from django.utils import timezone
from django.views.generic import ListView
from . import models


class HomeView(ListView):

    """ HomeView Definiton """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # super를 안부르면 컨텐츠들을 못 부른다!
        now = timezone.now()
        context["now"] = now
        return context
