# Generated by Django 3.2.11 on 2022-03-22 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0016_auto_20220301_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='telephone',
            field=models.CharField(max_length=100),
        ),
    ]
