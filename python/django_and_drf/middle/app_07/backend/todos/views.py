from rest_framework.generics import ListAPIView, RetrieveAPIView
from todos.models import Todo
from todos.serializers import TodoSerializer

class ListTodo(ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class DetailTodo(RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
