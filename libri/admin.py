from django.contrib import admin
from .models import *




class AuthorAdmin(admin.ModelAdmin):
    list_display=('last_name','first_name','email')
    search_fields = ('first_name', 'last_name')
    ordering=('last_name',)

class BookAdmin(admin.ModelAdmin):
        list_display = ('title', 'publisher','publication_date')
        list_filter = ('publication_date',)
        date_hierarchy = 'publication_date'
        ordering = ('-publication_date',)
        filter_horizontal = ('authors',)

# Register your models here.




admin.site.register(Publisher)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
