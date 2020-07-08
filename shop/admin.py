from django.contrib import admin

# Register your models here.


from .models import Product, Variation, ProductImage, Category, ProductFeatured

class ProductImageInline(admin.TabularInline):
	model = ProductImage
	extra = 0
	max_num = 10

class VariationInline(admin.TabularInline):
	model = Variation
	extra = 0
	max_num = 10


class ProductAdmin(admin.ModelAdmin):
	list_display = ['title','price' ]
	inlines = [
		ProductImageInline,
		VariationInline,
	]
	class Meta:
		model = Product


class CategoryAdmin(admin.ModelAdmin):

	class Meta:
		model = Category

class ProductImageAdmin(admin.ModelAdmin):
	#list_display = ['']

	class Meta:
		model = ProductImage


admin.site.register(Product, ProductAdmin)



#admin.site.register(Variation)

admin.site.register(ProductImage, ProductImageAdmin)

admin.site.register(Category, CategoryAdmin)

admin.site.register(ProductFeatured)