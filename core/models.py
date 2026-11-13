from django.db import models

# Create your models here.


class Unidade(models.Model):
    id_unidade = models.AutoField(primary_key=True)
    cd_unidade = models.CharField(
        max_length=20, verbose_name='Código da Unidade', blank= True)
    nm_unidade = models.CharField(
        max_length=150, verbose_name='Nome da Unidade', blank= True)
    cidade = models.CharField(
        max_length=100, verbose_name='Endereço da Unidade', blank= True)

    def __str__(self):
        return self.nm_unidade


class Usuario(models.Model):
    class perfil(models.TextChoices):
        MASTER_GERAL = 'MASTER_GERAL', 'Master Geral'
        MASTER_UNIDADE = 'MASTER_UNIDADE', 'Master Unidade'
        COORDENADOR = 'COORDENADOR', 'Coordenador'
        DOCENTE = 'DOCENTE', 'Docente'
        PORTARIA = 'PORTARIA', 'Portaria'
    id_usuario = models.AutoField(primary_key=True, unique=True, blank= True)
    nm_usuario = models.CharField(
        max_length=150, verbose_name='Nome do Usuário', blank= True)
    email = models.EmailField(unique=True, blank= True)
    uuid_cracha = models.CharField(max_length=50, unique=True, null=True)
    perfil = models.CharField(choices=perfil.choices, verbose_name= 'Perfil do Usuário', default= perfil.DOCENTE)
    unidades = models.ManyToManyField(Unidade)

    def __str__(self):
        return self.nome


class Espaco(models.Model):
    id_espaco = models.AutoField(primary_key=True, unique=True, blank= True)
    ds_espaco = models.CharField(verbose_name='Descrição do Espaço')
    unidade = models.ForeignKey(
        Unidade, on_delete=models.CASCADE, verbose_name='Unidade')
    st_disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.ds_espaco
class Chave(models.Model):
    id_chave = models.AutoField(primary_key=True, unique=True, blank= True)
    espaco = models.OneToOneField(Espaco, on_delete=models.PROTECT)
    cd_chave = models.CharField(max_length=30, unique=True, blank= True)
    uuid_tag_chave = models.CharField(max_length=50, unique=True, blank= True)
    st_disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.cd_chave