from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(
        max_length=20,
        help_text="Formato internacional, ex: +559987777-7777",
    )
    aceita_zap = models.BooleanField(default=True)
    momento_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Veiculo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="veiculos")
    placa = models.CharField(
        max_length=7,
        unique=True,
    )
    modelo = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.modelo} - {self.placa}"

class Servico(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nome

class OrdemServico(models.Model):
    class Status(models.TextChoices):
        AGUARDANDO = "AGUARDANDO", "Aguardando"
        ENTREGUE = "ENTREGUE", "Entregue"

    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE, related_name="ordens")
    servicos = models.ManyToManyField(Servico) # Many To Many: mais para mais, pode ter varias ordens juntas
    status = models.CharField(
        max_length=20, default=Status.AGUARDANDO, choices=Status.choices
    )
    observacoes = models.TextField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Ordem de Serviço: {self.pk} - {self.veiculo}"