# Generated by Django 3.2.12 on 2022-06-10 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20220207_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
