from django import forms
from datetimepicker.widgets import DateTimePicker

class EventForm(forms.Form):
    title = forms.CharField(label='Event Name', max_length=100)
    local = forms.CharField( widget=forms.TextInput(attrs={'id':'pac-input','placeholder':'Search Location'}),  label='Local', max_length=100)
    date = forms.DateField(widget=forms.widgets.DateTimeInput(attrs={'type' : 'date','id':'datepicker'}))
    time = forms.TimeField(widget=forms.widgets.DateTimeInput(attrs={'type' : 'time','id':'timepicker'}))

    description = forms.CharField()
    private = forms.BooleanField()
    price = forms.IntegerField()

    # image = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': False}))


class NightForm(forms.Form):

    title = forms.CharField(label='Night Name', max_length=100)
    events = forms.CharField(widget=forms.TextInput(attrs={'id': 'userEventa', 'placeholder': 'Search Events'}), label='Events', max_length=100)
    user = forms.CharField(widget=forms.TextInput(attrs={'id': 'userSearch', 'placeholder': 'Search Users'}), label='Username', max_length=100)
    background_color = forms.CharField(widget=forms.TextInput(attrs={'type':'color'}))
    price = forms.IntegerField()
    expense_type = 