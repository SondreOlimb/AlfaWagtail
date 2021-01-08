# Generated by Django 3.0.11 on 2021-01-08 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailusers', '0019_auto_20210108_1437'),
        ('website', '0017_extendeduserprofile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='extendeduserprofile',
            options={},
        ),
        migrations.RemoveField(
            model_name='extendeduserprofile',
            name='body',
        ),
        migrations.RemoveField(
            model_name='extendeduserprofile',
            name='coderedpage_ptr',
        ),
        migrations.AddField(
            model_name='extendeduserprofile',
            name='userprofile_ptr',
            field=models.OneToOneField(auto_created=True, default='test', on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailusers.UserProfile'),
            preserve_default=False,
        ),
    ]
