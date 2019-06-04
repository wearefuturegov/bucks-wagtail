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
            "bold", "italic", "link", "h2", "h3", "ol", "ul", "hr"
        ]
    class Meta:
        icon = "doc-full"
        label = "Rich text"


class PersonProfileBlock(blocks.StructBlock):
    image = APIFriendlyImageChooserBlock(required=True, help_text="A headshot of the person")
    headline = blocks.CharBlock(required=True, max_length=200, help_text="A positive headline for this story, including the person's first name")
    text = blocks.RichTextBlock(required=True, max_length=1500, features=["bold", "italic"], help_text="Aim for three short paragraphs: problem, action, result")
    class Meta:
        icon = "user"
        label = "Person profile"


class CallToActionButton(blocks.StructBlock):
    button_text = blocks.CharBlock(required=True, max_length=200, help_text="The text displayed on the button. Should be three words or less.")
    url = blocks.CharBlock(required=True, max_length=200, help_text="The URL the button links to")
    class Meta:
        icon = "tick"
        label = "Call-to-action button"


class FinancialHelpChecker(blocks.StaticBlock):
    admin_text='Display the financial help checker',
    class Meta:
        icon = "help"
        label = "Financial help checker"

class NeedsExplorer(blocks.StaticBlock):
    admin_text='Display the needs explorer',
    class Meta:
        icon = "help"
        label = "Needs explorer"