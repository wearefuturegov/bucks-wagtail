# Generated by Django 2.2.1 on 2019-05-24 22:07

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('communityassets', '0010_auto_20190522_1943'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accessibilities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AgeGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Suitabilities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='communityasset',
            name='cost',
        ),
        migrations.AddField(
            model_name='communityasset',
            name='area',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='communityasset',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Give a cost per session/activity. If a simple price cannot be given, leave the field blank.', max_digits=6, null=True, verbose_name='Cost (£)'),
        ),
        migrations.AlterField(
            model_name='communityasset',
            name='contact_name',
            field=models.CharField(blank=True, help_text='Give the name of a person involved with this service', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='communityasset',
            name='daytime',
            field=models.BooleanField(blank=True, default=False, help_text='Does this service happen during the daytime (between 9-5)?', null=True, verbose_name='During daytime?'),
        ),
        migrations.AlterField(
            model_name='communityasset',
            name='description',
            field=models.TextField(help_text='Describe the service in a short paragraph', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='communityasset',
            name='email',
            field=models.EmailField(blank=True, help_text='Give a contact email address', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='communityasset',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='communityasset',
            name='parent_organisation',
            field=models.CharField(help_text='The parent organisation delivering this service, if applicable', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='communityasset',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='Give a contact telephone number, with no spaces', max_length=128, null=True, region=None),
        ),
        migrations.AddField(
            model_name='communityasset',
            name='accessibility',
            field=models.ManyToManyField(blank=True, to='communityassets.Accessibilities'),
        ),
        migrations.AddField(
            model_name='communityasset',
            name='age_groups',
            field=models.ManyToManyField(blank=True, to='communityassets.AgeGroups'),
        ),
        migrations.AddField(
            model_name='communityasset',
            name='suitability',
            field=models.ManyToManyField(blank=True, to='communityassets.Suitabilities'),
        ),
    ]