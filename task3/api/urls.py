from django.urls import path

from api.views import GasStationView

urlpatterns = [
    path('', GasStationView.as_view()),
]
