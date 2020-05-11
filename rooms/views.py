from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage
from . import models


def all_rooms(request):
    page = request.GET.get("page", 1)
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10, orphans=5)

    try:
        rooms = paginator.page(int(page))
        return render(request, "rooms/home.html", {"page": rooms})
    except EmptyPage:  # EmptyPage 대신에 Exception을 두면 모든 에러에 대해서 예외처리를 함
        # 하지만, 각각의 에러에 맞게 대처하는 상황을 제시하는 것이 낫다.
        return redirect("/")
