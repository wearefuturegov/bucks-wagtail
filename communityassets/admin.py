from django.contrib import admin

from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register
)

from .models import CommunityAsset

# Register your models here.
class CommunityAssetAdmin(ModelAdmin):
    model = CommunityAsset
    menu_label = "Community Services"
    menu_icon = "site"
    menu_order = 10
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("name", "parent_organisation", "category", "description", "review_status")
    search_fields = ("name", "parent_organisation", "category__name", "description")
    list_filter = ("category", "review_status", "assigned_to")

    index_template_name = 'index.html'

modeladmin_register(CommunityAssetAdmin)


admin.site.register(CommunityAsset)