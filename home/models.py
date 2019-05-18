from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(Page):
    max_count = 1

    intro = models.CharField(max_length=400, blank=False, null=True, help_text="Appears under the title")
    hero_image = models.ForeignKey(
        "wagtailimages.Image", 
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="A large, mood-setting image which fills the top of the page"
    )

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
        ImageChooserPanel("hero_image")  
    ]