# Generated by Django 3.2 on 2021-12-18 08:28

from django.db import migrations
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20211211_1320'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='schedules',
            field=django_ckeditor_5.fields.CKEditor5Field(default=''),
        ),
    ]