from django import forms
from app.models import *

class BookCreate(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'