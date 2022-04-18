from django.db import models


class ClientMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=250)
    telephone = models.CharField(max_length=50)
    message = models.CharField(max_length=4000)
    message_date = models.DateTimeField(auto_now=True)
    is_replied_to = models.BooleanField()
    is_read = models.BooleanField()

    def __str__(self):
        return self.email


class SystemDetails(models.Model):
    email = models.CharField(max_length=500)
    password = models.CharField(max_length=500)

    def __str__(self):
        return self.email


class LeistungsKategorie(models.Model):
    name = models.CharField(max_length=200)
    fahrzeug = models.CharField(max_length=200)
    order = models.IntegerField()

    def __str__(self):
        return self.name


class Leistung(models.Model):
    kategorie = models.ForeignKey(LeistungsKategorie, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    preis = models.CharField(max_length=20)
    order = models.IntegerField()

    def __str__(self):
        return self.name


class FAQ(models.Model):
    frage = models.CharField(max_length=500)
    antwort = models.CharField(max_length=4000)
    order = models.IntegerField()

    def __str__(self):
        return self.name
