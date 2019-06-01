from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.api import APIField

class GenericContentPage(Page):

    summary = models.CharField(max_length=200, blank=False, null=True, help_text="A short summary of the page that appears on the homepage and in search results")
    intro = models.CharField(max_length=400, blank=False, null=True, help_text="Appears under the title")

    api_fields = [
        APIField("summary"),
        APIField("intro")
    ]

    content_panels = Page.content_panels + [
        FieldPanel("summary"),
        FieldPanel("intro")
    ]