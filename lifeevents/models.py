from django.db import models
from wagtail.core.models import Page, Orderable
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, InlinePanel, FieldRowPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import StreamField
from wagtail.api import APIField
from modelcluster.fields import ParentalKey

from streams import blocks

class ExternalLinks(Orderable):
    page = ParentalKey("lifeevents.GenericContentPage", related_name="external_links")

    title = models.CharField(max_length=200, blank=False, null=True)
    summary = models.CharField(max_length=200, blank=False, null=True)
    link_text = models.CharField(max_length=400, blank=False, null=True)
    url = models.URLField(max_length=200, blank=False, null=True)

    panels = [
        FieldPanel("title"),
        FieldPanel("summary"),
        FieldRowPanel([
            FieldPanel("link_text"),
            FieldPanel("url"),
        ])
    ]

    api_fields = [
        APIField("title"),
        APIField("summary"),
        APIField("link_text"),
        APIField("url"),
    ]

class GenericContentPage(Page):
    parent_page_types = ["home.HomePage", "lifeevents.LifeEventPage"]

    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    summary = models.CharField(max_length=200, blank=False, null=True, help_text="A short summary of the page that appears on the homepage and in search results")
    intro = models.CharField(max_length=400, blank=False, null=True, help_text="Appears under the title")

    content = StreamField(
        [
            ("rich_text", blocks.RichTextBlock()),
            ("person_profile", blocks.PersonProfileBlock()),
            ("call_to_action", blocks.CallToActionButton()),
            ("financial_help_checker", blocks.FinancialHelpChecker()),
            ("needs_explorer", blocks.NeedsExplorer())
        ],
        null=True,
        blank=True
    )

    api_fields = [
        APIField("summary"),
        APIField("intro"),
        APIField("image"),
        APIField("content"),
        APIField("external_links")
    ]

    content_panels = Page.content_panels + [
        FieldPanel("summary"),
        FieldPanel("intro"),
        ImageChooserPanel('image'),
        StreamFieldPanel("content"),
        InlinePanel("external_links", heading="External links")
    ]


class LifeEventPage(GenericContentPage):
    parent_page_types = ["home.HomePage"]