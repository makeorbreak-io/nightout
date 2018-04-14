from django import forms
from datetimepicker.widgets import DateTimePicker

class EventForm(forms.Form):
    eventName = forms.CharField(label='Event Name', max_length=100)
    local = forms.CharField( widget=forms.TextInput(attrs={'id':'pac-input','placeholder':'Search Location'}),  label='Local', max_length=100)
    date = forms.DateTimeField(widget=forms.widgets.DateTimeInput(attrs={'type' : 'date','id':'datepicker'}))
    time = forms.DateTimeField(widget=forms.widgets.DateTimeInput(attrs={'type' : 'time','id':'timepicker'}))

    descr = forms.CharField()
    private = forms.BooleanField()
    # price = forms.IntegerField()

class NightForm(forms.Form):
    eventName = forms.CharField(label='Event Name', max_length=100)
