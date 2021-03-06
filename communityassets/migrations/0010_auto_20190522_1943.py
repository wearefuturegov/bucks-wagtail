# Generated by Django 2.2.1 on 2019-05-22 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('communityassets', '0009_auto_20190522_1823'),
    ]

    operations = [
        migrations.AddField(
            model_name='communityasset',
            name='daytime',
            field=models.BooleanField(blank=True, help_text='Does this service happen during the daytime (between 9-5)?', null=True),
        ),
        migrations.AddField(
            model_name='communityasset',
            name='frequency',
            field=models.CharField(blank=True, help_text="Describe the frequency of this event if applicable. For example 'daily' or 'fortnightly'", max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='communityasset',
            name='postcode',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='communityasset',
            name='venue',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='communityasset',
            name='category',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='communityassets.Categories'),
        ),
        migrations.AlterField(
            model_name='communityasset',
            name='cost',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Give a value for how much this community service costs per session/activity. If a simple price cannot be given, leave the field blank.', max_digits=6, null=True, verbose_name='Cost(£)'),
        ),
        migrations.AlterField(
            model_name='communityasset',
            name='days',
            field=models.ManyToManyField(blank=True, to='communityassets.Days'),
        ),
        migrations.AlterField(
            model_name='communityasset',
            name='url',
            field=models.URLField(blank=True, help_text='The website or webpage where this service can be booked, or where more info can be found about it', null=True, verbose_name='Website URL'),
        ),
    ]
