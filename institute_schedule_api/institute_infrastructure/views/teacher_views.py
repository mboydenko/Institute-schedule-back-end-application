from django.http import Http404
from rest_framework.views import APIView, Request, Response

from ..models import Chair, Teacher
from ..serialization import teacher_serializer

class TeacherList(APIView):
    def get(self, request: Request):
        
        teachers = Teacher.objects.all()
        
        result = teacher_serializer.TeacherSerializer(teachers, many=True)
        
        return Response(result.data)

    def post(self, request: Request):
        teacher = Teacher()

        teacher.first_name = request.data['first_name']
        
        teacher.middle_name = request.data['middle_name']

        teacher.last_name = request.data['last_name']

        teacher.email = request.data['email']

        teacher.chair = Chair.objects.get(pk=int(request.data['chair_id']))

        teacher.save()

        return Response(teacher_serializer.TeacherSerializer(teacher).data)

class TeacherDetail(APIView):
    def get_object(self, pk: int) -> Teacher:
        try:
            return Teacher.objects.get(pk=pk)
        except Teacher.DoesNotExist:
            raise Http404

    def get(self, request: Request, id: int):
        
        teacher = self.get_object(id)

        return Response(teacher_serializer.TeacherSerializer(teacher).data)

    
    def put(self, request: Request, id: int):

        teacher = self.get_object(id)

        teacher.first_name = request.data['first_name']
        
        teacher.middle_name = request.data['middle_name']

        teacher.last_name = request.data['last_name']

        teacher.email = request.data['email']

        teacher.chair = Chair.objects.get(pk=int(request.data['chair_id']))

        teacher.save()

        return Response(teacher_serializer.TeacherSerializer(teacher).data)

    def delete(self, request: Request, id: int):

        teacher = self.get_object(id)

        teacher.delete()

        return Response(teacher_serializer.TeacherSerializer(teacher).data)