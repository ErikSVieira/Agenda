from django.shortcuts import render, HttpResponse  # , redirect
from core.models import Event

# Create your views here.


def list_event(request):
    # user = request.user
    # events = Event.objects.filter(user=user)
    events = Event.objects.all()
    data = {'events': events}
    return render(request, 'event.html', data)


def list_poll(request):
    return HttpResponse("Hello, world. You're at the polls index.")


# def index(request):
#     return redirect('/event')
