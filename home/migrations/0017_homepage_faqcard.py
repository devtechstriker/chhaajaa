# Generated by Django 3.2.12 on 2022-06-11 07:46

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_alter_faq_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='faqcard',
            field=wagtail.core.fields.StreamField([('faqcard', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Enter title', required=True)), ('description', wagtail.core.blocks.TextBlock(help_text='Enter description', required=True)), ('featured', wagtail.core.blocks.BooleanBlock(required=True))]))], blank=True, null=True),
        ),
    ]
