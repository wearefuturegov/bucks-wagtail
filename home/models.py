from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.api import APIField

class HomePage(Page):
    max_count = 1

    def child_pages(self):
        return Page.objects.live().child_of(self)

    api_fields = [
        # APIField("child_pages")
    ]