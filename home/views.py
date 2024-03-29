from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView

from home.models import Person, Question
from home.serializers import PersonSerializer, QuestionSerializer
from permissions import IsOwnerOrReadOnly


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


class QuestionListView(GenericAPIView):
    throttle_scope = 'question'
    pagination_class = PageNumberPagination
    serializer_class = QuestionSerializer

    def get(self, request):
        questions = Question.objects.all()
        paginate_questions = self.pagination_class().paginate_queryset(questions, request)
        serializer = self.serializer_class(instance=paginate_questions, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class QuestionCreateView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = QuestionSerializer

    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionUpdate(APIView):
    permission_classes = (IsOwnerOrReadOnly,)

    def put(self, request, pk):
        question = get_object_or_404(Question, pk=pk)
        self.check_object_permissions(request, question)
        serializer = QuestionSerializer(instance=question, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionDeleteView(APIView):
    permission_classes = (IsOwnerOrReadOnly,)

    def delete(self, request, pk):
        question = get_object_or_404(Question, pk=pk)
        question.delete()
        return Response(data={'message': 'question deleted'}, status=status.HTTP_200_OK)
