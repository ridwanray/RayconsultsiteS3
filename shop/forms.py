from django import forms

from django.forms.models import modelformset_factory


from .models import Variation, Category


CAT_CHOICES = (
	('electronics', 'Electronics'),
	('accessories', 'Accessories'),
	('rand', 'Rand'),
)

class ProductFilterForm(forms.Form):
	category_id = forms.ModelMultipleChoiceField(
		label='CATEGORIES',
		queryset=Category.objects.all(),
		widget=forms.CheckboxSelectMultiple,
		required=False)
	# category_title = forms.ChoiceField(
	# 	label='Category',
	# 	choices=CAT_CHOICES,
	# 	widget=forms.CheckboxSelectMultiple,
	# 	required=False)
	max_price = forms.DecimalField(decimal_places=2, max_digits=12, required=False)
	min_price = forms.DecimalField(decimal_places=2, max_digits=12, required=False)



class VariationInventoryForm(forms.ModelForm):
	class Meta:
		model = Variation
		fields = [
			"price",
			"sale_price",
			"inventory",
			"active",
		]


VariationInventoryFormSet = modelformset_factory(Variation, form=VariationInventoryForm, extra=0)