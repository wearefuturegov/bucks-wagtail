# Generated by Django 2.2.1 on 2019-05-24 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communityassets', '0012_auto_20190524_2242'),
    ]

    operations = [
        migrations.AddField(
            model_name='communityasset',
            name='assigned_to',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='communityasset',
            name='clo_notes',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='communityasset',
            name='health_safety',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='communityasset',
            name='insurance',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='communityasset',
            name='review_notes',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='communityasset',
            name='review_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='communityasset',
            name='safeguarding',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='communityasset',
            name='vol_dbs_check',
            field=models.TextField(max_length=500, null=True),
        ),
    ]
