# Generated by Django 4.2 on 2024-06-13 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='food'),
        ),
    ]
