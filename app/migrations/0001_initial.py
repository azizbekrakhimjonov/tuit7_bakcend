# Generated by Django 4.2 on 2024-10-04 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Universitet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=255)),
                ('manzil', models.CharField(max_length=255)),
                ('site', models.CharField(max_length=255)),
                ('rektor', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=255)),
                ('xorij_hamkorlik', models.CharField(max_length=255)),
                ('davlat', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Malumot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fakultet', models.CharField(max_length=100)),
                ('sigimi', models.CharField(max_length=255)),
                ('ballar', models.CharField(max_length=255)),
                ('reyting', models.CharField(max_length=255)),
                ('konktrakt', models.CharField(max_length=255)),
                ('universitet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.universitet')),
            ],
        ),
    ]