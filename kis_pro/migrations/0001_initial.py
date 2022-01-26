# Generated by Django 4.0.1 on 2022-01-25 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='TNM',
            fields=[
                ('cases_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='kis_pro.cases')),
                ('tumor', models.CharField(max_length=2)),
                ('nodes', models.CharField(max_length=2)),
                ('metastases', models.CharField(max_length=2)),
                ('report_text', models.TextField(max_length=500)),
            ],
            bases=('kis_pro.cases',),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kis_pro.role')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('birthdate', models.DateField()),
                ('attending_doctor', models.ManyToManyField(to='kis_pro.Doctor')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='doctor',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kis_pro.role'),
        ),
        migrations.AddField(
            model_name='cases',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kis_pro.doctor'),
        ),
        migrations.AddField(
            model_name='cases',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kis_pro.patient'),
        ),
    ]