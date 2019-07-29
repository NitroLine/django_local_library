from django import forms
from .models import Book
from django.core.exceptions import ValidationError
class BookForm(forms.ModelForm):
    """title = forms.CharField(max_length=150)
    author = forms.CharField(max_length=150)
    discr = forms.CharField(widget=forms.Textarea)
    count = forms.IntegerField(required=True,max_value=50,min_value=1)
    title.widget.attrs.update({'class': 'form-control'})
    author.widget.attrs.update({'class': 'form-control'})
    count.widget.attrs.update({'class': 'form-control'})
    discr.widget.attrs.update({'class': 'form-control'})
    """
    class Meta:
        model=Book
        fields = ['title','author','discr','count','profile_image']
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'count': forms.NumberInput(attrs={'class': 'form-control'}),
            'discr': forms.Textarea(attrs={'class': 'form-control'})
        }
    def clean_count(self):
        new_count=self.cleaned_data['count']
        if int(new_count)<=0 or int(new_count)>=50:
            raise ValidationError('Число должно быть в пределах от 1 до 49')
        return new_count


    '''
    def save(self):
        newBook=Book.objects.create(
            title=self.cleaned_data['title'],
            author=self.cleaned_data['author'],
            discr=self.cleaned_data['discr'],
            count=self.cleaned_data['count']
        )
        return newBook
    '''

