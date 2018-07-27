from django.contrib import admin
from .models import Item, Project



class Item(admin.TabularInline):
    model = Item
    extra = 3

class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    #inlines = [ChoiceInline]
    list_display = ('title', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['title']

admin.site.register(Project, ProjectAdmin)
#admin.site.register(Item)
