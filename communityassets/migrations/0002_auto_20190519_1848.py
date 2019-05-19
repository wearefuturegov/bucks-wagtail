# Generated by Django 2.2.1 on 2019-05-19 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communityassets', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='communityasset',
            old_name='name',
            new_name='title',
        ),
        migrations.AddField(
            model_name='communityasset',
            name='description',
            field=models.CharField(max_length=500, null=True),
        ),
    ]