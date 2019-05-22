from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, FieldRowPanel
from phonenumber_field.modelfields import PhoneNumberField
from django.forms import Select, CheckboxSelectMultiple

# Create your models here.
class Categories(models.Model):
    name = models.CharField(blank=False, null=False, max_length=100)
    def __str__(self):
        return self.name

class Days(models.Model):
    name = models.CharField(blank=False, null=False, max_length=100)
    def __str__(self):
        return self.name

class CommunityAsset(models.Model):

    name = models.CharField(blank=False, null=True, max_length=200, help_text="The common name of this community service")
    parent_organisation = models.CharField(blank=False, null=True, max_length=200, help_text="The parent organisation that delivers this community service")
    description = models.TextField(blank=False, null=True, max_length=500, help_text="Describe this community service in a short paragraph")
    
    # TODO:
    # Categories and keywords
    # 
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True, blank=False, default="")
    days = models.ManyToManyField(Days, blank=True)

    url = models.URLField(blank=True, null=True, help_text="The website or webpage where this service can be booked, or where more info can be found about it")

    contact_name = models.CharField(blank=True, null=True, max_length=100, help_text="The email address for this community service")
    phone = PhoneNumberField(blank=True, null=True, help_text="The contact phone number for this community service, without spaces")
    email = models.EmailField(blank=True, null=True, max_length=100, help_text="The contact email address for this community service")
    
    cost = models.DecimalField(max_digits=6, blank=True, null=True, decimal_places=2, help_text="Give a value for how much this community service costs per session/activity. If a simple price cannot be given, leave the field blank.")

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
            FieldPanel('days', widget=CheckboxSelectMultiple)
        ], heading="Scheduling"),

        MultiFieldPanel([
            FieldPanel('contact_name'),
            FieldRowPanel([
                FieldPanel('phone'),
                FieldPanel('email')
            ]),
        ], heading="Contact details")

    ]

    def __str__(self):
        return self.name