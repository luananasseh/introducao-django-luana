
from django.db import models


class Atividade(models.Model):
    TIPOS = [
        ('prova', 'Prova'),
        ('trabalho', 'Trabalho'),
        ('lista', 'Lista'),
        ('leitura', 'Leitura'),
        ('projeto', 'Projeto'),
        ('outro', 'Outro'),
    ]

    titulo = models.CharField(max_length=120)
    tipo = models.CharField(max_length=20, choices=TIPOS)
    prazo = models.DateTimeField()
    disciplina = models.ForeignKey(
        'Disciplina',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    dificuldade = models.IntegerField(null=True, blank=True)
    peso_nota = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )
    importancia = models.IntegerField(null=True, blank=True)

    duracao_estimada_min = models.IntegerField(null=True, blank=True)
    duracao_real_min = models.IntegerField(null=True, blank=True)

    status = models.CharField(max_length=30, default='planejada')
    fragmentavel = models.BooleanField(default=False)
    score_prioridade = models.DecimalField(
        max_digits=6, decimal_places=2, default=0
    )

    def __str__(self):
        return self.titulo

class Disciplina(models.Model):
    nome = models.CharField(max_length=120)
    codigo = models.CharField(max_length=20, blank=True)
    professor = models.CharField(max_length=120, blank=True)

    def __str__(self):
        return self.nome

class Compromisso(models.Model):
    CATEGORIAS = [
        ('aula', 'Aula'),
        ('estagio', 'Estágio'),
        ('pessoal', 'Pessoal'),
        ('outro', 'Outro'),
    ]

    titulo = models.CharField(max_length=120)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    inicio = models.DateTimeField()
    fim = models.DateTimeField()

    def __str__(self):
        return self.titulo

class Planejamento(models.Model):
    inicio_semana = models.DateField()
    versao = models.PositiveIntegerField(default=1)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Planejamento da semana {self.inicio_semana} - Versão {self.versao}"

class Bloco(models.Model):
    planejamento = models.ForeignKey(
        'Planejamento',
        on_delete=models.CASCADE,
        related_name='blocos'
    )

    atividade = models.ForeignKey(
        'Atividade',
        on_delete=models.CASCADE,
        related_name='blocos'
    )

    inicio = models.DateTimeField()
    fim = models.DateTimeField()

    status = models.CharField(
        max_length=30,
        default='planejado'
    )

    def __str__(self):
        return f"{self.atividade.titulo} - {self.inicio}"
