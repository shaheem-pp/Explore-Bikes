# Generated by Django 4.0.1 on 2022-02-17 06:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_tbl_vehicle_booking_booking_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='tbl_vehicle_booking',
            new_name='tbl_booking',
        ),
        migrations.AlterModelTable(
            name='tbl_booking',
            table='tbl_booking',
        ),
    ]
