# Generated by Django 4.0 on 2022-02-01 23:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kis_pro', '0006_surgerydata_report_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='RadioData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_text', models.TextField(max_length=500)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kis_pro.cases')),
            ],
        ),
    ]