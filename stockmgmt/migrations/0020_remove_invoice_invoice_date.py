# Generated by Django 3.2.7 on 2021-09-15 06:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stockmgmt', '0019_alter_invoice_invoice_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='invoice_date',
        ),
    ]
