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
        return self.nm_usuario


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

from django.db import models

class ReservaFixa(models.Model):
    class DiaDaSemana(models.IntegerChoices):
        DOMINGO = 1, 'Domingo'
        SEGUNDA = 2, 'Segunda-Feira'
        TERCA = 3, 'Terça-Feira'
        QUARTA = 4, 'Quarta-Feira'
        QUINTA = 5, 'Quinta-Feira'
        SEXTA = 6, 'Sexta-Feira'
        SABADO = 7, 'Sábado'

    id_reserva_fixa = models.AutoField(primary_key= True)
    nr_dia_semana = models.IntegerField(choices=DiaDaSemana.choices)
    hr_inicio = models.TimeField()
    hr_fim = models.TimeField()
    espaco = models.OneToOneField(Espaco, on_delete=models.PROTECT)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    ds_turma = models.CharField(max_length= 55)
    st_ativo = models.BooleanField(default = True)

    def __str__(self):
        return self.ds_turma

class TipoReservaPontual(models.TextChoices):
    DOCENTE_PONTUAL = 'DOCENTE_PONTUAL', 'Reserva Esporádica de Docente'
    EVENTO_EXTERNO = 'EVENTO_EXTERNO', 'Evento Institucional / Externo'
    MANUTENCAO = 'MANUTENCAO', 'Manutenção / Bloqueio Técnico'


class TipoReservaPontual(models.TextChoices):
    DOCENTE_PONTUAL = 'DOCENTE_PONTUAL', 'Reserva Esporádica de Docente'
    EVENTO_EXTERNO = 'EVENTO_EXTERNO', 'Evento Institucional / Externo'
    MANUTENCAO = 'MANUTENCAO', 'Manutenção / Bloqueio Técnico'


class ReservaPontual(models.Model):
    id_reserva_pontual = models.AutoField(primary_key=True)

    espaco = models.ForeignKey(
        Espaco,
        on_delete=models.PROTECT,
        verbose_name='Espaço'
    )

    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.PROTECT,
        verbose_name='Usuário responsável'
    )

    dt_reserva = models.DateField(verbose_name='Data da Reserva')
    hr_inicio = models.TimeField(verbose_name='Horário de Início')
    hr_fim = models.TimeField(verbose_name='Horário de Término')

    tp_reserva = models.CharField(
        max_length=30,
        choices=TipoReservaPontual.choices,
        verbose_name='Tipo de Reserva'
    )

    ds_motivo = models.TextField(verbose_name='Motivo da Reserva')

    st_aprovado = models.BooleanField(
        default=False,
        verbose_name='Reserva Aprovada'
    )

    def __str__(self):
        return f'{self.espaco} - {self.dt_reserva}'


class Remanejamento(models.Model):
    id_remanejamento = models.AutoField(primary_key=True)

    espaco = models.ForeignKey(
        Espaco,
        on_delete=models.PROTECT,
        verbose_name='Espaço'
    )

    usuario_substituto = models.ForeignKey(
        Usuario,
        on_delete=models.PROTECT,
        verbose_name='Usuário Substituto'
    )

    dt_remanejamento = models.DateField(
        verbose_name='Data Específica da Alteração'
    )

    hr_inicio = models.TimeField(verbose_name='Horário de Início')
    hr_fim = models.TimeField(verbose_name='Horário de Término')

    tp_reserva = models.CharField(
        max_length=30,
        choices=TipoReservaPontual.choices,
        verbose_name='Tipo de Reserva'
    )

    ds_motivo = models.TextField(verbose_name='Motivo do Remanejamento')

    dh_registro = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Data e Hora do Registro'
    )

    def __str__(self):
        return f'{self.espaco} - {self.dt_remanejamento}'

class PerfilAcesso(models.TextChoices):
    MASTER_GERAL = 'MASTER_GERAL', 'Master Geral (Global)'
    MASTER_UNIDADE = 'MASTER_UNIDADE', 'Master da Unidade'
    COORDENADOR = 'COORDENADOR', 'Coordenador de Área'
    DOCENTE = 'DOCENTE', 'Docente'
    PORTARIA = 'PORTARIA', 'Operador de Portaria'