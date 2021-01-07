# Generated by Django 3.0.11 on 2021-01-07 13:17

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20210107_1331'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShoeOrderable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='shoe_model', to='website.AdventurePage')),
                ('shoe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Shoes')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]