from rest_framework.generics import ListAPIView, UpdateAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView
from .models import Todo
from .serializers import TodoSerializer, ChooseSerializer


# Create your views here.
class All(ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class Create(CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class Detail(RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = ChooseSerializer
    lookup_field = 'id'


class Delete(DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = ChooseSerializer
    lookup_field = 'id'


class Update(UpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = ChooseSerializer
    lookup_field = 'id'
