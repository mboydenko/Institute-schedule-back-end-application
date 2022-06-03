from distutils.command.build import build
from django.http import Http404
from rest_framework.views import APIView, Request, Response

from ..models import Building
from ..serialization import building_serializer

class BuildingList(APIView):
    def get(self, request:Request):
        buildings = Building.objects.all()
        data = building_serializer.BuildingPreViewSerializer(buildings, many=True).data
        return Response(data)

    def post(self, request: Request):
        building = Building()
        building.name = request.data['name']
        building.short_name = request.data['sort_name']
        building.save()
        data = building_serializer.BuildingSerializer(building).data
        return Response(data)

class BuildingDetails(APIView):
    def get_object(self, pk: int) -> Building:
        try:
            return Building.objects.get(pk=pk)
        except Building.DoesNotExist:
            raise Http404
    
    def get(self, request: Request, id: int):
        building = self.get_object(id)
        data = building_serializer.BuildingSerializer(building).data
        return Response(data)

    def put(self, request: Request, id: int):
        building = self.get_object(id)
        building.name = request['name']
        building.short_name = request['short_name']
        building.save()
        data = building_serializer.BuildingSerializer(building).data
        return Response(data)

    def delete(self, request: Request, id: int):
        building = self.get_object(id)
        building.delete()
        data = building_serializer.BuildingSerializer(building).data
        return Response(data)
