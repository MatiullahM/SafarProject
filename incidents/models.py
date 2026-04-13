from django.db import models

# Create your models here.

class Incidents(models.Model):
    trip_id = models.IntegerField(blank=True, null=True)
    vehicle_id = models.IntegerField(blank=True, null=True)
    route_id = models.IntegerField(blank=True, null=True)
    incident_description = models.TextField(blank=True, null=True)
    reported_by = models.IntegerField(blank=True, null=True)
    incident_time = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted = models.BooleanField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'incidents'