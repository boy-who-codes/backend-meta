# Generated by Django 4.0 on 2024-06-22 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_client_logo_clientlogo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientlogo',
            name='client',
            field=models.CharField(default='null', max_length=10000),
        ),
        migrations.DeleteModel(
            name='Client',
        ),
    ]
