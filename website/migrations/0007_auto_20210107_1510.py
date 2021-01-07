# Generated by Django 3.0.11 on 2021-01-07 14:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0006_shoeorderable'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adventurepage',
            old_name='photo',
            new_name='banner_image',
        ),
        migrations.RemoveField(
            model_name='adventurepage',
            name='days_available',
        ),
        migrations.RemoveField(
            model_name='adventurepage',
            name='description',
        ),
        migrations.AddField(
            model_name='adventurepage',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Author'),
        ),
        migrations.AddField(
            model_name='adventurepage',
            name='author_display',
            field=models.CharField(blank=True, help_text='Override how the author’s name displays on this article.', max_length=255, verbose_name='Display author as'),
        ),
        migrations.AddField(
            model_name='adventurepage',
            name='caption',
            field=models.CharField(blank=True, max_length=255, verbose_name='Caption'),
        ),
        migrations.AddField(
            model_name='adventurepage',
            name='date_display',
            field=models.DateField(blank=True, null=True, verbose_name='Display publish date'),
        ),
    ]