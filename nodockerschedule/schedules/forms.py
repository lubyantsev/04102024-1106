from django import forms
from .models import Schedule, Event

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['name', 'password']  # Добавьте необходимые поля

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['schedule', 'when', 'where', 'who']

    def clean_when(self):
        when = self.cleaned_data.get('when')
        if not when:
            raise forms.ValidationError("Поле 'when' обязательно для заполнения.")
        return when

class PasswordForm(forms.Form):
    password = forms.CharField(max_length=100, widget=forms.PasswordInput, label='Пароль расписания')