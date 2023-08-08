# Generated by Django 4.2.4 on 2023-08-07 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_drinks_alter_items_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='lunch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('components', models.CharField(max_length=100)),
                ('images', models.ImageField(upload_to='photos/%y/%m/%d')),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
