from django import forms
from book.models import Book
from django.contrib.auth.models import User


class BookForm(forms.ModelForm):
    author = forms.ModelChoiceField(queryset=User.objects.all(), to_field_name='username')
    class Meta:
        model = Book
        fields = "__all__"
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'file': forms.ClearableFileInput(attrs={'class': 'form-control'}),

        }