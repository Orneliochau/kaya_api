# Generated by Django 5.0.4 on 2024-04-28 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pleace', '0005_remove_employee_department_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pleaceinformation',
            old_name='location',
            new_name='province',
        ),
        migrations.RemoveField(
            model_name='pleaceinformation',
            name='is_active',
        ),
        migrations.AddField(
            model_name='pleaceinformation',
            name='city',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pleaceinformation',
            name='facebook',
            field=models.URLField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='pleaceinformation',
            name='images',
            field=models.ImageField(default=1, upload_to='images'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pleaceinformation',
            name='instagram',
            field=models.URLField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='pleaceinformation',
            name='street_adress',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pleaceinformation',
            name='price',
            field=models.FloatField(blank=True, default=1),
            preserve_default=False,
        ),
    ]
