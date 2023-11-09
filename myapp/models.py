from django.db import models


class MyApp(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    phonenumber = models.IntegerField

    def __str__(self):
        return (
            f"MyApp(name={self.name}, type={self.type}, phonenumber={self.phonenumber})"
        )

    class Meta:
        db_table = "myApp"
