from django.contrib import admin
from .models import Book , Writer , ParentCategory , Category , Comment , Contact
# Register your models here.


class WriterInline(admin.StackedInline):
    model = Book
    
class CommentInline(admin.StackedInline):
    model = Comment
    
class WriterAdmin(admin.ModelAdmin):
    inlines = [WriterInline]
    list_display = ['name', 'bio']
    search_fields = ['name']


class BookAdmin(admin.ModelAdmin):
    inlines = [CommentInline]
    list_display = ['title', 'price', 'show', 'writer', 'parent_category' , 'category']
    list_filter = ['show', 'parent_category']
    search_fields = ['title', 'parent_category']
    actions = ['show_on']

    @admin.action(description='show selected books')
    def show_on(model_admin, request, queryset):
        queryset.update(show=True)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent_category_name']

    def parent_category_name(self, obj):
        return obj.parent_category.name if obj.parent_category else "not selected"
    
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject']
    

admin.site.register(Book , BookAdmin)
admin.site.register(Writer , WriterAdmin)
admin.site.register(ParentCategory)  
admin.site.register(Category , CategoryAdmin)  
admin.site.register(Comment)
admin.site.register(Contact,ContactAdmin)



