from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from rest_framework import serializers
from wagtail.images.models import Image

# Return custom image formats
class APIFriendlyImageChooserBlock(ImageChooserBlock):
    def get_api_representation(self, value, context=None):
        if value:
            return {
                'id': value.id,
                'title': value.title,
                'large': value.get_rendition('width-1000').attrs_dict,
                'thumbnail': value.get_rendition('fill-120x120').attrs_dict,
            }


class RichTextBlock(blocks.RichTextBlock):
    def __init__(self, required=True, help_text=None, editor='default', features=None, validators=(), **kwargs):
        super().__init__(**kwargs)
        self.features = [
            "bold", "italic", "link", "h2", "h3", "ol", "ul"
        ]

    class Meta:
        icon = "doc-full"
        label = "Rich text"


class LearnMoreBlock(blocks.StructBlock):
    cards = blocks.ListBlock(
        blocks.StructBlock([
            ("title", blocks.CharBlock(required=True, max_length=40)),
            ("description", blocks.TextBlock(required=True, max_length=200)),
            ("link_page", blocks.PageChooserBlock(required=False)),
            ("link_url", blocks.URLBlock(required=False, help_text="If the button page is selected, that will be used first"))
        ])
    )

    class Meta:
        icon = "help"
        label = "Learn more"


class PersonProfileBlock(blocks.StructBlock):
    image = APIFriendlyImageChooserBlock(required=True, help_text="A headshot of the person")
    headline = blocks.CharBlock(required=True, max_length=200, help_text="A positive headline for this story, including the person's first name")
    text = blocks.RichTextBlock(required=True, max_length=1500, features=["bold", "italic"], help_text="Aim for three short paragraphs: problem, action, result")

    class Meta:
        icon = "user"
        label = "Person profile"
