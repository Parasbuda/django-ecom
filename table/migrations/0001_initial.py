# Generated by Django 4.0.3 on 2022-03-13 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('active', models.BooleanField(default=True)),
                ('display_order', models.PositiveSmallIntegerField(blank=True, default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'Vacant'), (2, 'Occupied'), (3, 'Reserved')], default=1, help_text='1=vacant,2=occupied,3=reserved')),
                ('active', models.BooleanField(default=True)),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='table.block')),
            ],
        ),
    ]