from django.db import models

# Create your models here.


class Unidade(models.Model):
    cod_unidade = models.AutoField(
        primary_key=True, unique=True, verbose_name='Código da Unidade')
    nome_unidade = models.CharField(verbose_name='Nome da Unidade')
    endereco_unidade = models.CharField(verbose_name='Endereço da Unidade')


class Usuario(models.Model):
    nome_usuario = models.CharField(verbose_name='Nome do Usuário')
    code_usuario = models.AutoField(
        primary_key=True, unique=True, verbose_name='Código do Usuário')


class UnidadeUsuario(models.Model):
    code_UnidadeUsuario = models.AutoField(unique=True, primary_key=True)
    usuario = models.ForeignKey(
        Usuario, on_delete=models.CASCADE, verbose_name='Usuário')
    unidade = models.ForeignKey(
        Unidade, on_delete=models.CASCADE, verbose_name='Unidade')


class Espaco(models.Model):
    id_espaco = models.AutoField(primary_key=True, unique=True)
    ds_Espaco = models.CharField(verbose_name='Descrição do Espaço')
    unidade = models.ForeignKey(
        Unidade, on_delete=models.CASCADE, verbose_name='Unidade')


class Chave(models.Model):
    num_chave = models.IntegerField()
    id_chave = models.AutoField(primary_key=True, unique=True)
    espaco = models.ForeignKey(
        Espaco, on_delete=models.CASCADE, verbose_name='Espaço')
