# Generated by Django 5.0.1 on 2024-02-10 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_crfq_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crfq',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]
