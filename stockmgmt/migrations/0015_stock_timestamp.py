# Generated by Django 3.2.7 on 2021-09-14 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockmgmt', '0014_rename_opening_balance_customer_customer_due'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]