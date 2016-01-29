from django.db import models

class Variants(models.Model):

    id = models.IntegerField(primary_key=True, unique=True)
    genomic_pos = models.IntegerField()
    hgvs = models.TextField()


class Patients(models.Model):

    id = models.IntegerField(primary_key=True, unique=True)
    labnum = models.TextField(unique=True)
    firstname = models.TextField()
    surname = models.TextField()

class PatientVariants(models.Model):

    id = models.IntegerField(primary_key=True, unique=True)
    patient = models.ForeignKey(Patients)
    variant = models.ForeignKey(Variants)

