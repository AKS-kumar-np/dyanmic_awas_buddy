from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponse
from django.conf import settings
from .forms import RoomForm
from .models import Room 

PROJECT_NAME = getattr(settings, "PROJECT_NAME", "Unset Projet in Views")


# Create your views here.
def index(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms,
            'project_name': PROJECT_NAME}
    return render(request, 'homigo/index.html', context)



def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room':room}
    return render(request, 'homigo/room.html', context)


def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'form':form}
    return render(request, 'homigo/room_form.html', context)


def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST,instance=room)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'form':form}
    return render(request, 'homigo/room_form.html', context)


def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)

    if request.method == 'POST':
        room.delete()
        return redirect('index')


    return render(request, 'homigo/delete.html', {'obj':room})




def health(request):
    return HttpResponse('ok')