from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from home.models import Person, Question
from home.serializers import PersonSerializer, QuestionSerializer


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


class QuestionView(APIView):
    def get(self, request):
        questions = Question.objects.all()
        serializer = QuestionSerializer(instance=questions, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        question = get_object_or_404(Question, pk=pk)
        serializer = QuestionSerializer(instance=question, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        question = get_object_or_404(Question, pk=pk)
        question.delete()
        return Response(data={'message': 'question deleted'}, status=status.HTTP_200_OK)
