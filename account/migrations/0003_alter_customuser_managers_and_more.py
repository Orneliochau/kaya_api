# Generated by Django 5.0.4 on 2024-07-25 13:05

import account.managers
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_remove_customuser_username_customuser_name_and_more'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
                ('objects', account.managers.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(max_length=13, unique=True),
        ),
    ]