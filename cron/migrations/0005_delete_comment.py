# Generated by Django 4.1.1 on 2023-01-20 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cron', '0004_alter_post_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]