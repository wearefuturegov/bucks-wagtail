from django.db import models
from wagtail.core.models import Page, Orderable
from wagtail.admin.edit_handlers import PageChooserPanel, InlinePanel
from wagtail.api import APIField
from modelcluster.fields import ParentalKey

import json

# class PopularAdvice(Orderable):
#     page = ParentalKey("home.HomePage", related_name="popular_advice")

#     popular_page = models.ForeignKey(
#         "wagtailcore.Page",
#         null=True,
#         blank=False,
#         on_delete=models.SET_NULL,
#         related_name="+",
#     )

#     panels = [
#         PageChooserPanel("popular_page"),
#     ]


#     @property
#     def summary(self):
#         return json.dumps(self.popular_page.values())

#     api_fields = [
#         APIField("popular_page"),
#         APIField("summary")
#     ]


class HomePage(Page):
    max_count = 1

    # api_fields = [
    #     APIField("popular_advice")
    # ]

    # content_panels = Page.content_panels + [
    #     InlinePanel("popular_advice", heading="Popular advice")
    # ]

