# Generated by Django 3.2 on 2021-11-25 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='administrator',
            name='title',
            field=models.CharField(default='Doctor', max_length=200),
            preserve_default=False,
        ),
    ]
