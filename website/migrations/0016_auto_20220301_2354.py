# Generated by Django 3.2.11 on 2022-03-01 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0015_notification_content_hash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='content_hash',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='notification',
            name='url',
            field=models.URLField(blank=True, default='', null=True),
        ),
    ]