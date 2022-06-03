from typing import List
from django.http import Http404
from rest_framework.views import APIView, Request, Response
from ..serialization import group_serializer
from ..models import Group
from ..exceptions import group_exceptions

class GroupList(APIView):

    def create_group(self, data) -> Group:
        name = data['name']

        number_of_subgroups = int(data['number_of_subgroups'])

        groups: List[Group] = Group.objects.all()

        for group in groups:
            if(group.name == name):
                raise group_exceptions.NameNotAvailable()

        group = Group()

        group.name = name

        group.number_of_subgroups = number_of_subgroups

        group.save()

        return group


    def get(self, request: Request):
        
        groups = Group.objects.all()
        
        data = group_serializer.GroupSerializer(groups, many=True).data

        return Response(data, 200)

    def post(self, request: Request):

        group = self.create_group(request.data)

        data = group_serializer.GroupSerializer(group).data

        return Response(data)


class GroupDetail(APIView):
    def get_object(self,id: int) -> Group:
        try:
            return Group.objects.get(pk=id)
        except Group.DoesNotExist:
            raise Http404

    def edit_object(self, id: int, data) -> Group:
        current_group: Group = self.get_object(id)

        name = data['name']

        number_of_subgroups = int(data['number_of_subgroups'])

        groups: List[Group] = Group.objects.all()

        for group in groups:
            if(group.name == name and group.id != current_group.id):
                raise group_exceptions.NameNotAvailable()


        current_group.name = name

        current_group.number_of_subgroups = number_of_subgroups

        current_group.save()

        return current_group

    def get(self, request: Request, id: int):
        group = self.get_object(id)

        data = group_serializer.GroupSerializer(group).data

        return Response(data)

    def put(self, request: Request, id: int):
        group = self.edit_object(id, request.data)
        
        data = group_serializer.GroupSerializer(group).data

        return Response(data)

    def delete(self, request: Request, id: int):
        group = self.get_object(id)

        group.delete()

        data = group_serializer.GroupSerializer(group).data

        return Response(data)