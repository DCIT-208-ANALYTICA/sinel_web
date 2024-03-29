# Generated by Django 3.2.9 on 2021-12-10 23:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0002_testimonial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='added_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='message',
            field=models.TextField(default='hi'),
            preserve_default=False,
        ),
    ]
