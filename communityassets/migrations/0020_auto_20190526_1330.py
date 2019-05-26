# Generated by Django 2.2.1 on 2019-05-26 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communityassets', '0019_auto_20190526_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communityasset',
            name='frequency',
            field=models.CharField(blank=True, help_text="Describe the frequency of this event if applicable. For example 'daily' or 'fortnightly'", max_length=150, null=True),
        ),
    ]
