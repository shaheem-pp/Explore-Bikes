# Generated by Django 4.0.1 on 2022-02-11 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_alter_tbl_staff_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_vehicle_booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_model_number', models.CharField(max_length=30)),
                ('customer_id', models.CharField(max_length=30)),
                ('booking_date', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'tbl_vehicle_customer',
            },
        ),
        migrations.AlterField(
            model_name='tbl_vehicle_model',
            name='photo',
            field=models.CharField(max_length=100),
        ),
    ]
