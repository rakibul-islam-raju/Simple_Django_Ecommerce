# Generated by Django 3.0.7 on 2020-06-23 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20200617_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=500, max_digits=7),
            preserve_default=False,
        ),
    ]
