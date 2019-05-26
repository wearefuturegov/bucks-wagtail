from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, FieldRowPanel
from phonenumber_field.modelfields import PhoneNumberField
from django.forms import Select, CheckboxSelectMultiple, CheckboxInput

from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from modelcluster.models import ClusterableModel


class Categories(models.Model):
    name = models.CharField(blank=False, null=False, max_length=100)
    def __str__(self):
        return self.name

class Days(models.Model):
    name = models.CharField(blank=False, null=False, max_length=100)
    def __str__(self):
        return self.name

class AgeGroups(models.Model):
    name = models.CharField(blank=False, null=False, max_length=100)
    def __str__(self):
        return self.name

class Suitabilities(models.Model):
    name = models.CharField(blank=False, null=False, max_length=100)
    def __str__(self):
        return self.name

class Accessibilities(models.Model):
    name = models.CharField(blank=False, null=False, max_length=100)
    def __str__(self):
        return self.name

class Keywords(TaggedItemBase):
    content_object = ParentalKey(
        'CommunityAsset',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )

class ReviewStatus(models.Model):
    name = models.CharField(blank=False, null=False, max_length=100)
    def __str__(self):
        return self.name

class LAFAreas(models.Model):
    name = models.CharField(blank=False, null=False, max_length=100)
    def __str__(self):
        return self.name

class CCGLocalities(models.Model):
    name = models.CharField(blank=False, null=False, max_length=100)
    def __str__(self):
        return self.name

class LegacyCategories(models.Model):
    name = models.CharField(blank=False, null=False, max_length=100)
    def __str__(self):
        return self.name


class CommunityAsset(ClusterableModel):
    name = models.CharField(blank=False, null=True, max_length=200)
    parent_organisation = models.CharField(blank=True, null=True, max_length=200, help_text="The parent organisation delivering this service, if applicable")
    description = models.TextField(blank=False, null=True, max_length=500, help_text="Describe the service in a short paragraph")
    price = models.CharField(blank=True, null=True, max_length=100, help_text="Give a cost per session/activity. If a simple price cannot be given, leave the field blank.", verbose_name="Cost (£)")
    
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True, blank=False, default="")
    keywords = ClusterTaggableManager(through=Keywords, blank=True)
    age_groups = models.ManyToManyField(AgeGroups, blank=True)
    suitability = models.ManyToManyField(Suitabilities, blank=True)
    accessibility = models.ManyToManyField(Accessibilities, blank=True)

    venue = models.CharField(blank=True, null=True, max_length=150)
    area = models.CharField(blank=True, null=True, max_length=100)
    postcode = models.CharField(blank=True, null=True, max_length=100)

    days = models.ManyToManyField(Days, blank=True)
    frequency = models.CharField(blank=True, null=True, max_length=150, help_text="Describe the frequency of this event if applicable. For example 'daily' or 'fortnightly'")
    daytime = models.BooleanField(blank=True, null=True, help_text="Does this service happen during the daytime (between 9-5)?", default=False, verbose_name="During daytime?")

    contact_name = models.CharField(blank=True, null=True, max_length=150, help_text="Give the name of a person involved with this service")
    email = models.EmailField(blank=True, null=True, max_length=100, help_text="Give a contact email address")
    phone = models.CharField(blank=True, null=True, max_length=100, help_text="Give a contact telephone number, with no spaces")
    url = models.URLField(blank=True, null=True, help_text="The website or webpage where this service can be booked, or where more info can be found about it", verbose_name="Website URL")
    
    review_notes = models.TextField(blank=True, null=True, max_length=500)
    assigned_to = models.TextField(blank=True, null=True, max_length=500)
    review_number = models.CharField(blank=True, null=True, max_length=100)
    review_status = models.ForeignKey(ReviewStatus, on_delete=models.CASCADE, null=True, blank=False, default="")

    last_updated = models.CharField(blank=True, null=True, max_length=100)
    review_date = models.CharField(blank=True, null=True, max_length=100)

    laf_areas = models.ForeignKey(LAFAreas, on_delete=models.CASCADE, null=True, blank=True, default="", verbose_name="LAF Area")
    ccg_locality = models.ForeignKey(CCGLocalities, on_delete=models.CASCADE, null=True, blank=True, default="", verbose_name="CCG Locality")

    vol_dbs_check = models.TextField(blank=True, null=True, max_length=500, verbose_name="Volunteer DBS check")
    safeguarding = models.TextField(blank=True, null=True, max_length=500)
    health_safety = models.TextField(blank=True, null=True, max_length=500)
    insurance = models.TextField(blank=True, null=True, max_length=500)

    clo_notes = models.TextField(blank=True, null=True, max_length=500, verbose_name="CLO notes")

    legacy_categories = models.ManyToManyField(LegacyCategories, blank=True)

    panels = [

        MultiFieldPanel([
            FieldPanel('name'),
            FieldPanel('parent_organisation'),
            FieldPanel('description'),
            FieldPanel('price'),
        ]),

        MultiFieldPanel([
            FieldPanel('category', widget=Select),
            FieldPanel('keywords'),
            FieldPanel('age_groups', widget=CheckboxSelectMultiple),
            FieldPanel('suitability', widget=CheckboxSelectMultiple),
            FieldPanel('accessibility', widget=CheckboxSelectMultiple),
        ], heading="Discovery"),

        MultiFieldPanel([
            FieldPanel('days', widget=CheckboxSelectMultiple),
            FieldRowPanel([
                FieldPanel('daytime', widget=CheckboxInput),
                FieldPanel('frequency')
            ]),
        ], heading="When?"),

        MultiFieldPanel([
            FieldPanel('venue'),
            FieldRowPanel([
                FieldPanel('area'),
                FieldPanel('postcode')
            ])
        ], heading="Where?"),

        MultiFieldPanel([
            FieldPanel('contact_name'),
            FieldRowPanel([
                FieldPanel('phone'),
                FieldPanel('email')
            ]),
            FieldPanel('url'),
        ], heading="Contact details"),

        MultiFieldPanel([
                FieldPanel('review_notes'),
                FieldRowPanel([
                    FieldPanel('assigned_to'),
                    FieldPanel('review_number'),
                ]),
                FieldRowPanel([
                    FieldPanel('last_updated'),
                    FieldPanel('review_date'),
                ]),
                FieldRowPanel([
                    FieldPanel('vol_dbs_check'),
                    FieldPanel('safeguarding'),
                ]),
                FieldRowPanel([
                    FieldPanel('health_safety'),
                    FieldPanel('insurance'),
                ]),
                FieldRowPanel([
                    FieldPanel('laf_areas', widget=Select),
                    FieldPanel('ccg_locality', widget=Select),
                ]),
                FieldPanel('clo_notes'),
                FieldPanel('legacy_categories', widget=CheckboxSelectMultiple),
        ], heading="Internal")
    ]

    def __str__(self):
        return self.name