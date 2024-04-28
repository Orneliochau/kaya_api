# Generated by Django 5.0.4 on 2024-04-28 08:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pleace', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='pleaceinformation',
            old_name='Description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='pleaceinformation',
            old_name='Location',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='pleaceinformation',
            old_name='Price',
            new_name='price',
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('cv', models.FileField(blank=True, null=True, upload_to='')),
                ('department_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pleace.department')),
            ],
        ),
    ]