from django.db import models


class Patient(models.Model):

    labnum = models.TextField(unique=True)
    firstname = models.TextField()
    surname = models.TextField()


class Variant(models.Model):

    id = models.AutoField(primary_key=True)
    occurrences = models.ManyToManyField(Patient, through='PatientVariant')
    genomic_pos = models.IntegerField()
    hgvs = models.TextField()


class PatientVariant(models.Model):

    id = models.IntegerField(primary_key=True, unique=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE)

#These are the tables used for the Django tutorial polling app

class Question(models.Model):

    question_text = models.TextField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


