# Generated by Django 3.2.11 on 2022-02-20 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_partner_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='visible',
            field=models.BooleanField(default=False),
        ),
    ]
