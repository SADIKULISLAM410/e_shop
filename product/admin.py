from django.contrib import admin
from product.models import Category, Product, Images
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','parents','slug','status','create_date']
    # prepopulated_fields = {'slug': ('title',)} #ai line a aktu problem ace
    list_filter = ['status']
    
class ProductImageInline(admin.TabularInline):
    model = Images
    extra = 5

class ProductAdmin(admin.ModelAdmin):
    list_display = ['category','title','slug','stock','is_available','create_date','image_tag']
    # prepopulated_fields = {'slug': ('title',)}#ai line a aktu problem ace
    list_filter = ['category']
    readonly_fields = ('image_tag',)
    inlines = [ProductImageInline]
    
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['product']


admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Images,ImagesAdmin)

# admin.site.register(Category)
# admin.site.register(Product)
# admin.site.register(Images)