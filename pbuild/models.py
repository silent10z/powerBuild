from django.db import models


class User(models.Model):
    user_number = models.AutoField(db_column='USER_NUMBER', primary_key=True)  # Field name made lowercase.
    id = models.CharField(db_column='ID', max_length=50)  # Field name made lowercase.
    password = models.CharField(db_column='PASSWORD', max_length=50)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=10)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=300)  # Field name made lowercase.
    insert_day = models.DateField(db_column='INSERT_DAY')  # Field name made lowercase.
    coment = models.CharField(db_column='COMENT', max_length=500, blank=True, null=True)  # Field name made lowercase.



class Meta:
    managed = False
    db_table = 'user'

