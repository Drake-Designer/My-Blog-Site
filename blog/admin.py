from django.contrib import admin
from .models import Post, Author, Tag

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'content')
    list_filter = ('author', 'tags', 'date')


admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
