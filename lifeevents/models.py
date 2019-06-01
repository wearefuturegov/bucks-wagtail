from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import StreamField
from wagtail.api import APIField

from streams import blocks

# Create your models here.
class LifeEventPage(Page):
    parent_page_types = ["home.HomePage"]

    summary = models.CharField(max_length=200, blank=False, null=True, help_text="A short summary of the page that appears on the homepage and in search results")
    intro = models.CharField(max_length=400, blank=False, null=True, help_text="Appears under the title")

    content = StreamField(
        [
            ("rich_text", blocks.RichTextBlock()),
            ("person_profile", blocks.PersonProfileBlock()),
            ("learn_more", blocks.LearnMoreBlock()),
        ],
        null=True,
        blank=True
    )

    api_fields = [
        APIField("summary"),
        APIField("intro"),
        APIField("content")
    ]

    content_panels = Page.content_panels + [
        FieldPanel("summary"),
        FieldPanel("intro"),
        StreamFieldPanel("content")
    ]

    class Meta:
        verbose_name = "Life event"
        verbose_name_plural = "Life events"