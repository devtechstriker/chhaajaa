# Generated by Django 3.2.12 on 2022-12-03 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sahi_salah', '0012_auto_20221115_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='sahisalahindexpage',
            name='btn_name',
            field=models.CharField(blank=True, help_text='button name', max_length=200, null=True),
        ),
    ]
