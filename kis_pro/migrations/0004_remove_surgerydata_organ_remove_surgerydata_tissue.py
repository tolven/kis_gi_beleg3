# Generated by Django 4.0 on 2022-02-01 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kis_pro', '0003_rename_surgery_surgerydata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='surgerydata',
            name='organ',
        ),
        migrations.RemoveField(
            model_name='surgerydata',
            name='tissue',
        ),
    ]
