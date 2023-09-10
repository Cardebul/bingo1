from django.urls import path
from rest_framework.generics import RetrieveAPIView

from bingo.models import BingoModel

from .serializers import BingoSerializer

urlpatterns = [
    path('<int:user_id>/',
         RetrieveAPIView.as_view(queryset=BingoModel.objects.all(),
                                 serializer_class=BingoSerializer,
                                 lookup_field='user_id'))
]
