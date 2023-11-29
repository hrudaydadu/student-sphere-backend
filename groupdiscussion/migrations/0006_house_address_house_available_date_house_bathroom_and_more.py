# Generated by Django 4.1.12 on 2023-11-29 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groupdiscussion', '0005_rename_houses_housecomment_houses_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='address',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='house',
            name='available_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='house',
            name='bathroom',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='house',
            name='bedroom',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='house',
            name='contact_name',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='house',
            name='distance_walk',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='house',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='house',
            name='maximum_occupancy',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='house',
            name='property_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='house',
            name='rent_cost',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='house',
            name='special_notes',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='house',
            name='whatsApp_number',
            field=models.BigIntegerField(null=True),
        ),
    ]
