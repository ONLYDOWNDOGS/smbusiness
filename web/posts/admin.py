from django.contrib import admin

from .models import BlogPost, Announcement


class BlogPostInline(admin.TabularInline):
    model = BlogPost
    extra = 1

class AnnouncementAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                  {'fields': ['announcement_text']}),
        ('Date Information',    {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [BlogPostInline]
    list_display = ('announcement_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['announcement_text']

admin.site.register(Announcement, AnnouncementAdmin)