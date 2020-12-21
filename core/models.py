from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class User(AbstractUser):
    is_manager_sus = models.BooleanField('Manager SUS status', default=False)
    is_professional_health = models.BooleanField('Professional health status', default=False)
    is_patient = models.BooleanField('Patient status', default=False)

    def __str__(self):  # __unicode__ for Python 2
        return self.username

class Vaccine(models.Model):
    name = models.CharField(max_length=55)
    description = models.CharField(max_length=55)

    def __str__(self):
        return f'{self.name} - {self.description}'

    def has_add_permission(self, request):
        print(request.user)
        return request.user.is_professional_health


class User_Vaccine(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vaccine = models.ForeignKey(Vaccine, on_delete=models.CASCADE)
    lote = models.CharField(max_length=55) 
    date_application = models.DateField()  
    is_professional_created = models.BooleanField(default=False)

class Uf(models.Model):
    cod = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return f'{self.cod} - {self.name}'

class Municipio(models.Model):
    cod = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=False, null=False)
    cod_uf = models.ForeignKey(
        'Uf',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.cod} - {self.name}'

class Estabelecimento(models.Model):
    co_unidade = models.BigIntegerField(primary_key=True)
    co_cnes = models.BigIntegerField()
    nu_cnpj = models.CharField(max_length=15, blank=True, null=False)
    no_razao_social = models.CharField(max_length=255, blank=True, null=False)
    no_fantasia = models.CharField(max_length=255, blank=True, null=False)
    nu_latitude = models.CharField(max_length=50, blank=True, null=True, default=0.0)
    nu_longitude = models.CharField(max_length=50, blank=True, null=True, default=0.0)
    no_logradouro = models.CharField(max_length=255, blank=True, null=False)
    nu_endereco = models.CharField(max_length=55,blank=True, null=False)
    no_complemento = models.CharField(max_length=255, blank=True, null=False)
    no_bairro = models.CharField(max_length=255, blank=True, null=False)
    co_cep = models.IntegerField(blank=True, null=True)
    co_municipio_gestor = models.ForeignKey(
        'Municipio',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.co_cnes} - {self.no_fantasia}'

class User_Estabelecimento(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    estabelecimento = models.ForeignKey(Estabelecimento, on_delete=models.CASCADE)
    vinculo = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.user.username} - {self.estabelecimento.no_fantasia}'
    
    class Meta:
        verbose_name_plural = "Vinculos de profissionais com estabelecimento"

class EstoqueVacina(models.Model):
    vacina = models.ForeignKey(Vaccine, on_delete=models.CASCADE)
    estabelecimento = models.ForeignKey(Estabelecimento, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=10)

class EstabelecimentoAtendimento(models.Model):
    estabelecimento = models.ForeignKey(Estabelecimento, on_delete=models.CASCADE)
    horario = models.DateTimeField()
    vagas = models.IntegerField(default=10)

    def __str__(self):
        return f'{self.estabelecimento} - {self.horario}'

class Agendamento(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vacina = models.ForeignKey(Vaccine, on_delete=models.CASCADE)
    horario = models.ForeignKey(EstabelecimentoAtendimento, on_delete=models.CASCADE)
    atendido = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)