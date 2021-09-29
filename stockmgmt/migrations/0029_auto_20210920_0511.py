# Generated by Django 3.2.7 on 2021-09-20 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockmgmt', '0028_daily_accounts'),
    ]

    operations = [
        migrations.AddField(
            model_name='daily_accounts',
            name='Transcation_by',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='daily_accounts',
            name='Expense_reason',
            field=models.TextField(max_length=250, null=True),
        ),
    ]
