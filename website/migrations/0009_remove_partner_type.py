# Generated by Django 3.2.11 on 2022-02-20 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_partner_logo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partner',
            name='type',
        ),
    ]