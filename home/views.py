from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from home.models import Person
from home.serializers import PersonSerializer


class Home(APIView):
    def get(self, request):
        name = request.query_params.get('name', 'world')
        return Response({'msg': f'hello {name}'})

    def post(self, request):
        name = request.data.get('name', 'world')
        return Response({'msg': f'hello {name}'})


class PersonView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        persons = Person.objects.all()
        serializer = PersonSerializer(instance=persons, many=True)
        return Response(data=serializer.data)
