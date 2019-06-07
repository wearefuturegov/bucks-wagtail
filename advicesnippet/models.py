from django.db import models
from wagtail.admin.edit_handlers import FieldPanel


class AdviceSnippet(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    url = models.URLField(blank=True, null=True)

    panels = [
        FieldPanel('title'),
        FieldPanel('url'),
        FieldPanel('description')
    ]

    def __str__(self):
        return self.title