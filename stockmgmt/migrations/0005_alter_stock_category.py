# Generated by Django 3.2.7 on 2021-09-07 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stockmgmt', '0004_auto_20210907_0609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stockmgmt.category'),
        ),
    ]
