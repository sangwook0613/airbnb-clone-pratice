from django.shortcuts import render
from . import models


def all_rooms(request):  # core urls.py에서의 이름과 같아야되며
    all_rooms = models.Room.objects.all()
    return render(
        request, "rooms/home.html", context={"rooms": all_rooms}
    )  # templates 폴더에 있는 html파일 이름과 같아야하고 context의 제목은 html에 똑같이 쓰여야한다.
