# Generated by Django 2.2 on 2020-10-05 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='summary',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
    ]
