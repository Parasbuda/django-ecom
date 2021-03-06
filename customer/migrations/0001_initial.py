# Generated by Django 4.0.3 on 2022-03-13 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('gender', models.PositiveSmallIntegerField(choices=[(1, 'MALE'), (2, 'FEMALE'), (3, 'OTHERS')], help_text='Choice field where 1= male, 2=female,3=others')),
            ],
        ),
    ]
