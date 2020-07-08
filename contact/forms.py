from django	import	forms
from .models import Contact
class Contactform(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name','content','subject','email']

    def __init__(self, *args, **kwargs):
        super(Contactform, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'placeholder': 'Enter your name'})
        self.fields['content'].widget.attrs.update({'placeholder': 'Message'})
        self.fields['subject'].widget.attrs.update({'placeholder': 'Subject'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Enter Your Email'})
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
#def __init__(self, *args, **kwargs):
#super(Contactform, self).__init__(*args, **kwargs)
# self.fields['name'].widget.attrs.update({'placeholder': 'Enter a name'})
#name=forms.CharField(max_length=30,
#widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your Name', 'data-msg':'Please enter at least 4 chars', 'data-rule':'minlen:4'}))
#subject=forms.CharField(max_length=60,
#widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Subject', 'data-msg':'Please enter at least 8 chars of subject', 'data-rule':'minlen:4'}))
#content=forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Message', 'data-msg':'Please write something for us', 'data-rule':'required'}))
#email=forms.EmailField(max_length=254,
#widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your Email', 'data-msg':'Please enter a valid email', 'data-rule':'email'}))