from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Schedule, Event
from .forms import ScheduleForm, EventForm, PasswordForm

def home_view(request):
    schedules = Schedule.objects.all()
    schedule_form = ScheduleForm()
    password_form = PasswordForm()

    return render(request, 'schedules/home.html', {
        'schedules': schedules,
        'schedule_form': schedule_form,
        'password_form': password_form,
    })

def create_schedule_view(request):
    if request.method == 'POST':
        schedule_form = ScheduleForm(request.POST)
        if schedule_form.is_valid():
            schedule_form.save()
            messages.success(request, 'Расписание успешно создано!')
            return redirect('home')
    else:
        schedule_form = ScheduleForm()

    return render(request, 'schedules/create_schedule.html', {
        'schedule_form': schedule_form,
    })

def open_schedule_view(request):
    if request.method == 'POST':
        password_form = PasswordForm(request.POST)
        if password_form.is_valid():
            password = password_form.cleaned_data['password']
            try:
                schedule = Schedule.objects.get(password=password)
                messages.success(request, 'Расписание успешно открыто!')
                events = Event.objects.filter(schedule=schedule)
                return render(request, 'schedules/open_schedule.html', {
                    'schedule': schedule,
                    'events': events,
                    'password_form': password_form,
                })
            except Schedule.DoesNotExist:
                messages.error(request, 'Неверный пароль! Попробуйте снова.')
    else:
        password_form = PasswordForm()

    return render(request, 'schedules/open_schedule.html', {
        'password_form': password_form,
    })