# Generated by Django 2.2.1 on 2019-05-22 17:26

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('communityassets', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='communityasset',
            old_name='name',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='communityasset',
            name='contact_name',
            field=models.CharField(blank=True, help_text='The email address for this community service', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='communityasset',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='The contact phone number for this community service, without spaces', max_length=128, null=True, region=None),
        ),
    ]