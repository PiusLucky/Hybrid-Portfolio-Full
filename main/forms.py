#forms.py
import re
from django import forms
from main.models import Stack, Portfolio, Archive, Contact


class StackForm(forms.ModelForm):
    class Meta:
        model = Stack
        fields = "__all__"

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = "__all__"

class ArchiveForm(forms.ModelForm):
    class Meta:
        model = Archive
        fields = "__all__"


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
