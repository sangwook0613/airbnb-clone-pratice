from math import ceil
from django.shortcuts import render
from django.core.paginator import Paginator
from . import models


def all_rooms(request):
    page = request.GET.get("page", 1)
    room_list = models.Room.objects.all()
    paginator = Paginator(
        room_list, 10, orphans=5
    )  # orphans는 그 수 이하의 아이템들이 남았을때, 새로운 페이지를 만들지 않고 가장 마지막 페이지에 합쳐줌, 여기서 만약 마지막 페이지가 6개가 남았다면 새로운 페이지로 유지된다.
    rooms = paginator.page(int(page))
    print(vars(rooms.paginator))
    return render(request, "rooms/home.html", {"page": rooms})
