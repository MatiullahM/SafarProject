from django.db import models

# Create your models here.


class DriverAssistants(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    father_name = models.CharField(max_length=150)
    tazkira_number = models.CharField(unique=True, max_length=100)
    phone = models.CharField(unique=True, max_length=12)
    emergency_phone_number = models.CharField(max_length=20)
    is_active = models.BooleanField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted = models.BooleanField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'driver_assistants'


class Drivers(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    father_name = models.CharField(max_length=150)
    tazkira_number = models.CharField(unique=True, max_length=100)
    phone = models.CharField(unique=True, max_length=12)
    emergency_phone_number = models.CharField(max_length=12, blank=True, null=True)
    license_number = models.CharField(unique=True, max_length=100, blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted = models.BooleanField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'drivers'
