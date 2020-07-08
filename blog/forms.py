from django	import	forms
class Contactform(forms.Form):
    name=forms.CharField(max_length=30)
    subject=forms.CharField(max_length=60)
    content=forms.CharField(max_length=500, widget=forms.TextInput({}))
    email=forms.EmailField(max_length=254)