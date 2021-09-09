from django.db import models


class Image(models.Model):
    url = models.URLField()

    def __str__(self):
        return self.url


class Service(models.Model):
    name = models.CharField(max_length=255)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class Fuel(models.Model):
    CURRENCIES = (
        ('rub', 'rub'),
        ('euro', 'euro'),
        ('dol', 'dol')
    )
    image = models.ForeignKey(Image, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    currency = models.CharField(max_length=5, choices=CURRENCIES)

    def __str__(self):
        return self.name


class GasStation(models.Model):
    id = models.AutoField(primary_key=True)
    coordinates = models.CharField(max_length=250)
    number = models.IntegerField()
    address = models.CharField(max_length=255)
    images = models.ManyToManyField(Image, blank=True, related_name='stations')
    services = models.ManyToManyField(Service, blank=True, related_name='stations')
    fuel = models.ManyToManyField(Fuel, blank=True, related_name='stations')

    def __str__(self):
        return self.address




