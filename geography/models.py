from django.db import models

# Create your models here.

class Checkpoints(models.Model):
    name = models.CharField(max_length=100)
    type = models.TextField()  # This field type is a guess.
    province = models.ForeignKey('Provinces', models.DO_NOTHING, blank=True, null=True)
    route = models.ForeignKey('Routes', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'checkpoints'

class Provinces(models.Model):
    name = models.CharField(unique=True, max_length=150)
    code = models.CharField(unique=True, max_length=5, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'provinces'
    
    def __str__(self):
        return self.name
    

class Routes(models.Model):
    name = models.CharField(max_length=100)
    origin = models.ForeignKey(Provinces, models.DO_NOTHING)
    destination = models.ForeignKey(Provinces, models.DO_NOTHING, related_name='routes_destination_set')
    distance_km = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    path_to_destination = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'routes'


class Terminals(models.Model):
    name = models.CharField(max_length=150)
    owner = models.CharField(max_length=100, blank=True, null=True)
    province = models.ForeignKey(Provinces, models.DO_NOTHING, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'terminals'

    def __str__(self):
        return self.name