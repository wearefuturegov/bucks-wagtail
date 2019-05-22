# Generated by Django 2.2.1 on 2019-05-22 14:53

from django.db import migrations
import streams.blocks
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('lifeevents', '0004_auto_20190519_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lifeeventpage',
            name='content',
            field=wagtail.core.fields.StreamField([('rich_text', streams.blocks.RichTextBlock()), ('person_profile', wagtail.core.blocks.StructBlock([('image', streams.blocks.APIFriendlyImageChooserBlock(help_text='A headshot of the person', required=True)), ('headline', wagtail.core.blocks.CharBlock(help_text="A positive headline for this story, including the person's first name", max_length=200, required=True)), ('text', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic'], help_text='Aim for three short paragraphs: problem, action, result', max_length=1500, required=True))])), ('learn_more', wagtail.core.blocks.StructBlock([('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=40, required=True)), ('description', wagtail.core.blocks.TextBlock(max_length=200, required=True)), ('link_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('link_url', wagtail.core.blocks.URLBlock(help_text='If the button page is selected, that will be used first', required=False))])))]))], blank=True, null=True),
        ),
    ]
