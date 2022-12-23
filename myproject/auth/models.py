from django.db import models

class AuthTab(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.CharField(unique=True, max_length=20)
    password = models.CharField(max_length=128)
    is_admin = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'auth_tab'