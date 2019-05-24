from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, FieldRowPanel
from phonenumber_field.modelfields import PhoneNumberField
from django.forms import Select, CheckboxSelectMultiple, CheckboxInput


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


class CommunityAsset(models.Model):
    name = models.CharField(blank=False, null=True, max_length=200)
    parent_organisation = models.CharField(blank=False, null=True, max_length=200, help_text="The parent organisation delivering this service, if applicable")
    description = models.TextField(blank=False, null=True, max_length=500, help_text="Describe the service in a short paragraph")
    price = models.DecimalField(max_digits=6, blank=True, null=True, decimal_places=2, help_text="Give a cost per session/activity. If a simple price cannot be given, leave the field blank.", verbose_name="Cost (£)")
    
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True, blank=False, default="")
    # KEYWORDS
    age_groups = models.ManyToManyField(AgeGroups, blank=True)
    suitability = models.ManyToManyField(Suitabilities, blank=True)
    accessibility = models.ManyToManyField(Accessibilities, blank=True)

    venue = models.CharField(blank=True, null=True, max_length=100)
    area = models.CharField(blank=True, null=True, max_length=100)
    postcode = models.CharField(blank=True, null=True, max_length=100)

    days = models.ManyToManyField(Days, blank=True)
    frequency = models.CharField(blank=True, null=True, max_length=100, help_text="Describe the frequency of this event if applicable. For example 'daily' or 'fortnightly'")
    daytime = models.BooleanField(blank=True, null=True, help_text="Does this service happen during the daytime (between 9-5)?", default=False, verbose_name="During daytime?")

    contact_name = models.CharField(blank=True, null=True, max_length=100, help_text="Give the name of a person involved with this service")
    email = models.EmailField(blank=True, null=True, max_length=100, help_text="Give a contact email address")
    phone = PhoneNumberField(blank=True, null=True, help_text="Give a contact telephone number, with no spaces")
    url = models.URLField(blank=True, null=True, help_text="The website or webpage where this service can be booked, or where more info can be found about it", verbose_name="Website URL")
    
    # REVIEW NOTES
    # ASSIGNED TO
    # REVIEW NUMBER
    # REVIEW STATUS
    # LAST UPDATED
    # REVIEW DATE

    # LAF AREAS
    # CCG LOCALITY

    # VOLUNTEERS DBS CHECKED?
    # SAFEGUARDING
    # HEALTH AND SAFETY
    # INSURANCE

    # CLO NOTES

    # LEGACY CATEGORIES




    panels = [

        MultiFieldPanel([
            FieldPanel('name'),
            FieldPanel('parent_organisation'),
            FieldPanel('description'),
            FieldPanel('price'),
        ]),

        MultiFieldPanel([
            FieldPanel('category', widget=Select),
            # ...
            FieldPanel('age_groups', widget=CheckboxSelectMultiple),
            FieldPanel('suitability', widget=CheckboxSelectMultiple),
            FieldPanel('accessibility', widget=CheckboxSelectMultiple),
        ], heading="Discovery"),

        MultiFieldPanel([
            FieldPanel('days', widget=CheckboxSelectMultiple),
            FieldRowPanel([
                FieldPanel('daytime'),
                FieldPanel('frequency')
            ]),
        ], heading="When?"),

        MultiFieldPanel([
            FieldPanel('venue'),
            FieldPanel('area'),
            FieldPanel('postcode')
        ], heading="Where?"),

        MultiFieldPanel([
            FieldPanel('contact_name'),
            FieldRowPanel([
                FieldPanel('phone'),
                FieldPanel('email')
            ]),
            FieldPanel('url'),
        ], heading="Contact details")

        # MultiFieldPanel([

        # ], heading="Internal")
    ]

    def __str__(self):
        return self.name