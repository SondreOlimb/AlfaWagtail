# Generated by Django 3.0.11 on 2021-01-07 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_auto_20210107_2204'),
    ]

    operations = [
        migrations.RenameField(
            model_name='extendeduserprofile',
            old_name='test',
            new_name='bio',
        ),
    ]