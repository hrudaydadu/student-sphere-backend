# Generated by Django 4.1.12 on 2023-11-29 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groupdiscussion', '0006_house_address_house_available_date_house_bathroom_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='contact_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
