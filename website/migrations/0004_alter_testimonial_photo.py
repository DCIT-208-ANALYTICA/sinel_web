# Generated by Django 3.2.9 on 2021-12-11 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20211210_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/images'),
        ),
    ]
