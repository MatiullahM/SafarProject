from django.db import models

# Create your models here.




class TripDriver(models.Model):
    trip = models.ForeignKey('Trips', models.DO_NOTHING, blank=True, null=True)
    driver_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trip_driver'


class TripPassengers(models.Model):
    trip = models.ForeignKey('Trips', models.DO_NOTHING, blank=True, null=True)
    passenger_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trip_passengers'


class TripStatusHistory(models.Model):
    trip = models.ForeignKey('Trips', models.DO_NOTHING, blank=True, null=True)
    trip_status = models.TextField(blank=True, null=True)  # This field type is a guess.
    updated_by = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trip_status_history'


class Trips(models.Model):
    terminal_id = models.IntegerField(blank=True, null=True)
    company_id = models.IntegerField(blank=True, null=True)
    route_id = models.IntegerField(blank=True, null=True)
    vehicle_id = models.IntegerField(blank=True, null=True)
    assigned_by = models.IntegerField(blank=True, null=True)
    departure_time = models.DateTimeField(blank=True, null=True)
    arrival_time = models.DateTimeField(blank=True, null=True)
    trip_status = models.TextField(blank=True, null=True)  # This field type is a guess.
    created_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted = models.BooleanField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trips'
    
    

class VehicleAssignments(models.Model):
    trip = models.ForeignKey(Trips, models.DO_NOTHING, blank=True, null=True)
    vehicle_id = models.IntegerField(blank=True, null=True)
    assigned_by = models.IntegerField(blank=True, null=True)
    assigned_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vehicle_assignments'
