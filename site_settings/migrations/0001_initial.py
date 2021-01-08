# Generated by Django 3.0.11 on 2021-01-08 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
    ]

    operations = [
        migrations.CreateModel(
            name='MapboxApiApiSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mapbox_maps_api_key', models.CharField(blank=True, help_text='The API Key used for Mapbox.', max_length=255, verbose_name='MapBox API Key')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'verbose_name': 'MapBox API',
            },
        ),
    ]
