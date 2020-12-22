from .models import User, Vaccine, User_Vaccine, Agendamento, Estabelecimento, EstabelecimentoAtendimento, Uf, Municipio
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

class UserSerializer(serializers.HyperlinkedModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    username = serializers.CharField(
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(min_length=8)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
             validated_data['password'], is_patient=True)
        return user

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'is_patient', 'is_professional_health']
        write_only_fields = ('password',)
        read_only_fields = ('id',)

class VaccineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vaccine
        fields = ['id', 'name', 'description']


class UserVaccinesSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    vaccine = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = User_Vaccine
        fields = ('id', 'user', 'vaccine', 'lote', 'date_application', 'is_professional_created')
        read_only_fields = ('id',)

class AgendamentoSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    vaccine = serializers.PrimaryKeyRelatedField(read_only=True)
    horario = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Agendamento
        fields = ['id', 'user', 'vaccine', 'horario', 'atendido', 'created_at']


class EstabelecimentoAtendimentosSerializer(serializers.ModelSerializer):
    estabelecimento = serializers.PrimaryKeyRelatedField(read_only=True)
    horario = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = EstabelecimentoAtendimento
        fields = ['id', 'estabelecimento', 'horario', 'vagas']

class UfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uf
        fields = ['cod', 'name']

class MunicipioSerializer(serializers.ModelSerializer):
    cod_uf = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Municipio
        fields = ['cod', 'name', 'cod_uf']

class EstabelecimentoSerializer(serializers.ModelSerializer):
    co_municipio_gestor = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Estabelecimento
        fields = ['co_unidade', 'co_cnes', 'no_razao_social', 'no_fantasia', 'co_municipio_gestor' ]
