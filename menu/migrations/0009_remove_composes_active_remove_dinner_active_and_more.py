# Generated by Django 4.2.4 on 2023-08-12 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0008_delete_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='composes',
            name='active',
        ),
        migrations.RemoveField(
            model_name='dinner',
            name='active',
        ),
        migrations.RemoveField(
            model_name='drinks',
            name='active',
        ),
        migrations.RemoveField(
            model_name='items',
            name='active',
        ),
        migrations.RemoveField(
            model_name='lunch',
            name='active',
        ),
    ]
