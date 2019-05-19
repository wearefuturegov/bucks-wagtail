from django.db import models

# Create your models here.
class CommunityAsset(models.Model):
    title = models.CharField(blank=False, null=True, max_length=200, help_text="The name of this community asset")
    description = models.CharField(blank=False, null=True, max_length=500)

    def __str__(self):
        return self.title