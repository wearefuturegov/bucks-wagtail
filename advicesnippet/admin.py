from django.contrib import admin
from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register
)
from .models import AdviceSnippet

# Register your models here.
class AdviceSnippetAdmin(ModelAdmin):
    model = AdviceSnippet
    menu_label = "Advice snippets"
    menu_icon = "site"
    menu_order = 10
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("title", "url", "description")
    search_fields = ("title", "url", "description")
    list_filter = ("title", "url", "description")

    # index_template_name = 'index.html'

modeladmin_register(AdviceSnippetAdmin)

admin.site.register(AdviceSnippet)