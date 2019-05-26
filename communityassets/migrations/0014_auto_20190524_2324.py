# Generated by Django 2.2.1 on 2019-05-24 23:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('communityassets', '0013_auto_20190524_2308'),
    ]

    operations = [
        migrations.CreateModel(
            name='CCGLocalities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='LAFAreas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='LegacyCategories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ReviewStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='communityasset',
            name='last_updated',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='communityasset',
            name='review_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='communityasset',
            name='assigned_to',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='communityasset',
            name='clo_notes',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='CLO notes'),
        ),
        migrations.AlterField(
            model_name='communityasset',
            name='health_safety',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='communityasset',
            name='insurance',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='communityasset',
            name='parent_organisation',
            field=models.CharField(blank=True, help_text='The parent organisation delivering this service, if applicable', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='communityasset',
            name='review_notes',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='communityasset',
            name='safeguarding',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='communityasset',
            name='vol_dbs_check',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Volunteer DBS check'),
        ),
        migrations.AddField(
            model_name='communityasset',
            name='ccg_locality',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='communityassets.CCGLocalities', verbose_name='CCG Locality'),
        ),
        migrations.AddField(
            model_name='communityasset',
            name='laf_areas',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='communityassets.LAFAreas', verbose_name='LAF Area'),
        ),
        migrations.AddField(
            model_name='communityasset',
            name='legacy_categories',
            field=models.ManyToManyField(blank=True, to='communityassets.LegacyCategories'),
        ),
        migrations.AddField(
            model_name='communityasset',
            name='review_status',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='communityassets.ReviewStatus'),
        ),
    ]