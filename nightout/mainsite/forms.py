from django import forms
from datetimepicker.widgets import DateTimePicker

class EventForm(forms.Form):
    eventName = forms.CharField(label='Event Name', max_length=100)
    local = forms.CharField(label='Local', max_length=100)
    date = forms.DateTimeField(widget=forms.widgets.TimeInput(attrs={'type': 'time'}))

    descr = forms.CharField()
    private = forms.BooleanField()
    price = forms.IntegerField()
