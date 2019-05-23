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


class CommunityAsset(models.Model):
    name = models.CharField(blank=False, null=True, max_length=200)
    parent_organisation = models.CharField(blank=False, null=True, max_length=200, help_text="The parent organisation delivering this service, if applicable")
    description = models.TextField(blank=False, null=True, max_length=500, help_text="Describe the service in a short paragraph")
    url = models.URLField(blank=True, null=True, help_text="The website or webpage where this service can be booked, or where more info can be found about it", verbose_name="Website URL")
    cost = models.DecimalField(max_digits=6, blank=True, null=True, decimal_places=2, help_text="Give a cost per session/activity. If a simple price cannot be given, leave the field blank.", verbose_name="Cost (£)")
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True, blank=False, default="")
    
    days = models.ManyToManyField(Days, blank=True)
    frequency = models.CharField(blank=True, null=True, max_length=100, help_text="Describe the frequency of this event if applicable. For example 'daily' or 'fortnightly'")
    daytime = models.BooleanField(blank=True, null=True, help_text="Does this service happen during the daytime (between 9-5)?", default=False, verbose_name="During daytime?")

    venue = models.CharField(blank=True, null=True, max_length=100)
    postcode = models.CharField(blank=True, null=True, max_length=100)

    contact_name = models.CharField(blank=True, null=True, max_length=100, help_text="Give the name of a person involved with this service")
    phone = PhoneNumberField(blank=True, null=True, help_text="Give a contact telephone number, with no spaces")
    email = models.EmailField(blank=True, null=True, max_length=100, help_text="Give a contact email address")
    
    panels = [
        MultiFieldPanel([
            FieldPanel('name'),
            FieldPanel('parent_organisation'),
            FieldPanel('description'),
            FieldPanel('url'),
            FieldPanel('cost'),
            FieldPanel('category', widget=Select)
        ], heading="About the service"),

        MultiFieldPanel([
            FieldPanel('days', widget=CheckboxSelectMultiple),
            FieldRowPanel([
                FieldPanel('daytime'),
                FieldPanel('frequency')
            ]),
        ], heading="When?"),

        MultiFieldPanel([
            FieldPanel('venue'),
            FieldPanel('postcode')
        ], heading="Where?"),

        MultiFieldPanel([
            FieldPanel('contact_name'),
            FieldRowPanel([
                FieldPanel('phone'),
                FieldPanel('email')
            ])
        ], heading="Contact details")
    ]

    def __str__(self):
        return self.name