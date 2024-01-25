# Generated by Django 4.1 on 2024-01-17 13:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesitems',
            name='date_added',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]
