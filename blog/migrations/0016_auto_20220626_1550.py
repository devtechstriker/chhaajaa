# Generated by Django 3.2.12 on 2022-06-26 15:50

from django.db import migrations, models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20220610_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='devnagri_body',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='devnagri_btn',
            field=models.BooleanField(default=False),
        ),
    ]
