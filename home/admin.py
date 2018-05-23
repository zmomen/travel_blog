from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from home.models import Friend, Blog, Comment


class BlogAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    model = Blog
    fieldsets = [
        ('Blog Title', {'fields': ['title']}),
        ('Blog', {'fields': ['blog']}),
    ]
    summernote_fields = 'blog'
    list_display = ('title', 'user', 'created', 'updated')


# Register your models here.
admin.site.register(Friend)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)

