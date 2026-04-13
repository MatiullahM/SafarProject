from django.db import models

# Create your models here.



class Companies(models.Model):
    name = models.CharField(max_length=150)
    owner = models.CharField(max_length=150, blank=True, null=True)
    coverage_area = models.CharField(max_length=150, blank=True, null=True)
    contact_number = models.CharField(max_length=12)
    sec_contact_number = models.CharField(max_length=12)
    terminal_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted = models.BooleanField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'companies'

    def __str__(self):
        return self.company_name
    
class VehicleType(models.Model):
    type_name = models.CharField(unique=True, max_length=50)
    seat_capacity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'vehicle_type'






class Vehicles(models.Model):
    company = models.ForeignKey(Companies, models.DO_NOTHING, blank=True, null=True)
    vehicle_type = models.ForeignKey(VehicleType, models.DO_NOTHING, blank=True, null=True)
    plate_number = models.CharField(unique=True, max_length=20, blank=True, null=True)
    is_accident = models.BooleanField(blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted = models.BooleanField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vehicles'
