# Generated by Django 4.2 on 2023-04-08 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bidding', '0009_alter_product_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='ending_time',
            field=models.TimeField(help_text='after how many hours the bid will end'),
        ),
    ]
