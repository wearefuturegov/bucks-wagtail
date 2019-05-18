from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

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
    image = ImageChooserBlock(required=True, help_text="Add a headshot of the person")
    headline = blocks.CharBlock(required=True, max_length=200, help_text="Include the person's name")
    text = blocks.RichTextBlock(required=True, features=["bold", "italic"])

    class Meta:
        icon = "user"
        label = "Person profile"