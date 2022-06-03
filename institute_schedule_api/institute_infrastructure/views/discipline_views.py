from http import HTTPStatus
from django.http import Http404
from rest_framework.views import APIView, Request, Response
from ..serialization.discipline_serializer import DisciplineSerializer
from ..models import Discipline

class DisciplineList(APIView):
    def get(self, request: Request):
        
        disciplines = Discipline.objects.all()
        
        data = DisciplineSerializer(disciplines, many=True).data
        
        return Response(data)

    def post(self, request: Request):
        
        discipline = Discipline()
        
        discipline.name = request.data['name']
        
        discipline.save()
        
        data = DisciplineSerializer(discipline).data
        
        return Response(data, status=HTTPStatus.CREATED)
    

class DisciplineDetails(APIView):
    def get_object(self, pk) -> Discipline:
        try:
            return Discipline.objects.get(pk=pk)
        except Discipline.DoesNotExist:
            raise Http404
    
    def get(self, response: Request, id: int):
        discipline = self.get_object(id)
        
        data = DisciplineSerializer(discipline).data

        return Response(data)
    
    def put(self, response: Request, id: int):
        discipline = self.get_object(id)

        discipline.name = response.data['name']

        discipline.save()

        data = DisciplineSerializer(discipline).data

        return Response(data, status=HTTPStatus.OK)
    
    def delete(self, request: Request, id: int):
        discipline = self.get_object(id)

        discipline.delete()

        return Response(status=HTTPStatus.OK)