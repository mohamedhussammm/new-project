# Generated by Django 4.2.4 on 2023-08-13 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_merge_0002_cart_cartitem_0002_checkout'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout',
            name='id',
        ),
        migrations.AlterField(
            model_name='checkout',
            name='name',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
    ]
