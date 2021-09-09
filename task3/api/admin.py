from django.contrib import admin

from api.models import GasStation, Image, Service, Fuel

admin.site.register(Image)
admin.site.register(Service)
admin.site.register(GasStation)
admin.site.register(Fuel)
