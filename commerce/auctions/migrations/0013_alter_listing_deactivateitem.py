# Generated by Django 3.2.12 on 2023-02-26 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_listing_deactivateitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='deactivateItem',
            field=models.CharField(blank=True, max_length=4000, null=True),
        ),
    ]
