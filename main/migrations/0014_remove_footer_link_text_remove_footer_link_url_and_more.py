# Generated by Django 4.0 on 2024-06-22 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_footer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='footer',
            name='link_text',
        ),
        migrations.RemoveField(
            model_name='footer',
            name='link_url',
        ),
        migrations.RemoveField(
            model_name='footer',
            name='order',
        ),
        migrations.CreateModel(
            name='FooterLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_text', models.CharField(max_length=200)),
                ('link_url', models.CharField(max_length=200)),
                ('order', models.IntegerField(default=0)),
                ('footer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='links', to='main.footer')),
            ],
        ),
    ]
