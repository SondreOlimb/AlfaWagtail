# Generated by Django 3.0.11 on 2021-01-07 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_auto_20210107_2311'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extendeduserprofile',
            name='bio',
        ),
        migrations.AddField(
            model_name='extendeduserprofile',
            name='test',
            field=models.CharField(default='', help_text='Write a bio for your profile page', max_length=40, verbose_name='test'),
        ),
    ]
