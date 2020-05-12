from django.views.generic import ListView
from django.http import Http404
from django.shortcuts import render
from . import models


class HomeView(ListView):

    """ HomeView Definiton """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"


def room_detail(request, pk):
    try:
        room = models.Room.objects.get(pk=pk)
        return render(request, "rooms/detail.html", {"room": room})
    except models.Room.DoesNotExist:
        raise Http404()  # 여기서 return이 아니라 raise다! 에러를 띄운다고 생각하자
        # 이것만 써도 장고는 404 html 파일을 render할 것(만약 있다면)
