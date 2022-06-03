from django.http import Http404
from rest_framework.views import APIView, Request, Response
from ..models import Chair
from ..serialization import chair_serializer

class ChairList(APIView):
    def get(self, request: Request):
        chairs = Chair.objects.all()
        data = chair_serializer.ChairPreViewSerializor(chairs, many=True).data
        return Response(data)
    
    def post(self, request: Request):
        chair = Chair()
        chair.name = request.data['name']
        chair.abbreviation = request.data['abbreviation']
        chair.save()
        data = chair_serializer.ChairPreViewSerializor(chair).data
        return Response(data)

class ChairDetail(APIView):
    def get_object(self, id: int) -> Chair:
        try:
            chair = Chair.objects.get(pk=id)
            return chair
        except Chair.DoesNotExist:
            raise Http404
    
    def get(self, request: Request, id: int):
        chair = self.get_object(id)
        data = chair_serializer.ChairSerializer(chair).data
        return Response(data)
    
    def put(self, request: Request, id: int):
        chair = self.get_object(id)
        chair.name = request.data['name']
        chair.abbreviation = request.data['abbreviation']
        chair.save()
        data = chair_serializer.ChairSerializer(chair).data
        return Response(data)

    def delete(self, request: Request, id: int):
        chair = self.get_object(id)
        chair.delete()
        data = chair_serializer.ChairSerializer(chair).data
        return Response(data)