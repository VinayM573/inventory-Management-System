# Generated by Django 5.0.1 on 2024-02-12 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_alter_crfq_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='crfq',
            name='notes',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='crfq',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Denied', 'Denied')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='crfq',
            name='total',
            field=models.IntegerField(null=True),
        ),
    ]
