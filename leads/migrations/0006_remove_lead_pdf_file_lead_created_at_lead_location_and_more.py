# Generated by Django 4.2.13 on 2024-06-22 14:37

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0005_lead_pdf_file_alter_pdf_pdf_file_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lead',
            name='pdf_file',
        ),
        migrations.AddField(
            model_name='lead',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='lead',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='pdf',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='leads.pdf'),
        ),
    ]
