# Generated by Django 4.0.3 on 2022-04-04 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('memory', '0004_rename_thumbnail_memory_photo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='memory',
            options={'ordering': ('-timestamp',)},
        ),
        migrations.RenameField(
            model_name='memory',
            old_name='date_added',
            new_name='timestamp',
        ),
    ]