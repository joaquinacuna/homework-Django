from django import forms

from .models import Author, Book


class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = ('name','is_female', 'ocupation','email',)

        widgets = {
            'name': forms.TextInput(attrs={'class': 'textinputclass'}),
            'ocupation': forms.TextInput(attrs={'class': 'textinputclass'}),
            'email': forms.TextInput(attrs={'class': 'emailinputclass'}),
        }


class BookForm(forms.ModelForm):

    class Meta:
        model = Book

        fields = ('date', 'name','pages','author','topic',)

        widgets = {
            'date': forms.DateField(),
            'name': forms.TextInput(attrs={'class': 'textinputclass'}),
            'pages': forms.IntegerField(),
            'topic': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
        }
