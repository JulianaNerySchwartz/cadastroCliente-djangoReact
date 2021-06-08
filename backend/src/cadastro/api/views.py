from rest_framework.generics import ListAPIView, RetrieveAPIView

from cadastro.models import Cadastro
from .serializers import CadastroSerializer


class CadastroListView(ListAPIView):
    queryset = Cadastro.objects.all()
    serializer_class = CadastroSerializer


class CadastroDetailView(RetrieveAPIView):
    queryset = Cadastro.objects.all()
    serializer_class = CadastroSerializer
