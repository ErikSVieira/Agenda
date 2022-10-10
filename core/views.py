from django.shortcuts import redirect, render, HttpResponse  # , redirect
from core.models import Event
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import datetime, timedelta


# Create your views here.
def login_user(request):
    return render(request, 'login.html')


def submit_login(request):
    try:
        if request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'Invalid username or password.')
    except Exception:
        messages.error(request, 'Operation Invalid!')
    finally:
        return redirect('/')


def logout_user(request):
    logout(request)
    return redirect('/')


@login_required(login_url='/login/')
def list_event(request):
    events = request.GET.get('events')
    try:
        user = request.user
        today = datetime.now() - timedelta(hours=1)
        if events == 'old':
            events = Event.objects.filter(user=user,
                date_event__lt=today).order_by('date_event')
        elif events == 'all':
            events = Event.objects.all().order_by('date_event')
        else:
            events = Event.objects.filter(user=user,
                date_event__gt=today).order_by('date_event')
    except Exception:
        messages.error(request, 'Failed to list events.')
    finally:
        data = {'events': events}
        return render(request, 'event.html', data)



@login_required(login_url='/login/')
def evento(request):
    id_event = request.GET.get('id')
    dados = {}
    try:
        if id_event:
            user = request.user
            event = Event.objects.get(id=id_event)
            if user == event.user:
                dados['event'] = Event.objects.get(id=id_event)
            else:
                messages.error(request, 'Event not registered!!!')
    except Exception:
        messages.error(request, 'Edit error - Operation Invalid!')
    finally:
        return render(request, 'evento.html', dados)


@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        try:
            title = request.POST.get('titulo')
            date_event = request.POST.get('data_evento')
            description = request.POST.get('description')
            user = request.user
            id_event = request.POST.get('id_event')
            if title == '' or description == '' or date_event == '':
                messages.error(
                    request, 'Invalid title or event date or description')
                return redirect('/event/event/')
            elif id_event:
                event = Event.objects.get(id=id_event)
                if user == event.user:
                    event.title = title
                    event.description = description
                    event.date_event = date_event
                    event.save()
                    messages.success(request, 'Event edited successfully')
                else:
                    messages.error(request, 'Edit failed. Invalid ID!')
            else:
                Event.objects.create(
                    title=title,
                    date_event=date_event,
                    description=description,
                    user=user
                )
                messages.success(request, 'Event created successfully')
        except Exception:
            messages.error(request, 'Operation Invalid!')
    else:
        messages.error(request, 'Method not identified. Internal error!')
    return redirect('/')


@login_required(login_url='/login/')
def delet_event(request, id_event):
    try:
        user = request.user
        event = Event.objects.get(id=id_event)
        if user == event.user:
            event.delete()
            messages.success(request, 'Event deleted successfully')
        else:
            messages.error(request, 'Operation not authorization!')
    except Exception:
        messages.error(request, 'Event was not deleted. Error not identified!')
    finally:
        return redirect('/')
