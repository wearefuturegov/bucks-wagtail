# Generated by Django 2.2.1 on 2019-05-26 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communityassets', '0015_auto_20190526_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communityasset',
            name='price',
            field=models.CharField(blank=True, help_text='Give a cost per session/activity. If a simple price cannot be given, leave the field blank.', max_length=50, null=True, verbose_name='Cost (£)'),
        ),
    ]
