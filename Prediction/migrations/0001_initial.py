# Generated by Django 3.1.7 on 2022-05-13 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ticker_name', models.CharField(max_length=100)),
                ('Price', models.DecimalField(decimal_places=5, max_digits=10)),
                ('Market_cap', models.DecimalField(decimal_places=5, max_digits=10)),
            ],
        ),
    ]
