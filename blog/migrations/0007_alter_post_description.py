# Generated by Django 5.0.6 on 2024-06-01 14:41

import django_quill.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_post_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=django_quill.fields.QuillField(blank=True, default='<p></p>', max_length=10000, null=True),
        ),
    ]
