# Generated by Django 4.0 on 2024-06-22 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_remove_footer_link_text_remove_footer_link_url_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='background_image',
            field=models.ImageField(blank=True, null=True, upload_to='page_backgrounds/'),
        ),
    ]
