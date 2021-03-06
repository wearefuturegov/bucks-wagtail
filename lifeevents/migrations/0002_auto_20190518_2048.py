# Generated by Django 2.2.1 on 2019-05-18 20:48

from django.db import migrations
import streams.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('lifeevents', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lifeeventpage',
            options={'verbose_name': 'Life event', 'verbose_name_plural': 'Life events'},
        ),
        migrations.AddField(
            model_name='lifeeventpage',
            name='content',
            field=wagtail.core.fields.StreamField([('rich_text', streams.blocks.RichTextBlock()), ('person_profile', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='Add a headshot of the person', required=True)), ('title', wagtail.core.blocks.CharBlock(max_length=200, required=True)), ('text', wagtail.core.blocks.TextBlock(max_length=1000, required=True))])), ('learn_more', wagtail.core.blocks.StructBlock([('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=40, required=True)), ('description', wagtail.core.blocks.TextBlock(max_length=200, required=True)), ('link_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('link_url', wagtail.core.blocks.URLBlock(help_text='If the button page is selected, that will be used first', required=False))])))]))], blank=True, null=True),
        ),
    ]
