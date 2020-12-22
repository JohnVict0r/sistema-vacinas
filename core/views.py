from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets, permissions, status, filters

from .models import User, Vaccine, User_Vaccine, Agendamento, Estabelecimento, EstabelecimentoAtendimento, Uf, Municipio
from .serializers import (
    UserSerializer, 
    VaccineSerializer, 
    UserVaccinesSerializer, 
    AgendamentoSerializer, 
    EstabelecimentoSerializer,
    EstabelecimentoAtendimentosSerializer,
    UfSerializer,
    MunicipioSerializer
    )

@api_view(['POST'])
def auth(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def profile(request):
    """
    List all code snippets, or create a new snippet.
    """
    if not request.user.is_authenticated:
        return Response(data={"message":"Usuário não autenticado"}, status=status.HTTP_401_UNAUTHORIZED)

    if request.method == 'GET':
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

@api_view(['GET'])
def patients(request):
    """
    List all code snippets, or create a new snippet.
    """
    if not request.user.is_authenticated:
        return Response(data={"message":"Usuário não autenticado"}, status=status.HTTP_401_UNAUTHORIZED)

    if request.method == 'GET':
        users = User.objects.filter(is_patient=True)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def vaccines(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        vaccines = Vaccine.objects.all()
        serializer = VaccineSerializer(vaccines, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def uf_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        ufs = Uf.objects.all()
        serializer = UfSerializer(ufs, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def municipios(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        municipios = Municipio.objects.all()
        serializer = MunicipioSerializer(municipios, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def estabelecimentos(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        estabelecimentos = Estabelecimento.objects.all()
        serializer = EstabelecimentoSerializer(estabelecimentos, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def user_vaccines(request):
    """
    List all code snippets, or create a new snippet.
    """
    if not request.user.is_authenticated:
        return Response(data={"message":"Usuário não autenticado"}, status=status.HTTP_401_UNAUTHORIZED)

    if request.method == 'GET':
        user_vaccines = User_Vaccine.objects.filter(user=request.user)
        serializer = UserVaccinesSerializer(user_vaccines, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        """ 
        serializer = UserVaccinesSerializer(data=request.data, many=True) """
        vaccine = Vaccine.objects.get(pk=request.data['vaccine'])

        user_vaccine = User_Vaccine.objects.create(
            user=request.user, 
            vaccine=vaccine,
            lote=request.data['lote'],
            date_application=request.data['date_application'],
            is_professional_created=False
            )

        serializer = UserVaccinesSerializer(user_vaccine)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
def user_agendamentos(request):
    """
    List all code snippets, or create a new snippet.
    """
    if not request.user.is_authenticated:
        return Response(data={"message":"Usuário não autenticado"}, status=status.HTTP_401_UNAUTHORIZED)

    if request.method == 'GET':
        user_agendamentos = Agendamento.objects.filter(user=request.user)
        serializer = AgendamentoSerializer(user_agendamentos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        vaccine = Vaccine.objects.get(pk=request.data['vaccine'])
        horario = EstabelecimentoAtendimento.objects.get(pk=request.data['horario'])

        user_agendamento = Agendamento.objects.create(
            user=request.user, 
            vacina=vaccine,
            horario=horario
            )

        serializer = AgendamentoSerializer(user_agendamento)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def pacient_vaccines(request):
    """
    List all code snippets, or create a new snippet.
    """
    if not request.user.is_authenticated:
        return Response(data={"message":"Usuário não autenticado"}, status=status.HTTP_401_UNAUTHORIZED)
    
    if not request.user.is_professional_health:
        return Response(data={"message":"Usuário não autorizado"}, status=status.HTTP_401_UNAUTHORIZED)

    if request.method == 'POST':
        """ 
        serializer = UserVaccinesSerializer(data=request.data, many=True) """
        vaccine = Vaccine.objects.get(pk=request.data['vaccine'])
        user = User.objects.get(pk=request.data['user'])

        user_vaccine = User_Vaccine.objects.create(
            user=user, 
            vaccine=vaccine,
            lote=request.data['lote'],
            date_application=request.data['date_application'],
            is_professional_created=True
            )

        serializer = UserVaccinesSerializer(user_vaccine)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
def atendimentos(request):
    """
    List all code snippets, or create a new snippet.
    """
    if not request.user.is_authenticated:
        return Response(data={"message":"Usuário não autenticado"}, status=status.HTTP_401_UNAUTHORIZED)

    if request.method == 'GET':
        atendimentos = EstabelecimentoAtendimento.objects.all()
        serializer = EstabelecimentoAtendimentosSerializer(atendimentos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        estabelecimento = Estabelecimento.objects.get(pk=request.data['estabelecimento'])

        atendimento = EstabelecimentoAtendimento.objects.create(
            estabelecimento=estabelecimento, 
            horario=request.data['horario'],
            vagas=request.data['vagas']
            )

        serializer = EstabelecimentoAtendimentosSerializer(atendimento)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
def agendamentos(request):
    """
    List all code snippets, or create a new snippet.
    """
    if not request.user.is_authenticated:
        return Response(data={"message":"Usuário não autenticado"}, status=status.HTTP_401_UNAUTHORIZED)

    if request.method == 'GET':
        agendamentos = Agendamento.objects.all()
        serializer = AgendamentoSerializer(agendamentos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        agendamento = Agendamento.objects.filter(pk=request.data['id']).first()
        agendamento.atendido = True
        agendamento.save()
        serializer = AgendamentoSerializer(agendamentos)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        """ 
        serializer = UserVaccinesSerializer(data=request.data, many=True) """
        user = User.objects.get(pk=request.data['user'])
        vaccine = Vaccine.objects.get(pk=request.data['vaccine'])
        horario = EstabelecimentoAtendimento.objects.get(pk=request.data['horario'])

        agendamento = Agendamento.objects.create(
            user=user, 
            vaccine=vaccine,
            horario=horario
            )

        serializer = AgendamentoSerializer(agendamento)
        return Response(serializer.data, status=status.HTTP_201_CREATED)