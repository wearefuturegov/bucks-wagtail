from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, FieldRowPanel
from phonenumber_field.modelfields import PhoneNumberField

class Days(models.Model):
    day = models.CharField(max_length=8)




# Create your models here.
class CommunityAsset(models.Model):

    name = models.CharField(blank=False, null=True, max_length=200, help_text="The common name of this community service")
    parent_organisation = models.CharField(blank=False, null=True, max_length=200, help_text="The parent organisation that delivers this community service")
    description = models.CharField(blank=False, null=True, max_length=500, help_text="Describe this community service in a short paragraph")
    
    url = models.URLField(blank=True, null=True, help_text="The website or webpage where this service can be booked, or where more info can be found about it")

    contact_name = models.CharField(blank=True, null=True, max_length=100, help_text="The email address for this ")
    phone = PhoneNumberField(blank=True, null=True, help_text="The contact phone number for this community service ")
    email = models.EmailField(blank=True, null=True, max_length=100, help_text="The contact email address for this community service")
    
    days = models.ManyToManyField(Days)
    
    cost = models.DecimalField(max_digits=6, blank=True, null=True, decimal_places=2, help_text="Give a value for how much this community service costs per session/activity. If a simple price cannot be given, leave the field blank.")

    # panels = [
    #     MultiFieldPanel([
    #         FieldRowPanel([
    #             FieldPanel('name'),
    #             FieldPanel('parent_organisation')
    #         ])
    #     ], heading="Testing")
    # ]

    def __str__(self):
        return self.title