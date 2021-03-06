# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Comment(models.Model):
    index = models.AutoField(primary_key=True)
    fid = models.CharField(max_length=20)
    id = models.IntegerField()
    text = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comment'
        unique_together = (('index', 'fid', 'id'),)


class Facility(models.Model):
    index = models.AutoField(primary_key=True)
    fid = models.CharField(db_column='FID', max_length=20)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.
    type = models.IntegerField(db_column='Type')  # Field name made lowercase.
    address = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'facility'
        unique_together = (('index', 'fid'),)


class User(models.Model):
    index = models.AutoField(primary_key=True)
    id = models.IntegerField(db_column='ID')  # Field name made lowercase.
    type = models.IntegerField(db_column='Type')  # Field name made lowercase.
    pwd = models.CharField(max_length=25)
    name = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'user'
        unique_together = (('index', 'id'),)


class WRecords(models.Model):
    index = models.AutoField(primary_key=True)
    fid = models.CharField(max_length=20)
    id = models.IntegerField()
    date = models.DateTimeField(blank=True, null=True)
    text = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'w_records'
