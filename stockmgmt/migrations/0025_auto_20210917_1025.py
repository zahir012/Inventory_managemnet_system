# Generated by Django 3.2.7 on 2021-09-17 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stockmgmt', '0024_auto_20210916_1726'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='name',
        ),
        migrations.AddField(
            model_name='invoice',
            name='Customer_Name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stockmgmt.customer'),
        ),
    ]
