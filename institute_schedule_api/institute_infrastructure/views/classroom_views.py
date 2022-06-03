from distutils.command.build import build
from django.http import Http404
from rest_framework.views import APIView, Request, Response

from ..models import Building, Classroom
from ..serialization import classroom_serializer

class ClassroomList(APIView):
    def get(self, request:Request):
        classrooms = Classroom.objects.all()
        data = classroom_serializer.ClassroomSerializer(classrooms, many=True).data
        return Response(data)

    def post(self, request: Request):
        classroom = Classroom()
        classroom.name = request.data['name']
        classroom.building = Building.objects.get(pk=int(request.data['building_id']))
        classroom.save()
        data = classroom_serializer.ClassroomSerializer(classroom).data
        return Response(data)

class ClassroomDetails(APIView):
    def get_object(self, pk: int) -> Classroom:
        try:
            return Building.objects.get(pk=pk)
        except Building.DoesNotExist:
            raise Http404
    
    def get(self, request: Request, id: int):
        classroom = self.get_object(id)
        data = classroom_serializer.ClassroomSerializer(classroom).data
        return Response(data)

    def put(self, request: Request, id: int):
        classroom = self.get_object(id)
        classroom.name = request['name']
        classroom.building = request['building_id']
        classroom.save()
        data = classroom_serializer.ClassroomSerializer(classroom).data
        return Response(data)

    def delete(self, request: Request, id: int):
        classroom = self.get_object(id)
        classroom.delete()
        data = classroom_serializer.ClassroomSerializer(classroom).data
        return Response(data)
