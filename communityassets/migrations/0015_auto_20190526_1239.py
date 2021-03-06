# Generated by Django 2.2.1 on 2019-05-26 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('communityassets', '0014_auto_20190524_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communityasset',
            name='ccg_locality',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='communityassets.CCGLocalities', verbose_name='CCG Locality'),
        ),
        migrations.AlterField(
            model_name='communityasset',
            name='laf_areas',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='communityassets.LAFAreas', verbose_name='LAF Area'),
        ),
        migrations.AlterField(
            model_name='communityasset',
            name='price',
            field=models.CharField(blank=True, help_text='Give a cost per session/activity. If a simple price cannot be given, leave the field blank.', max_length=30, null=True, verbose_name='Cost (£)'),
        ),
    ]
