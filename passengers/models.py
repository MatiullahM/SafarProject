from django.db import models

# Create your models here.



class PassengerDocuments(models.Model):
    passenger = models.ForeignKey('Passengers', models.DO_NOTHING, blank=True, null=True)
    document_type = models.CharField(max_length=50, blank=True, null=True)
    document_number = models.CharField(max_length=100, blank=True, null=True)
    file_path = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'passenger_documents'


class PassengerForeigner(models.Model):
    passenger = models.OneToOneField('Passengers', models.DO_NOTHING, primary_key=True)
    nationality = models.CharField(max_length=100)
    passport_number = models.CharField(max_length=100)
    visa_number = models.CharField(unique=True, max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'passenger_foreigner'


class PassengerNational(models.Model):
    passenger = models.OneToOneField('Passengers', models.DO_NOTHING, primary_key=True)
    father_name = models.CharField(max_length=150, blank=True, null=True)
    tazkira_number = models.CharField(unique=True, max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'passenger_national'


class PassengerType(models.Model):
    passenger_type = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'passenger_type'


class Passengers(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=12)
    emergency_phone_number = models.CharField(max_length=12)
    passenger_type = models.ForeignKey(PassengerType, models.DO_NOTHING, blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted = models.BooleanField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'passengers'

