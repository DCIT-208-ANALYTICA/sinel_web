# Generated by Django 3.2.11 on 2022-02-20 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communications', '0004_alter_appointment_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
