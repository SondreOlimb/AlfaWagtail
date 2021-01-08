# Generated by Django 3.0.11 on 2021-01-08 13:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('coderedcms', '0018_auto_20200805_1702'),
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('website', '0020_auto_20210108_1453'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtUserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instagram', models.URLField(default='', help_text='Add your instagram', max_length=10, verbose_name='Instagram url')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='wagtail_extended_userprofile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='ExtendedUserProfile',
        ),
    ]