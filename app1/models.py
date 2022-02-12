from django.db import models


# Create your models here.

class tbl_staff(models.Model):
    Staffid = models.CharField(max_length=30)
    Name = models.CharField(max_length=40)
    Address = models.CharField(max_length=30)
    Phone = models.CharField(max_length=30)
    Email = models.CharField(max_length=30)
    Status = models.CharField(max_length=30)
    category = models.CharField(max_length=15, default="Nil")

    class Meta:
        db_table = "tbl_staff"


class tbl_vehicle_model(models.Model):
    vehiclemodelnumber = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    enginecapacity = models.CharField(max_length=40)
    photo = models.CharField(max_length=100)
    cc = models.CharField(max_length=40)
    tankcapacity = models.CharField(max_length=30)
    mileage = models.CharField(max_length=40)
    colour = models.CharField(max_length=30)
    price = models.CharField(max_length=40)

    class meta:
        db_table = "tbl_vehicle_model"


class tbl_spare_parts(models.Model):
    sparepartnumber = models.CharField(max_length=30)
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=30)
    photo = models.CharField(max_length=40)
    unit = models.CharField(max_length=30)
    price = models.CharField(max_length=40)
    stockquantity = models.CharField(max_length=30)

    class meta:
        db_table = "tbl_spare_parts"


class tbl_service(models.Model):
    serviceid = models.CharField(max_length=30)
    servicename = models.CharField(max_length=40)

    class Meta:
        db_table = "tbl_service"


class tbl_reviews(models.Model):
    reviewid = models.CharField(max_length=30)
    customerName = models.CharField(max_length=40)
    review = models.CharField(max_length=30)
    reviewdate = models.CharField(max_length=30)

    class Meta:
        db_table = "tbl_reviews"


class tbl_complaints(models.Model):
    complaintid = models.CharField(max_length=30)
    customerName = models.CharField(max_length=40)
    complaint = models.CharField(max_length=30)
    complaintDate = models.CharField(max_length=30)

    class Meta:
        db_table = "tbl_complaints"


class tbl_customer(models.Model):
    Customerid = models.CharField(max_length=30)
    Name = models.CharField(max_length=40)
    Address = models.CharField(max_length=30)
    Phone = models.CharField(max_length=30)
    Email = models.CharField(max_length=30)
    Password = models.CharField(max_length=20)
    status = models.CharField(max_length=30)

    class Meta:
        db_table = "tbl_customer"


class tbl_login(models.Model):
    userid = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    hint = models.CharField(max_length=30)

    class Meta:
        db_table = "tbl_login"


class tbl_vehicle_booking(models.Model):
    vehicle_model_number = models.CharField(max_length=30)
    customer_id = models.CharField(max_length=30)
    booking_date = models.CharField(max_length=30)
    status = models.CharField(max_length=30)

    class Meta:
        db_table = "tbl_vehicle_customer"
