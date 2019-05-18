from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import StreamField

# TODO
from stream import blocks

# Create your models here.
class LifeEventPage(Page):

    hero_image = models.ForeignKey(
        "wagtailimages.Image", 
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="A large, mood-setting image which fills the top of the page"
    )
    first_paragraph = models.CharField(max_length=800, blank=False, null=True, help_text="The introductory paragraph")

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