from django import forms
from manageapp.models import rent
from manageapp.models import maintain
from manageapp.models import addevent
from manageapp.models import complain
from manageapp.models import guest


class rent_form(forms.ModelForm):
    class Meta:
        model = rent
        fields = ['Name', 'house', 'Month', 'Amount', 'pmethod']


class maintain_form(forms.ModelForm):
    class Meta:
        model = maintain
        fields = ['Name', 'house', 'Month', 'Amount', 'pmethod']


class addevent_form(forms.ModelForm):
    class Meta:
        model = addevent
        fields = ['NEvent', 'DEvent', 'DateE', 'TEvent', 'Fund', 'Venue']


class complain_form(forms.ModelForm):
    class Meta:
        model = complain
        fields = ['Name', 'ctitle', 'comp']


class guest_form(forms.ModelForm):
    class Meta:
        model = guest
        fields = ['VName', 'house', 'mobile']
