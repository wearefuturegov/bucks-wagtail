from django.contrib import admin

from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register
)

from .models import CommunityAsset

# Register your models here.
class CommunityAssetAdmin(ModelAdmin):
    model = CommunityAsset
    menu_label = "Community Assets"
    menu_icon = "site"
    menu_order = 10
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("name", "parent_organisation", "description")
    search_fields = ("name", "parent_organisation", "description")

modeladmin_register(CommunityAssetAdmin)
