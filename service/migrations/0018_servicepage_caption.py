# Generated by Django 3.2.12 on 2022-08-03 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0017_merge_0016_auto_20220610_1559_0016_auto_20220610_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicepage',
            name='caption',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]