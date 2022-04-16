# Generated by Django 4.0.3 on 2022-03-13 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('paymentMode', '0001_initial'),
        ('additionalCharge', '0001_initial'),
        ('order', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillMain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_no', models.CharField(max_length=10, unique=True)),
                ('pay_type', models.PositiveSmallIntegerField(choices=[(1, 'Cash'), (2, 'Credit')], default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='order.ordermain')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('remarks', models.CharField(max_length=100)),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='payment_details', to='bill.billmain')),
                ('payment_mode', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='paymentMode.paymentmode')),
            ],
        ),
        migrations.CreateModel(
            name='BillDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='bill_details', to='bill.billmain')),
                ('order_detail', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='order.orderdetail')),
            ],
        ),
        migrations.CreateModel(
            name='AdditionalChargeType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('remarks', models.CharField(max_length=100)),
                ('additional_charge', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='additionalCharge.additionalcharge')),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='additional_charge_types', to='bill.billmain')),
            ],
        ),
    ]
