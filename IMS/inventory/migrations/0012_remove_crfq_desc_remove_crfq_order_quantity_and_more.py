# Generated by Django 5.0.1 on 2024-02-14 17:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0011_remove_crfq_subtotal_crfq_desc_crfq_order_quantity_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crfq',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='crfq',
            name='order_quantity',
        ),
        migrations.RemoveField(
            model_name='crfq',
            name='price',
        ),
        migrations.RemoveField(
            model_name='crfq',
            name='product',
        ),
        migrations.RemoveField(
            model_name='crfq',
            name='uom',
        ),
        migrations.CreateModel(
            name='RFQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(max_length=100, null=True)),
                ('order_quantity', models.PositiveIntegerField(null=True)),
                ('uom', models.CharField(choices=[('KG', 'KG'), ('Gram', 'Gram'), ('Unit', 'Unit')], max_length=10, null=True)),
                ('price', models.IntegerField(null=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.product')),
                ('rfqid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.crfq')),
            ],
        ),
    ]
