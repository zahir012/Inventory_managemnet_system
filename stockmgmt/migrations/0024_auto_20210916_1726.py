# Generated by Django 3.2.7 on 2021-09-16 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockmgmt', '0023_invoice_net_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='line_elaven',
            field=models.CharField(blank=True, default='', max_length=120, null=True, verbose_name='Due Amount'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='line_elaven_quantity',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Quantity'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='line_elaven_total_price',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Line Total (tk)'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='line_elaven_unit_price',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Unit Price (tk)'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_eight_total_price',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Line Total (tk)'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_eight_unit_price',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Unit Price (tk)'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_nine_total_price',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Line Total (tk)'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_nine_unit_price',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Unit Price (tk)'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_seven_total_price',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Line Total (tk)'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_seven_unit_price',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Unit Price (tk)'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_six_total_price',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Line Total (tk)'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_six_unit_price',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Unit Price (tk)'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_ten_total_price',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Line Total (tk)'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_ten_unit_price',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Unit Price (tk)'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_three_total_price',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Line Total (tk'),
        ),
    ]
