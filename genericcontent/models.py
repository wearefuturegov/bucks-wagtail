from django.db import models
from wagtail.core.models import Page, Orderable
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, InlinePanel, FieldRowPanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import StreamField
from wagtail.api import APIField
from modelcluster.fields import ParentalKey
from django.forms import CheckboxInput

from streams import blocks


class ExternalLinks(Orderable):
    page = ParentalKey("genericcontent.GenericContent", related_name="external_links")

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


class GenericContent(Page):
    summary = models.CharField(max_length=200, blank=False, null=True, help_text="A short summary of the page that appears on the homepage and in search results")
    intro = models.CharField(max_length=400, blank=False, null=True, help_text="Appears under the title")
    popular_advice = models.BooleanField(null=True, blank=True, help_text="Show this page as popular advice on the homepage?")
    popular_search = models.BooleanField(null=True, blank=True, help_text="Show this page as a popular search on the homepage?")

    content = StreamField(
        [
            ("rich_text", blocks.RichTextBlock()),
            ("person_profile", blocks.PersonProfileBlock()),
            ("call_to_action", blocks.CallToActionButton()),
            ("financial_help_checker", blocks.FinancialHelpChecker()),
        ],
        null=True,
        blank=True
    )

    api_fields = [
        APIField("summary"),
        APIField("intro"),
        APIField("content"),
        APIField("popular_advice"),
        APIField("popular_search"),
    ]

    content_panels = Page.content_panels + [
        FieldPanel("summary"),
        FieldPanel("intro"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel("popular_advice", widget=CheckboxInput),
                FieldPanel("popular_search", widget=CheckboxInput)
            ]),
        ], heading="Listing on homepage"),
        StreamFieldPanel("content"),
        InlinePanel("external_links", heading="External links")
    ]