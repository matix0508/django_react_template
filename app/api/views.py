from rest_framework import generics
from .models import FirstModel
from .serializers import FirstModelSerializer

# Create your views here.
class FirstModelView(generics.CreateAPIView):
    queryset = FirstModel.objects.all()
    serializer_class = FirstModelSerializer