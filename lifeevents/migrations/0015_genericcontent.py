# Generated by Django 2.2.1 on 2019-06-02 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lifeevents', '0014_learnmore'),
    ]

    operations = [
        migrations.CreateModel(
            name='GenericContent',
            fields=[
                ('lifeevent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='lifeevents.LifeEvent')),
            ],
            options={
                'abstract': False,
            },
            bases=('lifeevents.lifeevent',),
        ),
    ]