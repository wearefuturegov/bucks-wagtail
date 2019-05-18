from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import StreamField

from streams import blocks

# Create your models here.
class LifeEventPage(Page):
    parent_page_types = ["home.HomePage"]

    hero_image = models.ForeignKey(
        "wagtailimages.Image", 
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="A large, mood-setting image which fills the top of the page"
    )
    first_paragraph = models.TextField(max_length=300, blank=False, null=True, help_text="The introductory paragraph")

    content = StreamField(
        [
            ("rich_text", blocks.RichTextBlock()),
            ("person_profile", blocks.PersonProfileBlock()),
            ("learn_more", blocks.LearnMoreBlock()),
        ],
        null=True,
        blank=True
    )

    content_panels = Page.content_panels + [
        ImageChooserPanel("hero_image"),
        FieldPanel("first_paragraph"),
        StreamFieldPanel("content")
    ]

    class Meta:
        verbose_name = "Life event"
        verbose_name_plural = "Life events"