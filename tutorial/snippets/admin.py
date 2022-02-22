from django.contrib import admin

from .models import Snippet
# Register your models here.


class SnippetAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title', 'code', 'linenos', 'language',
                                         'style', 'owner']}),
    ]
    list_display = ('pk', 'title', 'code', 'linenos', 'language',
                    'style', 'owner', 'created')


admin.site.register(Snippet, SnippetAdmin)
