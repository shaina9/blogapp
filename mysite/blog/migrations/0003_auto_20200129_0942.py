# Generated by Django 2.2.9 on 2020-01-29 04:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_thumbnail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='thumbnail',
            new_name='image',
        ),
    ]
