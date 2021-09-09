from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import GasStation
from api.serializers import GasStationSerializer


class GasStationView(APIView):
    def get(self, request):
        stations = GasStation.objects.all().prefetch_related()
        serializer = GasStationSerializer(stations, many=True)
        return Response(serializer.data)
