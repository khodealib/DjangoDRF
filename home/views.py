from rest_framework.response import Response
from rest_framework.views import APIView


class Home(APIView):
    def get(self, request):
        name = request.query_params.get('name', 'world')
        return Response({'msg': f'hello {name}'})

    def post(self, request):
        name = request.data.get('name', 'world')
        return Response({'msg': f'hello {name}'})
