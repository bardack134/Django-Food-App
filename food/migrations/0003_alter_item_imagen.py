# Generated by Django 4.2 on 2024-06-13 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_item_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='imagen',
            field=models.ImageField(blank=True, default='https://th.bing.com/th/id/OIP.kRfblRpg8bm4PcJqIF6SRgHaFj?rs=1&pid=ImgDetMain', null=True, upload_to='food'),
        ),
    ]
