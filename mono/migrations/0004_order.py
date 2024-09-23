# Generated by Django 4.2.16 on 2024-09-21 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mono', '0003_breadbaza'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=300)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('piece', models.IntegerField()),
                ('time_of_year', models.CharField(max_length=50)),
            ],
        ),
    ]
