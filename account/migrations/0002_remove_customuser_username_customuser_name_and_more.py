# Generated by Django 5.0.4 on 2024-07-25 12:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='username',
        ),
        migrations.AddField(
            model_name='customuser',
            name='name',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(default=1, max_length=13, unique=True, validators=[django.core.validators.RegexValidator(message="O número de telefone deve ser digitado no formato: '+258849293949'. São permitidos até 13 dígitos.", regex='\\+2588[2-7]\\d{7}\\b')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
    ]