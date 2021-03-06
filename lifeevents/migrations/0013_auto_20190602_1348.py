# Generated by Django 2.2.1 on 2019-06-02 13:48

from django.db import migrations
import streams.blocks
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('lifeevents', '0012_auto_20190601_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lifeevent',
            name='content',
            field=wagtail.core.fields.StreamField([('rich_text', streams.blocks.RichTextBlock()), ('person_profile', wagtail.core.blocks.StructBlock([('image', streams.blocks.APIFriendlyImageChooserBlock(help_text='A headshot of the person', required=True)), ('headline', wagtail.core.blocks.CharBlock(help_text="A positive headline for this story, including the person's first name", max_length=200, required=True)), ('text', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic'], help_text='Aim for three short paragraphs: problem, action, result', max_length=1500, required=True))])), ('call_to_action', wagtail.core.blocks.StructBlock([('button_text', wagtail.core.blocks.CharBlock(help_text='The text displayed on the button. Should be three words or less.', max_length=200, required=True)), ('url', wagtail.core.blocks.CharBlock(help_text='The URL the button links to', max_length=200, required=True))])), ('financial_help_checker', streams.blocks.FinancialHelpChecker()), ('needs_explorer', streams.blocks.NeedsExplorer())], blank=True, null=True),
        ),
    ]
