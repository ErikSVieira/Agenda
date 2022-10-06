from django.shortcuts import redirect, render, HttpResponse  # , redirect
from core.models import Event
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def login_user(request):
    return render(request, 'login.html')


def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Invalid username or password')
    return redirect('/')


def logout_user(request):
    logout(request)
    return redirect('/')


@login_required(login_url='/login/')
def list_event(request):
    user = request.user
    events = Event.objects.filter(user=user)
    # events = Event.objects.all()
    data = {'events': events}
    return render(request, 'event.html', data)


def list_poll(request):
    return HttpResponse("Hello, world. You're at the polls index.")


# def index(request):
#     return redirect('/event')


@login_required(login_url='/login/')
def evento(request):
    return render(request, 'evento.html')


@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        try:
            title = request.POST.get('titulo')
            date_event = request.POST.get('data_evento')
            description = request.POST.get('description')
            user = request.user
            if title == '' or description == '' or date_event == '':
                messages.error(
                    request, 'Invalid title or date event or description')
            else:
                Event.objects.create(
                    title=title,
                    date_event=date_event,
                    description=description,
                    user=user
                )
                messages.success(request, 'Created Event with Success')
        except:
            messages.error(request, 'Operation Invalid')
        finally:
            return redirect('/event/event')
    else:
        messages.error(request, 'Not saved. Error not identified!')
