# Generated by Django 4.2.13 on 2024-06-22 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0003_pdf'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lead',
            name='pdf_file',
        ),
        migrations.AddField(
            model_name='pdf',
            name='pdf_file_name',
            field=models.CharField(default='meta-insyt.pdf', max_length=1000),
        ),
    ]
