# Generated by Django 2.2.1 on 2019-05-26 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communityassets', '0020_auto_20190526_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communityasset',
            name='contact_name',
            field=models.CharField(blank=True, help_text='Give the name of a person involved with this service', max_length=150, null=True),
        ),
    ]